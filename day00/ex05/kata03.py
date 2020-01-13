# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    kata03.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: acoudouy <acoudouy@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/01/13 13:53:26 by acoudouy          #+#    #+#              #
#    Updated: 2020/01/13 13:58:17 by acoudouy         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

phrase = "The right format"
length = len(phrase)
i = 0
string = ""
while i < 41 - length:
	string += "-"
	i += 1
string += phrase
print(string)
