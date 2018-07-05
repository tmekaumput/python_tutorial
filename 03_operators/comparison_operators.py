operators = ['==', '!=', '<>', '>', '<', '>=', '<=']
a = 10
b = 20
print 'a = ',a
print 'b = ',b

for operator in operators:
    expression = 'a' + operator + 'b'
    result = eval(expression)
    print expression,'=',result
