from recipe import Recipe
from book import Book



#print("What recipe do you want to add ?")
#name = input()
#print("What is its cooking level ?")
#lvl = input()
#print("What is the cooking time ?")
#time = input()
#print("What are the ingredients ?")
#ingr = input()
#print("What is the description ?")
#des = input()
#print("What is the recipe type ? starter, lunch or dessert ?")
#rec_type = input()
#print()
#rec_to_add = Recipe(name, lvl, time, ingr, des, rec_type)
#to_print = str(rec_to_add)
#print(to_print)

tourte = Recipe("Tourte", 2,25,"flour and dreams","C'est la base","lunch")
cookie = Recipe("Cookie",1,10,"sugard and love","Mmmmmh","dessert")
pasta = Recipe("Pasta",3,125,"pesto, tomatoes","I love pasta","lunch")
bread  = Recipe("Bread and butter",1,1,"bread","","starter")
mybook = Book("Martine fait de la cuisine", 2015)

mybook.add_recipe(tourte)
mybook.add_recipe(cookie)
mybook.add_recipe(pasta)
mybook.add_recipe(bread)
mybook.add_recipe(1)

#if i == 1
#mybook.get_recipe_by_name(bread.name)
#mybook.get_recipe_by_name(cookie.name)
#mybook.get_recipe_by_name("miamm")

#   if i == 2
#        mybook.get_recipes_by_types("lunch")
#        mybook.get_recipes_by_types("starter")
#        mybook.get_recipes_by_types("pocahantas")

i = "0"
while i != "5":
        i = input()
