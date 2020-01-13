# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    loading.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: acoudouy <acoudouy@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/01/13 18:21:02 by acoudouy          #+#    #+#              #
#    Updated: 2020/01/13 18:25:51 by acoudouy         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_progress(listy):
	for i in listy:
		yield i * i



listy = range(1000)
ret = 0
for elem in ft_progress(listy):
	ret += (elem + 3) % 5
	sleep(0.01)
print()
print(ret)
