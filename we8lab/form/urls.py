from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('<id>/new/', views.new),
    path('<id>/view/', views.view_form_by_id),
]