def ft_reduce(fun, lst):
    res = 0
    for count, el in enumerate(lst):
        if count == 0:
            res += fun(lst[count], lst[count + 1]) 
        elif count < len(lst) - 1:
            res = fun(res, lst[count + 1]) 
    return (res)


def fun(x,y):
    if x == 1 and y == 1:
        return (True)
    return (False)

l = [0,0,0,0]
print(ft_reduce(fun, l))


l = [1,1,1,1]
print(ft_reduce(fun, l))

l = [1,1,0,1]
print(ft_reduce(fun, l))

l = [1,2,3]
print(ft_reduce(lambda x, y: x * y + 1, l))
