from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from .tokens import account_activation_token
from django.core.mail import EmailMessage
from django.utils.http import is_safe_url
from forum.models import Post




# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Hesabınızı Aktifleştirin.'
            message = render_to_string('acc_activate_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token':account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                        mail_subject, message, to=[to_email]
            )
            email.send()
            return redirect('/confirmation_phase')
    else:
        form = RegisterForm()
    return render(request, 'signup.html', {'form': form})



def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        # return redirect('home')
        return redirect('/login')
    else:
        return HttpResponse('Activation link is invalid!')

def confirmation_phase(request):
    return render(request, 'confirm_email.html')

def sign_in(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method=='POST':
            username=request.POST['username']
            password=request.POST['password']
            user=authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                next = request.GET.get('next', '/default/url/')
                if not is_safe_url(next,allowed_hosts=request.get_host()):
                    next = '/default/url/'
                return redirect(next)
            else:
                messages.error(request,'Kullanıcı Adı veya Şifre Yanlış')
                return render(request,"registration/login.html")
        else:
            return render(request,"registration/login.html")

@login_required
def sign_out(request):
    logout(request)
    return redirect('/')


@login_required
def user_profile(request, username):
    if request.user.username != username:
        user = User.objects.get(username=username)
    else:
        user = request.user
    posts=Post.objects.filter(author=user)
    return render(request, "userpage.html", {'profile': user,'posts':posts})
