from django.urls import path
from . import views

app_name = 'work1'
urlpatterns = [
    path('',views.home,name='home1'),
     path('ajax-posting/', views.ajax_posting, name='ajax_posting')
]
