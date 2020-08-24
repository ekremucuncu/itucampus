from django.urls import path
from . import views


app_name='ad'

urlpatterns=[
    path('',views.AdList.as_view(),name='ad')
]
