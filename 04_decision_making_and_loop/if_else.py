#Single line expression
var = 100
if ( var == 100 ) : print "Value of expression is 100"
print "Simple!"

#Nested with input
var = int(raw_input('Please enter a number: '))

if var < 200:
   print "Expression value is less than 200"
   if var == 150:
      print "Which is 150"
   elif var == 100:
      print "Which is 100"
   elif var == 50:
      print "Which is 50"
   elif var < 50:
      print "Expression value is less than 50"
else:
   print "Could not find true expression"

# Null value test
var = None
if(var):
    print 'Something in var'
else:
    print 'Nothing in var'

# Null value test
var = 0
if(var):
    print 'var is not zero (TRUE)'
else:
    print 'var is zero (FALSE)'