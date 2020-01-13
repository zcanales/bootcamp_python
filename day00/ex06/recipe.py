# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    recipe.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: acoudouy <acoudouy@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/01/13 14:19:55 by acoudouy          #+#    #+#              #
#    Updated: 2020/01/13 16:31:07 by acoudouy         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

cookbook = {
	'sandwich' : {'ingredient' : {'ham', 'bread', 'tomatoes'}, 'meal' : 'lunch', 'prep_time' : '10'},
	'cake' : {'ingredient' : {'flour', 'sugar', 'eggs'}, 'meal' : 'dessert', 'prep_time' : '60'},
	'salad' : {'ingredient' : {'avocado', 'arugula', 'tomatoes', 'spinach'}, 'meal' : 'lunch', 'prep_time' : '15'}
}

def PrintRecipe(recipe):
	if recipe in cookbook:
		print("Recipe for " + recipe + ":")
		ing = str(cookbook[recipe]['ingredient']);
		meal = str(cookbook[recipe]['meal'])
		print("Ingredient list: " + ing[4:len(ing) - 1])
		print("To be eaten for " + meal + ".")
		print("Takes " + str(cookbook[recipe]['prep_time']) + " minutes of cooking.")

def DeleteRecipe(recipe):
	if recipe in cookbook:
		del cookbook[recipe]

def AddRecipe(name, ingr, meal_type, prep_time):
	if name in cookbook:
		print("Entry already exists")
	else:
		i = len(cookbook)
		cookbook.update( {name : {'ingredient' : "XXXX" + ingr + "X", 'meal' : meal_type, 'prep_time' : prep_time}})

def PrintCookbook():
	for item in cookbook:
		PrintRecipe(item)
		print("")

print("Please select an option by typing the corresponding number:")
print("1: Add a recipe")
print("2: Delete a recipe")
print("3: Print a recipe")
print("4: Print the cookbook")
print("5: Quit")
i = input()
while i != 5:
	if i == 1:
		print("Please enter the recipe name to add it (with quotation marks)")
		name = input()
		print("Please enter the recipe ingredients (with quotation marks)")
		ingredients = input()
		print("Please enter the recipe meal type (with quotation marks)")
		meal = input()
		print("Please enter the recipe preparation time (with quotation marks)")
		time = input()
		AddRecipe(name, ingredients, meal, time)
	elif i == 2:
		print("Please enter the recipe name to delete it (with quotation marks)")
		name = input()
		if name in cookbook:
			DeleteRecipe(name)
		else:
			print("Recipe not found")
	elif i == 3:
		print("Please enter the recipe name to print it (with quotation marks)")
		name = input()
		if name in cookbook:
			PrintRecipe(name)
		else:
			print("Recipe not found")
	elif i == 4:
		PrintCookbook()
	elif i == 5:
		print("")
	else:
		print("Wrong number, please enter corresponding number")
	print("")
	print("What do you want to do now ?")
	print("1: Add a recipe")
	print("2: Delete a recipe")
	print("3: Print a recipe")
	print("4: Print the cookbook")
	print("5: Quit")
	i = input()
