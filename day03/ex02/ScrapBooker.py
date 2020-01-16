from ImageProcessor import ImageProcessor
from PIL import Image
import numpy as np

class ScrapBooker():
    def crop(self, array, dim, pos = (0,0)):
        self.size_height = len(array)
        self.size_width = len(array[0])
        if dim[0] + pos[0] > self.size_height or dim[1] + pos[1] > self.size_width:
            print("Dimension larger than the image. Please check dimension or position")
        else:
            new = array[pos[0]:pos[0]+dim[0],pos[1]:pos[1]+dim[1]]
            return(new)
    
    def thin(self, array, n, axis):
        new = np.delete(array,list(range(0,array.shape[axis], n)), axis)
        return (new)

    def juxtapose(self, array, n, axis):
        new = array
        for i in range(n - 1):
            new = np.concatenate((new, array),axis)
        return (new)

    def mosaic(self, array, dim):
        temp = array
        for i in range(dim[0] - 1):
            temp = np.concatenate((temp, array),0)
        new = temp
        for i in range(dim[1] - 1):
            new = np.concatenate((new, temp),1)
        return (new)

test = ImageProcessor()
scrap = ScrapBooker()
array = test.load('42AI.png')
#dim = (100,150)
#new_arr = scrap.crop(array,dim)
#test.display(new_arr)

#new_arr = scrap.thin(array,2,1)
#test.display(new_arr)

#new_arr = scrap.juxtapose(array, 5, 0)
#test.display(new_arr)

#dim = (5,7)
#new = scrap.mosaic(array, dim)
#test.display(new)
