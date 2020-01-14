from recipe import Recipe

def RepInt(string):
	try:
		int(string)
		return True
	except ValueError:
		return False

def __str__(self):
    """Return the string to print with the recipe info"""
    print("Hello")


name = input()
lvl = input()
time = input()
ingr = input()
des = input()
rec_type = input()

rec_to_add = Recipe(name, lvl, time, ingr, des, rec_type)
print(rec_to_add.description)
