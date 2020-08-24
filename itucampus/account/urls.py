from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name='account'

urlpatterns=[
    path('signup/', views.signup, name="register"),
    path('activate/<slug:uidb64>/<slug:token>/',
         views.activate, name='activate'),
    path('login/', views.sign_in,name='login'),
    path('logout/',views.sign_out,name='logout'),
    path('confirmation_phase/',views.confirmation_phase,name="confirmation_phase"),
    # path('<username>',views.user_profile,name='user_profile')
]


urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
