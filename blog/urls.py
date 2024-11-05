from django.urls import path
from . import views

urlpatterns = [
    
    path("", views.blog, name="blog"),
    path("category/<int:category_id>", views.category, name="category"), #"<category_id>" hace referencia al id como lo dice la palabra, buscara por id
    
 ]
