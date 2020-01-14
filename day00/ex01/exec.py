import sys

for arg in sys.argv:
    str = ' '.join(sys.argv[1:])
    length = len(str)
    str += " "

str = str.swapcase()
slicedString = str[length - 1::-1]
print(slicedString)
