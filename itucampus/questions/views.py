from django.shortcuts import render
from django.views import generic
from .models import Question,Answer
from .forms import QuestionForm,AnswerForm
from django.views.generic.edit import FormMixin
from django.urls import reverse

# Create your views here.


class QuestionDetail(FormMixin, generic.DetailView):
    model = Question
    template_name = 'question_detail.html'
    context_object_name = 'question'
    form_class = AnswerForm

    def get_context_data(self, **kwargs):
        context = super(QuestionDetail, self).get_context_data(**kwargs)
        context ['answermodel_list'] = Answer.objects.filter(question=self.object).order_by('created_on')
        context['form'] = AnswerForm(initial={'question': self.object})
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.question = self.get_object()
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('question:question_detail', kwargs={'slug': self.object.slug})


class QuestionList(generic.CreateView):
    template_name = 'question.html'
    form=QuestionForm
    model = Question
    fields=['question','title','body']
    success_url="/sorular"

    def form_valid(self, form):
        form.instance.author=self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ['question_list'] = Question.objects.order_by('-created_on')
        return context
