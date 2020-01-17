import numpy as np
import math
from ImageProcessor import ImageProcessor

class AdvancedFilter():
    def mean_blur(self, array):
        kernel = np.full((3,3),1)
        temp = np.full((3,3),0)
        kernel_sum = 0
        tot_sum = 0
        for x in kernel:
            for y in kernel[x]:
                kernel_sum += kernel[x][y]
        for z in range(3):
            for x in array:
                for y in array[x]:
                    temp[x % 3][y % 3][z % 3] = kernel[x % 3][y % 3][z] * array[x][y][z]
                    tot_sum += temp[x % 3][y % 3][z]
                    if x % 3 == 2 and y % 3 == 2:
                        tot_sum = tot_sum / kernel_sumY


test = ImageProcessor()
array = test.load('rick.png')
advfilter = AdvancedFilter()

t = advfilter.gaussianBlur(array, 3,1)

#new = advfilter.mean_blur(array)
#test.display(new)
