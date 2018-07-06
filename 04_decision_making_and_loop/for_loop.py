for letter in ['a','b','c','d']: # Loop through list items
   print 'Current Letter :', letter

for number in range(1,10):        # Loop through counter
   print 'Current number :', number

items = ['item1', 'item2',  'item3']
for index in range(len(items)):
   print 'Current item :', items[index]


lower = 10
upper = 20
# uncomment the following lines to take input from the user
#lower = int(input("Enter lower range: "))
#upper = int(input("Enter upper range: "))
print("Prime numbers between",lower,"and",upper,"are:")
for num in range(lower,upper + 1):
    for i in range(2,num):
        if (num % i) == 0:
            print 'zero'
            break
    else:
        print '%d is a prime number \n' %(num),