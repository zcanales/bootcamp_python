from PIL import Image
from NumPyCreator import NumPyCreator
import numpy as np

class ImageProcessor():
    
    def __enter__(self):
        try:
            self.fd = Image.open(self.path)
            self.size = self.fd.size
            print("Loading image of dimensions " + str(self.size[0]) + " x " + str(self.size[1]))
        except IOError:
            print("File not found")
            exit()
        return (self)

    def __exit__(self, type, value, traceback):
        self.fd.close()

    def load(self, path):
        self.path = path
        if self.path[-4:] != ".png":
            print("It's not a .png file")
        else:
            self.__enter__()
            pix = self.fd.load()
            data = np.array(self.fd)
            return (data)

    def display(self, array):
        img = Image.fromarray(array, 'RGB')
        img.show()

test = ImageProcessor()
imp = test.load('42AI.png')
test.display(imp)
