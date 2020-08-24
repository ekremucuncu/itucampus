from django.shortcuts import render
from django.views import generic
from .forms import WPGroupForm
from .models import WPGroup
# Create your views here.


class WPGroupView(generic.CreateView):
    template_name='wp.html'
    form_class=WPGroupForm
    model=WPGroup
    success_url='success/'

def scs(request):
    return render(request,'success.html')
