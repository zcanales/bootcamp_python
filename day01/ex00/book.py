from recipe import Recipe
from datetime import datetime

class Book:
    """My book as a class"""
    def __init__(self, name, creation_date):
        self.name = name
        self.last_update = creation_date
        self.creation_date = creation_date
        self.recipes_list = []

    def get_recipe_by_name(self, name):
        """Print a recipe with the name 'name' and return the instance"""
        if isinstance(name, str) == 0:
            print("You should give us a recipe name")
        else:
            for item in self.recipes_list:
                if item.name == name:
                    print(name)
                    return (item)
            print("404 Recipe not found")

    def get_recipes_by_types(self, recipe_type):
        """Get all recipe names for a given recipe_type"""
        res = 0
        print("The result for " + recipe_type + " is :")
        if isinstance(recipe_type, str) == 1:
            for item in self.recipes_list:
                if item.recipe_type == recipe_type:
                    print("- " + item.name)
                    res += 1
            if res == 0:
                print("No recipe found for type " + recipe_type + ".")
        else:
            print("You should give us a recipe type")
        print("")

    def add_recipe(self, recipe):
         """Add a recipe to the book and update last_update"""
         if isinstance(recipe, Recipe) == 1:
            self.recipes_list.append(recipe)
            self.last_update = str(datetime.now())
         else:
             print("Mmmh, does not look like a recipe")

