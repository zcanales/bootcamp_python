class Vector:
    def __init__(self, var):
        i = 0
        self.data = []
        if isinstance(var, list) == 1:
            for item in var:
                if isinstance(item, float) == 0:
                    print("Your list is not only composed by float")
                    return
            self.data = var
        elif isinstance(var, int) == 1:
            while i < var:
                self.data.append(0.0 + i)
                i += 1
        elif isinstance(var, tuple) == 1:
            if len(var) != 2:
                print("Wrong parameter, should be two int")
            elif isinstance(var[0], int) == 0 or isinstance(var[1], int) == 0:
                print("Wrong parameter, they should both be int")
            elif var[1] < var [0]:
                print("2nd parameter should be greater than the 1st one")
            else:
                while i < var[1] - var[0]:
                    self.data.append(var[0] + 0.0 + i)
                    i += 1
        else:
            print("Parameter is not formatted or empty")
            
    def __str__(self):
        """Print Vector Content"""
        string = "(Vector " + str(self.data) + ")"
        return (string)

    def __add__(self, x):
        if isinstance(x, Vector) == 1:
            if len(self.data) != len(x.data):
                print("Vectors are not the same size")
            else:
                j = 0
                v = Vector(len(self.data))
                for item in self.data:
                    v.data[j] = self.data[j] + v.data[j]
                    j += 1
        elif isinstance(x, int) == 0:
            print("The second param should be an int or a vector")
        else:
            j = 0
            v = Vector(len(self.data))
            for i in self.data:
                v.data[j] = self.data[j] + x
                j += 1
        return(v)
    
    def __radd__(self, x):
        if isinstance(x, Vector) == 1:
            if len(self.data) != len(x.data):
                print("Vectors are not the same size")
            else:
                j = 0
                v = Vector(len(self.data))
                for item in self.data:
                    v.data[j] = self.data[j] + v.data[j]
                    j += 1
        elif isinstance(x, int) == 0:
            print("The second param should be an int")
        else:
            j = 0
            v = Vector(len(self.data))
            for i in self.data:
                v.data[j] = self.data[j] + x
                j += 1
        return(v)
    
    def __sub__(self, x):
        if isinstance(x, Vector) == 1:
            if len(self.data) != len(x.data):
                print("Vectors are not the same size")
            else:
                j = 0
                v = Vector(len(self.data))
                for item in self.data:
                    v.data[j] = self.data[j] - v.data[j]
                    j += 1
        elif isinstance(x, int) == 0:
            print("The second param should be an int")
        else:
            j = 0
            v = Vector(len(self.data))
            for i in self.data:
                v.data[j] = self.data[j] - x
                j += 1
        return(v)
    
    def __rsub__(self, x):
        if isinstance(x, Vector) == 1:
            if len(self.data) != len(x.data):
                print("Vectors are not the same size")
            else:
                j = 0
                v = Vector(len(self.data))
                for item in self.data:
                    v.data[j] = v.data[j] - self.data[j]
                    j += 1
        elif isinstance(x, int) == 0:
            print("The second param should be an int")
        else:
            j = 0
            v = Vector(len(self.data))
            for i in self.data:
                v.data[j] = x - self.data[j]
                j += 1
        return(v)
    
    def __truediv__(self, x):
        if isinstance(x, int) == 0:
            print("The second param should be an int")
        else:
            j = 0
            v = Vector(len(self.data))
            for i in self.data:
                v.data[j] = self.data[j] / x
                j += 1
        return(v)
    
    def __rtruediv__(self, x):
        if isinstance(x, int) == 0:
            print("The second param should be an int")
        else:
            j = 0
            v = Vector(len(self.data))
            for i in self.data:
                v.data[j] = self.data[j] / x
                j += 1
        return(v)
