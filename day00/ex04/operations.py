# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    operations.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: acoudouy <acoudouy@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/01/13 12:09:50 by acoudouy          #+#    #+#              #
#    Updated: 2020/01/13 13:01:25 by acoudouy         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

def RepInt(string):
	try:
		int(string)
		return True
	except ValueError:
		return False

if len(sys.argv) != 3:
	print("You should enter only 2 args")
else:
	if (RepInt(sys.argv[1]) and RepInt(sys.argv[2])):
		a = int(sys.argv[1])
		b = int(sys.argv[2])
		print("Sum: " + str(a +b))
		print("Difference: " + str(a - b))
		print("Product: " + str(a * b))
		if b == 0:
			print("Quotient: ERROR (div by zero)")
		else:
			print("Quotient: " + str(float(a) / float(b)))
		if b == 0:
			print("Remainder: ERROR (modulo by zero)")
		else:
			print("Remainder: " + str(a % b))
	else:
		print("InputError: only numbers")
