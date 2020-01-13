# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    kata04.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: acoudouy <acoudouy@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/01/13 13:59:02 by acoudouy          #+#    #+#              #
#    Update: 2020/01/13 14:13:35 by acoudouy         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ZeroOrNot(num):
	if num < 10:
		return ("0" + str(num))
	else:
		return (str(num))

t = ( 0,4,132.42222,10000,12345.67)
day = ZeroOrNot(t[0])
ex = ZeroOrNot(t[1])
res = float(t[2])
exp = float(t[3])
power = 0
while exp >= 10:
	power += 1
	exp = exp / 10
power = ZeroOrNot(power)
exp1 = float(t[4])
power1 = 0
while exp1 >= 10:
	power1 += 1
	exp1 = exp1 / 10
power1 = ZeroOrNot(power1)
print("day_" + day + ", ex_" + ex + " : " + str("%.2f" % res) + ", " + str("%.2f" % exp) + "e+" + power + ", " + str("%.2f" % exp1) + "e+" + power1)
