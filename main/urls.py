from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('time/', views.date_t, name='time'),
    path('script/', views.script_view, name='script'),
]