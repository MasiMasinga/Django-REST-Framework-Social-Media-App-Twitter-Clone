from django.urls import path
from .views import UsernameUpdateView, EmailUpdateView, PasswordUpdateView

urlpatterns = [
    path('update/username/', UsernameUpdateView.as_view(), name='username_update'),
    path('update/email/', EmailUpdateView.as_view(), name='email_update'),
    path('update/password/', PasswordUpdateView.as_view(), name='password_update'),
]