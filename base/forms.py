from django.forms import ModelForm
from .models import Restaurant, Recipe, Ingredient



class RestaurantForm(ModelForm):
    class Meta:
        model = Restaurant
        fields = '__all__'
        
class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        fields = '__all__'
        
        
class IngredientForm(ModelForm):
    class Meta:
        model = Ingredient
        fields = '__all__'
        