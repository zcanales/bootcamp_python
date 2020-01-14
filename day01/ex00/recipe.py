class Recipe:
    """My recipe in a class"""
    def __init__(self, name, cooking_lvl, cooking_time, ingredients, description, recipe_type):
        self.name = name
        self.cooking_lvl = cooking_lvl
        self.cooking_time = cooking_time
        self.ingredients = ingredients
        self.description = description
        self.recipe_type = recipe_type
        if isinstance(name, str) == 0:
            print("Name should be a string")
        if name == "":
            print("Your recipe must have a name")
        try:
            cooking_lvl = int(cooking_lvl)
            if cooking_lvl < 0 or cooking_lvl > 5:
                 print("The cooking level should be between 0 and 5 included")
        except ValueError:
            print("The cooking level should be an int")
        if cooking_lvl == 0:
            print("Your recipe must have level")
        try:
            cooking_time = int(cooking_time)
            if cooking_time < 0:
                 print("The cooking time should not be negative")
        except ValueError:
            print("The cooking time should be an int")
        if cooking_time == 0:
            print("Your recipe must have a cooking time")
        if type(ingredients) is not str:
            print("Ingredients should be a string")
        if ingredients == "":
            print("Your recipe must have ingredients")
        if type(recipe_type) is not str:
            print("The recipe type should be a string")
        if recipe_type == "":
            print("Your recipe must have type")
        if recipe_type != "starter" and recipe_type != "lunch" and recipe_type != "dessert":
            print("The recipe type should be either starter, lunch or dessert")

    def __str__(self):
        a = "Recipe for " + self.name + ". "
        b = "Its level is " + str(self.cooking_lvl) + " and its time is " + str(self.cooking_time) + " mn.\n"
        c = "You will need " + self.ingredients + ". "
        d = ""
        if self.description != "":
            d = self.description + ". "
        e = "You should eat it as " + self.recipe_type + ". "
        txt = a + b + c + d + e
        return (txt)
        
