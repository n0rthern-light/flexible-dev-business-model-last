from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('new/<id>/', views.new),
    path('view/<id>/', views.view_form_by_id),
]