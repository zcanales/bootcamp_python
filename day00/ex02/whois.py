# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    whois.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: acoudouy <acoudouy@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/01/13 11:10:17 by acoudouy          #+#    #+#              #
#    Updated: 2020/01/13 11:31:23 by acoudouy         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

def RepInt(string):
	try:
		int(string)
		return True
	except ValueError:
		return False

if len(sys.argv) != 2:
	print("ERROR, not the right number of args")
else:
	if RepInt(sys.argv[1]):
		number=int(sys.argv[1])
		if number == 0:
			print("I'm Zero.")
		elif number % 2 == 0:
			print("I'm Even.")
		else:
			print("I'm Odd.")
	else:
		print("Error, arg not an int")
