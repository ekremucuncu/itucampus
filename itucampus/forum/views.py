from django.views import generic
from django.views.generic.edit import FormMixin
from .models import Post,Comment
from .forms import PostForm,CommentForm
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from django.utils.http import is_safe_url




# Create your views here.


class PostDetail(FormMixin, generic.DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post'
    form_class = CommentForm

    def get_context_data(self, **kwargs):
        context = super(PostDetail, self).get_context_data(**kwargs)
        context ['commentmodel_list'] = Comment.objects.filter(post=self.object).order_by('created_on')
        context['form'] = CommentForm(initial={'post': self.object})
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.instance.author_security = self.request.user
        form.instance.post = self.get_object()
        if form.instance.anonn==True:
            pass
        else:
            form.instance.author=self.request.user
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('forum:post_detail', kwargs={'slug': self.object.slug})



class PostList(generic.CreateView):
    template_name = 'forum.html'
    form=PostForm
    model = Post
    fields=['post']
    success_url="/forum"

    def form_valid(self, form):
        form.instance.author=self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ['postmodel_list'] = Post.objects.order_by('-created_on')
        return context


def delete_comment(request,slug=None,comment_id=None):
    comment_delete=Comment.objects.get(id=comment_id)
    comment_delete.delete()
    next = request.GET.get('next', '/default/url/')
    if not is_safe_url(next,allowed_hosts=request.get_host()):
        next = '/default/url/'
    return redirect(next)
