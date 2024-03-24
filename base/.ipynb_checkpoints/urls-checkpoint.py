from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('list-restaurant/', views.listRestaurant, name='list-restaurant'),
    path('restaurant/<str:pk>/', views.readRestaurant, name='detail-restaurant'), 
    path('create-restaurant/', views.createRestaurant, name = 'create-restaurant'),
    path('update-restaurant/<str:pk>/', views.updateRestaurant, name = 'update-restaurant'),
    path('delete-restaurant/<str:pk>/', views.deleteRestaurant, name = 'delete-restaurant'),

    path('list-recipe/', views.listRecipe, name='list-recipe'), 
    path('recipe/<str:pk>', views.readRecipe, name='detail-recipe'), 
    path('create-recipe/', views.createRecipe, name = 'create-recipe'),
    path('update-recipe/<str:pk>/', views.updateRecipe, name = 'update-recipe'),
    path('delete-recipe/<str:pk>/', views.deleteRecipe, name = 'delete-recipe'),
    
    path('list-ingredient/', views.listIngredient, name='list-ingredient'), 
    path('ingredient/<str:pk>', views.readIngredient, name='detail-ingredient'), 
    path('create-ingredient/', views.createIngredient, name = 'create-ingredient'),
    path('update-ingredient/<str:pk>/', views.updateIngredient, name = 'update-ingredient'),
    path('delete-ingredient/<str:pk>/', views.deleteIngredient, name = 'delete-ingredient'),
]