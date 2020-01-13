# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    kata01.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: acoudouy <acoudouy@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/01/13 12:55:00 by acoudouy          #+#    #+#              #
#    Updated: 2020/01/13 13:10:59 by acoudouy         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

languages = {
 'Python': 'Guido van Rossum',
 'Ruby': 'Yukihiro Matsumoto',
 'PHP': 'Rasmus Lerdorf',
 }

for item in languages:
	print(item + " was created by " + languages[item])
