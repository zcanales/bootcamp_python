from PIL import Image
import numpy as np
from ImageProcessor import ImageProcessor

class ColorFilter():
    def invert(self, array):
        new = array
        for x in range(len(array)):
            for y in range(len(array[0])):
                for z in range(3):
                    new[x][y][z] = 255 - array[x][y][z]
        return (new)

    def to_blue(self, array):
        new = array
        for x in range(len(array)):
            for y in range(len(array[0])):
                for z in range(3):
                    if z != 2:
                        new[x][y][z] = 0
        return(new) 
            
    def to_green(self, array):
        new = array
        for x in range(len(array)):
            for y in range(len(array[0])):
                for z in range(3):
                    if z != 1:
                        new[x][y][z] = 0
        return(new) 

    def to_red(self, array):
        new = array
        for x in range(len(array)):
            for y in range(len(array[0])):
                for z in range(3):
                    if z != 0:
                        new[x][y][z] = 0
        return(new)

    def celluloid(self, array):
        new = array
        for x in range(len(array)):
            for y in range(len(array[0])):
                for z in range(3):
                    if new[x][y][z] / 64 < 1:
                        new[x][y][z] = 0
                    elif new[x][y][z] / 64 < 2:
                      new[x][y][z] = 64
                    elif new[x][y][z] / 64 < 3:
                        new[x][y][z] = 128
                    else:
                        new[x][y][z] = 186
        return(new)


test = ImageProcessor()
array = test.load('koala.png')
color = ColorFilter()

#new = color.invert(array)
#test.display(new)

#new = color.to_blue(array)
#test.display(new)

new = color.to_green(array)
test.display(new)

#new = color.to_red(array)
#test.display(new)

#new = color.celluloid(array)
#test.display(new)
