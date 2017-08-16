# Hey everybody! How are you all? It's been a while since our last session where we explored Lists in Python.
# A quick recap: We've been introduced and worked with the following core data types until now:
# 1) Numbers (Integers, Reals, Complex, and Decimal)
# 2) Booleans 
# 3) Strings
# 4) Tuples
# 5) Lists

# Of these, the first four types are Immutable types, while the fifth one - Lists - is Mutable.

# Now, let's dive into the last data type in Python: Dictionaries.
# Dictionaries are probably the most important data type in Python, and like Lists are mutable.
# However, unlike Lists, Dictionaries aren't sequences. They aren't necessarily a sequence of objects
# that are indexed. Rather, Dictionaries make use of keys. We'll see how this works soon.
# Also, like Lists, Dictionaries are very flexible. They can be expanded and shrunk as needed.
# And like Lists, they are collections of different types of objects - including Lists themselves.

# Let's look at how Dictionaries differ from Lists. Consider the following List declaration:
firstName = 'Kevin';
lastName = 'Sequeira';
age = 25;
city = 'Mumbai';

student001 = [firstName, lastName, age, city];
print('Student 001 Details as a List: ' + str(student001));

# The individual objects within the List can be called with the help of their index numbers:
print('Last Name: ' + str(student001[1]));
print('City: ' + str(student001[3]) + '\n');

# As mentioned before, Dictionaries, unlike Lists, aren't a sequence of indexed objects. Instead,
# Dictionaries make use of 'key: value' pairs. Here's how:
student002 = {'firstName': 'Kevin', 'lastName': 'Sequeira', 'age': 25, 'city': 'Mumbai'};
print('Student 002 Details as a Dictionary: ' + str(student002));
# print('Last Name: ' + str(student002[1]));      # This line of code throws as error. This is because the Dictionary student002 is not indexed.
print('Last Name: ' + str(student002['lastName']));
print('City: ' + str(student002['city']) + '\n');      # These two lines of code fetch the objects by searching their keys.

# Here's another way of declaring and initializing a Dictionary:
student003 = {};
student003['firstName'] = 'Diana';
student003['lastName'] = 'Sequeira';
student003['age'] = 22;
student003['city'] = 'Mumbai';
print('Student 003 Details as a Dictionary: ' + str(student003) + '\n');

# On printing the above line of code, you will discover that the data is not displayed in the same order as it was populated into the Dictionary.
# The line printed is: Student Details as a Dictionary: {'lastName': 'Sequeira', 'age': 22, 'firstName': 'Diana', 'city': 'Mumbai'}

# The same goes for printing the Dictionary student002: 
print('Student 002 Details as a Dictionary: ' + str(student002) + '\n');
# The line printed is: Student Details as a Dictionary: {'age': 25, 'city': 'Mumbai', 'firstName': 'Kevin', 'lastName': 'Sequeira'}
# This makes it clear that Dictionaries do not store data as an 'indexed' sequence of objects, but a 'keyed' sequence of objects.
# Any object within a dictionary can be fetched by accessing its respective 'key'.

# Let's look at a couple of more ways to declare and initialize dictionaries. You can create a dictionary this way:
student004 = dict(firstName = 'Annet', lastName = 'DSouza', age = '24', city = 'Mumbai');
print('Student 004 Details as a Dictionary: ' + str(student004) + '\n');

# Another way is to 'zip' the Dictionary Keys and Values together. This form can be used in cases where dictionaries have
# to be created during application runtime. However, I would avoid it because it's just too long to type!
student005 = dict(zip(['firstName', 'lastName', 'age', 'city'], ['Anushka', 'Mathias', '1', 'Doha']));
print('Student 005 Details as a Dictionary: ' + str(student005) + '\n');

del student001, student002, student003, student004, student005;     # Here, I've deleted the Dictionaries we created, because why keep them if they
                                                                    # aren't going to be used?

# Now that we know how to declare and initialize Dictionaries in Python, let's take it one step further.
# In practical application development, you'll seldom come across cases where you need to create and use
# Dictionaries as simple as the ones made above. The examples we just saw are 'Single Level' Dictionaries.
# They only contain multiple keys. In real-life, you might need to work with 'Multi-level' Dictionaries.

# Let's take the below Dictionary, for example:
student001 = {'1001':
                    {'fullName':
                                {'firstName': 'Kevin', 'lastName': 'Sequeira'},
                     'contactNumber':
                                {'primaryContact': 9619497463, 'secondaryContact': 9323731312},
                     'age': 25,
                     'address': ['Mumbai']
                    }
              }
print('Student 001 Details: ' + '\n' + str(student001) + '\n');
# The output for the above line of code is:
# {'1001': {'fullName': {'firstName': 'Kevin', 'lastName': 'Sequeira'}, 'city': 'Mumbai', 'contactNumber': {'primaryContact': 9619497463, 'secondaryContact': 9323731312}, 'age': 25}}

# Have a nice and careful look at the Dictionary we just created. It's complex, and contains more than one dictionary within itself.
# Let's say we want to add a List of subjects within the Dictionary. Here's how you do it:
student001['1001']['subjects'] = ['Advanced Microwave Engineering', 'Image Processing', 'Neural Networks'];
print('Student 001 Details: ' + '\n' + str(student001) + '\n');

# It's also pretty easy to fetch data from the above Dictionary. Say, you want to display the Student 001's full name:
print('Full Name of Student 001: ' + str(student001['1001']['fullName']['firstName']) + ' ' + str(student001['1001']['fullName']['lastName']) + '\n');

# And if you also want to print the Student 001's city:
print('Address of Student 001: ' + student001['1001']['address'][0] + '\n');     # You see, the data for the key, 1001: address: 'Mumbai' is of type String.
                                                                        # So we don't need to use the str() function for displaying as we've used
# before.

# Let's say we want to extend the address for Student 001:
student001['1001']['address'].append('Borivali (W)');
print('Address of Student 001: ' + student001['1001']['address'][0] + ', ' + student001['1001']['address'][1] + '\n');   
# As you can see, the value of the 'address' key in Student 001 is actually a List containing multiple strings. And that's exactly
# how we have fetched them, using their index numbers.
# The output of the above print statement is:
# Address of Student 001: Mumbai, Borivali (W)

print('Address of Student 001: ' + student001['1001']['address'][1] + ', ' + student001['1001']['address'][0] + '\n');
# In the same manner, the output of the above print statement is:
# Address of Student 001: Borivali (W), Mumbai

# That's all for Dictionaries, for now. We'll definitely revisit Python Dictionaries in the form of a short project
# soon. Before that, we'll dive into some interesting Python statements, and see how they can be used for manipulating
# the flow of your programs.
# Also, we're not completely done with Python data types. There's a couple of simple data types that we shall dive into the next video
# and with that we'll wrap up our series on Python Data Types.
