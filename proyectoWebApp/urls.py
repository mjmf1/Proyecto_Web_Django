from django.urls import path
from proyectoWebApp import views

urlpatterns = [
    path("", views.home, name = "Home"),
    path("servicios", views.servicios, name = "Servicios"),
    path("tienda", views.tienda, name = "Tienda"),
    path("blog", views.blog, name = "Blog"),
    path("contacto", views.contacto, name = "contacto"),
]