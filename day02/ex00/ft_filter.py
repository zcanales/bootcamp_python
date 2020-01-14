def ft_filter(fun, lst):
    res = []
    for count, el in enumerate(lst):
        if fun(el) == True:
            res.append(el)
    return(res)

lst = range(20)
print(ft_filter(lambda x: x > 14, lst))
