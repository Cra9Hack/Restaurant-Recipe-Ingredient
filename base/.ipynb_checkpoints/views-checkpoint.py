from django.shortcuts import render, redirect
from .models import Restaurant, Recipe, Ingredient
from .forms import RestaurantForm, RecipeForm, IngredientForm
from django.db.models import Q
# Create your views here.


def home(request):
    return render(request, 'base/home.html' )


#CRUD RESTAURANT
#Function to list restaurants with filter for a recipe
def listRestaurant(request):
    if request.GET.get('q') != None:
        q=request.GET.get('q')
        restaurants = Restaurant.objects.filter(recipes__name__icontains = q)
    else: 
        q=None
        restaurants = Restaurant.objects.all()
    recipes = Recipe.objects.all()
    context = {'restaurants': restaurants, 'recipes':recipes , 'q':q}
    return render(request, 'base/restaurant_list.html', context )

#Displays the name, description and lists of recipes and ingredients available in the restaurant
def readRestaurant(request, pk):
    restau = Restaurant.objects.get(id=pk)
    recipes = restau.recipes.all()
    ingredients = Ingredient.objects.filter(recipe__restaurant__name = restau.name).distinct()
    context = {'restaurant':restau, 'recipes':recipes, 'ingredients':ingredients}  
    return render(request, 'base/restaurant_detail.html', context)

#Creates a new restaurant, fill up name, descr and list of recipes from the list of the already existing ones
def createRestaurant(request):
    form = RestaurantForm()
    if request.method == 'POST':
        form = RestaurantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list-restaurant')
    context = {'form':form}
    return render(request, 'base/restaurant_form.html', context)

#Edits every field of the restaurant apart from timestamps
def updateRestaurant(request, pk):
    restaurant = Restaurant.objects.get(id=pk)
    form = RestaurantForm(instance = restaurant)
    if request.method == 'POST':
        form = RestaurantForm(request.POST, instance = restaurant)
        if form.is_valid():
            form.save()
            return redirect('list-restaurant')
    context = {'form':form}
    return render(request, 'base/restaurant_form.html', context)

#deletes a restaurant from the database
def deleteRestaurant(request, pk):
    restaurant = Restaurant.objects.get(id=pk)
    if request.method == 'POST':
        restaurant.delete()
        return redirect('list-restaurant')
    return render(request, 'base/delete.html', {'obj': restaurant})



#CRUD RECIPE
#Displays a list of recipes with filters for a chosen restaurant and ingredient
def listRecipe(request):     
    if request.GET.get('q') != None:
        q=request.GET.get('q')
        recipes = Recipe.objects.filter(restaurant__name = q)
    else: 
        q=None
        recipes = Recipe.objects.all()
    if request.GET.get('p') !=None:
        p=request.GET.get('p')
        recipes = recipes.filter(ingredients__name = p)
    else:
        p=None
    restaurants = Restaurant.objects.all()
    ingredients = Ingredient.objects.all()
    context = {'restaurants': restaurants, 'recipes':recipes, 'ingredients': ingredients, 'q':q, 'p':p}
    return render(request, 'base/recipe_list.html', context )

#Displays a selected recipe and shows all the used ingredients and all the restaurants that serve it
def readRecipe(request, pk):
    recipe = Recipe.objects.get(id=pk)
    ingredients = recipe.ingredients.all()
    restaurants = Restaurant.objects.filter(recipes__name = recipe.name).distinct()
    context = {'recipe':recipe, 'ingredients':ingredients, 'restaurants':restaurants}
    return render(request, 'base/recipe_detail.html', context)

#creates new recipe, fill up name, descr and select ingredients from the list of the already existing ones
def createRecipe(request):
    form = RecipeForm()
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list-recipe')
    context = {'form':form}
    return render(request, 'base/recipe_form.html', context)

#edit an existing recipe, can change every field apart from timestamps
def updateRecipe(request, pk):
    recipe = Recipe.objects.get(id=pk)
    form = RecipeForm(instance = recipe)
    if request.method == 'POST':
        form = RecipeForm(request.POST, instance = recipe)
        if form.is_valid():
            form.save()
            return redirect('list-recipe')
    context = {'form':form}
    return render(request, 'base/recipe_form.html', context)

#delete an existing recipe from the database
def deleteRecipe(request, pk):
    recipe = Recipe.objects.get(id=pk)
    if request.method == 'POST':
        recipe.delete()
        return redirect('list-recipe')
    return render(request, 'base/delete.html', {'obj': recipe})



#CRUD INGREDIENT

#Displays a list of ingredients with filters for a chosen restaurant and recipe
def listIngredient(request):
    
    if request.GET.get('q') != None:
        q=request.GET.get('q')
        ingredients = Ingredient.objects.filter(recipe__name = q)
    else: 
        ingredients = Ingredient.objects.all()
        q=None
    if request.GET.get('p') !=None:
        p=request.GET.get('p')
        ingredients = Ingredient.objects.filter(recipe__restaurant__name = p).distinct()
    else:
        p=None   
    restaurants = Restaurant.objects.all()
    recipes = Recipe.objects.all()
    context = {'ingredients': ingredients, 'recipes':recipes, 'restaurants':restaurants, 'q':q, 'p':p }
    return render(request, 'base/ingredient_list.html', context )

#Displays a selected ingredient and lists of recipes and restaurants that use it
def readIngredient(request, pk):
    ingredient = Ingredient.objects.get(id=pk)
    recipes = ingredient.recipe_set.all()
    restaurants = Restaurant.objects.filter(recipes__ingredients__name = ingredient.name).distinct()
    context = {'ingredient':ingredient, 'recipes':recipes, 'restaurants':restaurants}
    return render(request, 'base/ingredient_detail.html', context)

#create a new ingredients, fill up its name
def createIngredient(request):
    form = IngredientForm()
    if request.method == 'POST':
        form = IngredientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list-ingredient')
    context = {'form':form}
    return render(request, 'base/ingredient_form.html', context)

#edit and existing ingredient, change its name
def updateIngredient(request, pk):
    ingredient = Ingredient.objects.get(id=pk)
    form = IngredientForm(instance = ingredient)
    if request.method == 'POST':
        form = IngredientForm(request.POST, instance = ingredient)
        if form.is_valid():
            form.save()
            return redirect('list-ingredient')
    context = {'form':form}
    return render(request, 'base/ingredient_form.html', context)

#delete an existing ingredient
def deleteIngredient(request, pk):
    ingredient = Ingredient.objects.get(id=pk)
    if request.method == 'POST':
        ingredient.delete()
        return redirect('list-ingredient')
    return render(request, 'base/delete.html', {'obj': ingredient})