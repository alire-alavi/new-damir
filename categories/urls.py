from django.urls import path

app_name= 'categories'

from . import views

urlpatterns = [
    path('', views.category_list_view, name="categories-list"),
    path('<name>/', views.by_category, name="by_category"),
]