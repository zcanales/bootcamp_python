class Recipe:
    """My recipe in a class"""
    def __init__(self, name, cooking_lvl, cooking_time, ingredients, description, recipe_type):
        self.name = name
        self.cooking_lvl = cooking_lvl
        self.cooking_time = cooking_time
        self.ingredients = ingredients
        self.description = description
        self.recipe_type = recipe_type

    if type(name) != str
        print("Name should be a string")
        exit()
    try:
        cooking_lvl = int(cooking_lvl)
        if cooking_lvl < 0 or cooking_lvl > 5
             print("The cooking level should be between 0 and 5 included")
             exit()
    except ValueError:
        print("The cooking level should be an int")
        exit()
    try:
        cooking_time = int(cooking_time)
        if cooking_time < 0
             print("The cooking time should not be negative")
             exit()
    except ValueError:
        print("The cooking time should be an int")
        exit()
    if type(ingredients) is not str 
        print("Ingredients should be a string")
    if type(recipe_type) is not str
        print("The recipe type should be a string")
    if recipe_type != "starter" and recipe_type != "lunch" and recipe_type != dessert
        print("The recipe type should be either starter, lunch or dessert")

