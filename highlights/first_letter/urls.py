from django.urls import path
from . import views

urlpatterns = [
    path('', views.first, name="first"),
    path('<letter>', views.first, name="first"),
]
