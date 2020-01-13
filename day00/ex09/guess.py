# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    guess.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: acoudouy <acoudouy@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/01/13 17:54:38 by acoudouy          #+#    #+#              #
#    Updated: 2020/01/13 18:32:03 by acoudouy         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import random

def RepInt(string):
	try:
		int(string)
		return True
	except ValueError:
		return False

print("This is an interactive guessing game!")
print("You have to enter a number between 1 and 99 to find out the secret number.")
print("Type 'exit' to end the game.")
print("Good luck!")
print("")
print("What's your guess between 1 and 99?")
n = random.randint(1,99)
i = input()
intent = 0
win = 0
while i != "exit" and win == 0:
	if RepInt(i) == False:
		print("That's not a number, try again")
	else:
		j = int(i)
		if j > n:
			print("Too high !")
			intent += 1
		elif j < n:
			print("Too low !")
			intent += 1
		else:
			print("Congratulation, you've got it!")
			print("You won in " + str(intent) + " attempts !")
			win = 1
			if n == 42:
				print("D apres mon medecin, je souffre d une malformation de la glande altruiste assortie d une deficience de la fibre morale et en consequence je suis dispense de sauver les Univers.")
	if win == 0:
		i = input()
print("Goodbye !")
