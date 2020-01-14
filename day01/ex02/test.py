from vector import Vector

print("Vector 1")
v1 = Vector([0.0,5.0,10.0,20.0])
print(v1)
print("")

print("Vector 2")
v2 = Vector(5)
print(v2)
print("")


print("Vector 3")
v3 = Vector((3,8))
print(v3)
print("")


print("Vector 4")
v4 = Vector(1)
print(v4)
print("")


print("Vector 5")
v5 = Vector("lol")
print(v5)
print("")

print("Add : v1 + 1")
v6 = v1 + 1
print(v6)
print(v1)
print("")

print("Add : 1 + v1")
v6 = 1 + v1
print(v6)
print(v1)
print("")

print("Add : v3 + v2")
v9 = v3 + v2
print(v9)
print(v3)
print(v2)
print("")

print("Sub : v3 - 2")
v7 = v3 - 2
print(v7)
print(v3)
print("")

print("Sub : 2 - v3")
v7 = 2 - v3
print(v7)
print(v3)
print("")

print("Sub : v3 - v2")
v9 = v3 - v2
print(v9)
print(v3)
print(v2)
print("")

#print("Truediv : v2 / 2")
#v8 = v2 / 2
#print(v8)
#print(v2)
#print("")

print("Mul : v1 * 4")
v8 = v1 * 4
print(v8)
print(v1)
print("")

print("Mul : 5 * v2")
v8 = 5 * v2
print(v8)
print(v2)
print("")

print("Mul : v3 * v2")
v8 = v3 * v2
print(v8)
print(v2)
print(v3)
print("")

print(repr(v1))
