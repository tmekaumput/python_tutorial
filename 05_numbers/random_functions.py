import random

random.seed(1)
print random.random()
print random.choice(['a','b','c'])
list = ['a','b','c']
random.shuffle(list)
print list