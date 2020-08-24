from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns



app_name='forum'

urlpatterns=[
     path('', views.PostList.as_view(), name='post'),
     path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
     path('delete/<slug:slug>/<comment_id>/',views.delete_comment,name='delete')
]



urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
