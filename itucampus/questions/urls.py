from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


app_name='question'

urlpatterns=[
     path('', views.QuestionList.as_view(), name='question'),
     path('<slug:slug>/', views.QuestionDetail.as_view(), name='question_detail'),

]



urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
