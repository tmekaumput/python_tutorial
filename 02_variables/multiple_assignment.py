#a,b,c point to the same location in memory
a = b = c = 1
print('Value [a] = ', a)
print('Value [b] = ', b)
print('Value [c] = ', c)
print('Memory Address [a] = ' + hex(id(a)))
print('Memory Address [b] = ' + hex(id(b)))
print('Memory Address [c] = ' + hex(id(c)))

del(b)
try:
    print('Value [b] = ', b)
except NameError, e:
    print(e)