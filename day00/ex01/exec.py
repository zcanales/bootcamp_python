# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    exec.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: acoudouy <acoudouy@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/01/13 10:08:25 by acoudouy          #+#    #+#              #
#    Updated: 2020/01/13 11:21:52 by acoudouy         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

for arg in sys.argv:
	str=' '.join(sys.argv[1:])
	length=len(str)
	str += " "

str=str.swapcase()
slicedString=str[length-1::-1]
print (slicedString)
