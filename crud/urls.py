from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
urlpatterns = [

    path('password_reset/', 
        views.PasswordEmailSender.as_view(), name='password_reset'),

    path('reset/<uidb64>/<token>/',views.InputsChange.as_view(),
         name='password_reset_confirm'),
    
    path('reset/done/',views.SuccessPasswordChangeDone.as_view(),name='password_reset_complete'),

    path('password_reset/done/',views.success_email,name='password_reset_done')

]
