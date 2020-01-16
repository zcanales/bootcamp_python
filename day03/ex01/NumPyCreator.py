import numpy as np
import random

class NumPyCreator():
    def from_list(self, lst):
        np_array = np.array(lst)
        return(np_array)
    def from_tuple(self, tpl):
        np_array = np.asarray(tpl)
        return(np_array)
    def from_iterable(self, itr):
        np_array = np.fromiter(itr, 'int64')
        return(np_array)
    def from_shape(self, shape, value):
        np_array = np.full(shape, value)
        return(np_array)
    def random(self, shape):
        np_array = np.random.random_sample(shape)
        return(np_array)

    def identity(self, n):
        np_array = np.identity(n)
        return(np_array)
