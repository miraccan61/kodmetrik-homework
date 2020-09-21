from django.urls import path

from .views import SignUpView,validate_username
app_name = 'work3'

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('ajax/validate_username/', validate_username, name='validate_username'),
]