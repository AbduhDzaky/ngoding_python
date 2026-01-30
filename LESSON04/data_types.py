import math 
# String data type

# Literal assignment
first = 'Abduh'
last = 'Dzaky'

# print(type(first))
# print(type(first) == str)
# print(isinstance(first, str))

# constructure function
# pizza = str("Papperoni")
# print(type(pizza))
# print(type(pizza) == str)
# print(isinstance(pizza, str))

# Concatenation 
fullname = first + ' ' + last 
print(fullname)

fullname += '!'
print(fullname)

# Casting a number to a string
decade = str(1980) # untuk "merubah" angka menjadi string
print(type(decade)) #untuk mengetahui tipe datanya apa
print(decade)

statement = "I like rock music from the " + decade + "s."
print(statement)

# Multiple line
multiline = '''
Hey, How are you?

i was just checking in

                        All good? 
'''
print(multiline)

# Escaping special characters
sentence = 'I\'m back to work!\tHey!\n\nWhere\'s this at\\located?'
print(sentence)

# String Methods
print(first)
print(first.upper())
print(first.lower())
print(first)

print(multiline.title()) # agar tiap baris baru huruf awalnya kapital
print(multiline.replace("good", "ok")) # untuk mengganti suatu kata menjadi kata lain
print(multiline)

print(len(multiline))
multiline += "                                            "
multiline = "                       " + multiline
print(len(multiline))

print(len(multiline.strip()))
print(len(multiline.lstrip()))
print(len(multiline.rstrip()))

print(' ')

# Build a menu
title = "menu".upper()
print(title.center(20, "=")) 
print("Coffee".ljust(16,".") + "$1".rjust(4))
print("Muffin".ljust(16,".") + "$2".rjust(4))
print("Cheese Cake".ljust(16,".") + "$4".rjust(4))

print('')

# String index values
print(first[1])
print(first[-1])
print(first[1:-1])
print(first[1:])

# Some methods some boolean data 
print(first.startswith('A'))
print(first.endswith('h'))

# Boolean data type
myvalue = True
x = bool(False)
print(type(x))
print(isinstance(myvalue, bool))

# Numeric data types

# integer type
price = 100
best_price = int(80)
print(type(price))
print(isinstance(best_price, int))

# float type
gpa = 3.28
y = float(1.14)
print(type(gpa))

# complex type
comp_value = 5+3j
print(type(comp_value))
print(comp_value.imag) 
print(comp_value.real)

# Built in function for numbers

print(abs(gpa))
print(abs(gpa * -1))

print(round(gpa)) # rounded down poin gpa

print(round(gpa, 1)) # rounded up poin gpa



print(math.pi)
print(math.sqrt(64))
print(math.ceil(gpa))
print(math.floor(gpa))

# Casting a string to a number 
zipcode = "10001"
zip_value = int(zipcode)
print(type(zip_value))

# error if you attempt to cast incorrect data
# zip_value = int("New York")
