from django.contrib import admin
from django.urls import path, include
from .views import home, salvar_produto, editar_produto, update_produto

urlpatterns = [
    path("", home),
    path("salvar/", salvar_produto, name="salvar_produto"),
    path("editar/<int:id>/", editar_produto, name="editar_produto"),
    path("update/<int:id>/", update_produto, name="update_produto"),
]