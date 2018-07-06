# Declaring tuple variables
# They can be of different types
tup1 = ('physics', 'chemistry', 1997, 2000);
tup2 = (1, 2, 3, 4, 5 );
tup3 = "a", "b", "c", "d";

# Empty tuple
tup4 = ();

# Single tuple requires to have , at the end
tup5 = (50,);

# Access tuple - similar to list
print "tup1[0]: ", tup1[0];
print "tup2[1:5]: ", tup2[1:5];

# Tuples are immutable but we can join them or copy values to create new one
tup6 = tup1 + tup2;
print tup6;

tup7 = tup1[1:2]
print tup7;

# Get length
print len(tup1)

# Repetition
print tup1 * 2

# membership
print 'physics' in tup1