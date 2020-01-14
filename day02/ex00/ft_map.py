def ft_map(fun, lst):
    res = []
    for count, el in enumerate(lst):
        res.append(fun(el))
    return(res)

lst = [0,2,4,5,6]
print(ft_map(lambda x: x + x, lst))
