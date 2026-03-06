from django.contrib import admin
from django.urls import path, include
from .views import home, salvar_categoria, editar_categoria, update_categoria, deletar_categoria

urlpatterns = [
    path("", home),
    path("salvar/", salvar_categoria, name="salvar_categoria"),
    path ("editar/<int:id>/", editar_categoria, name="editar_categoria"),
    path ("update/<int:id>/", update_categoria, name="update_categoria"),
    path("deletar/<int:id>/", deletar_categoria, name="deletar_categoria"),
]