# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    filterwords.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: acoudouy <acoudouy@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/01/13 16:32:33 by acoudouy          #+#    #+#              #
#    Updated: 2020/01/13 16:49:29 by acoudouy         ###   ########.fr        #
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
	print("ERROR")
elif RepInt(sys.argv[1]):
	print("ERROR")
elif RepInt(sys.argv[2]):
	word_list = sys.argv[1].split()
	res = []
	i = 0
	while i < len(word_list):
		if len(word_list[i]) >= int(sys.argv[2]):
			res.append(word_list[i])
		i += 1
	print(res)
else:
	print("ERROR")
