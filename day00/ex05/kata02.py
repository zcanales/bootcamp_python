# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    kata02.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: acoudouy <acoudouy@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/01/13 13:11:14 by acoudouy          #+#    #+#              #
#    Updated: 2020/01/13 13:18:42 by acoudouy         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

t = (3,30,2019,9,25)
if t[3] < 10:
	month = "0" + str(t[3])
else:
	month = str(t[3])
if t[4] < 10:
	day = "0" + str(t[4])
else:
	day = str(t[4])
year = str(t[2])
if t[0] < 10:
	hour = "0" + str(t[0])
else:
	hour = str(t[0])
if t[1] < 10:
	minute = "0" + str(t[1])
else:
	minute = str(t[1])
print(month + "/" + day + "/" + year + " " + hour + ":" + minute)
