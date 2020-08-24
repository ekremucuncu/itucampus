from django.shortcuts import render
from .forms import AdForm
from .models import Ad
from django.views import generic
from django.urls import reverse

class AdList(generic.CreateView):
    model= Ad
    template_name='ad.html'
    fields=['title','body']


    def form_valid(self, form):
        form.instance.ad=self.object
        form.instance.author = self.request.user
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
            return reverse('ad:ad')


    def get_context_data(self, **kwargs):
        kwargs['ad_list'] = Ad.objects.order_by('-created_on')
        return super(AdList, self).get_context_data(**kwargs)
