from random import shuffle

def generator(txt, sep, option="None"):
    if isinstance(txt, str) == 0:
        print("The text must be a string")
    elif isinstance(sep, str) == 0:
        print("The sep must br a string")
    else:
        res = txt.split(sep)
        if option == "ordered":
            res.sort()
        elif option == "unique":
            a = []
            for word in res:
                if word not in a:
                    a.append(word)
            return (a)
        elif option == "shuffle":
            shuffle(res)
        return (res)


t = "Coucou je vais bien ne 1 t'en fais pas. la vie va 4 bon train je 2 la vie coin 3 coin hallelujah va"
for word in generator(t," "):
    print(word)
print("")
print("")
for word in generator(t," ", "unique"):
    print(word)
print("")
print("")
for word in generator(t," ", "shuffle"):
    print(word)
print("")
print("")
for word in generator(t," ", "ordered"):
    print(word)
print("")
print("")
