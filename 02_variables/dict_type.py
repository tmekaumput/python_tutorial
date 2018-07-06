# Declaration of Dictionary type
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

# Access values using keys
print "dict['Name']: ", dict['Name']
print "dict['Age']: ", dict['Age']

# Values can be updated
dict['Age'] = 10
print "dict['Age']: ", dict['Age']

# Length
print len(dict)

# Get keys
print dict.keys()

# Get value with default value
print dict.get('Unknown', 'default')

# Copy
print 'Original: ' + hex(id(dict))
print 'Copy: ' + hex(id(dict.copy()))

# Individual key can be delete
del dict['Class']
print dict.has_key('Class')

# Clear all data
dict.clear()
print dict