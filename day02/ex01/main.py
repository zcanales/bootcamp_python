def what_are_the_vars(*args, **kwargs):
    obj = ObjectC()
    for count, el in enumerate(args):
        string = "var_" + str(count)
        setattr(obj,string,el)
    for arg in kwargs:
        setattr(obj,str(arg), str(kwargs[str(arg)]))
    return (obj)

class ObjectC(object):
    def __init__(self):
        pass

def doom_printer(obj):
    if obj is None:
        print("Error")
        print("End")
        return
    for attr in dir(obj):
        if attr[0] != "_":
            value = getattr(obj, attr)
            print("{}: {}".format(attr, value))
    print("end")

if __name__ == "__main__":
    obj = what_are_the_vars(7)
    doom_printer(obj)
    obj = what_are_the_vars("ft_lol", "hi")
    doom_printer(obj)
    obj = what_are_the_vars()
    doom_printer(obj)
    obj = what_are_the_vars(12, "Yes", [0,0,0], a=10, hello="world")
    doom_printer(obj)
    obj = what_are_the_vars(42, a=10, var_0="world")
    doom_printer(obj)
