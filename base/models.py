from django.db import models

# Create your models here.
    

class Ingredient(models.Model):
    """
    fields:
        name - name of the ingredient, a string 
        updated,createdand - timestamps
    """
    name = models.CharField(max_length = 200)
    updated = models.DateTimeField(auto_now = True)#takes a snapshot every time it's saved
    created = models.DateTimeField(auto_now_add = True)#takes a snapshot only the first time it's save
    
    class Meta:
        ordering = ['-updated', '-created']    
        
    def __str__(self):
        return self.name
    
class Recipe(models.Model):
    """
    fields:
        name - name of the recipe, a string 
        ingredients - list of the ingredients, connected by many2many relation to the ingredients table
        description - recipe instruction/description, a string
        updated,createdand - timestamps
    """
    name = models.CharField(max_length = 200)
    ingredients = models.ManyToManyField(Ingredient)
    description = models.TextField(null=True , blank = True)
    updated = models.DateTimeField(auto_now = True)#takes a snapshot every time it's saved
    created = models.DateTimeField(auto_now_add = True)#takes a snapshot only the first time it's save
        
    class Meta:
        ordering = ['-updated', '-created']
        
    def __str__(self):
        return self.name

class Restaurant(models.Model):
    """
    fields:
        name - name of the recipe, a string 
        recipes - list of the recipes available in the restraurant, connected by many2many relation to the recipes table
        description - restaurant description, a string
        updated,createdand - timestamps
    """
    name = models.CharField(max_length = 200)
    description = models.TextField(null=True , blank = True)
    recipes = models.ManyToManyField(Recipe)
    updated = models.DateTimeField(auto_now = True)#takes a snapshot every time it's saved
    created = models.DateTimeField(auto_now_add = True)#takes a snapshot only the first time it's save

    class Meta:
        ordering = ['-updated', '-created']
        
    def __str__(self):
        return self.name 
    
