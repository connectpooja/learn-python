#In this, we will learn the variables
#Python unlike the other languages, don't have any particular syntax to define variables

x = 5 #x is the the variable here, = is the assignment operator, 5 is the assinged value
# here, the assigned 5 is an integer which defined by int

print(x) 

# I have a value 6
stringVariable = str(6)
integerVariable = int(6)
floatVariable = float(6)

# varA = int('a')
# print(varA)
varB = str('b')
print(varB)
# varC = float('c')
# print(varC)
print(ord('A'))

print(stringVariable)
print(integerVariable)
print(floatVariable)

print(type(stringVariable))
print(type(integerVariable))
print(type(floatVariable))

#More on Variables
#Usage of Single Quotes and Double Quotes
x = "Pooja"
#this is the exact same thing as writing 
x = 'Pooja'

#variable name are case sensitive
a = 5
A = 7

pooja = 7
Pooja = 8
PoOja = 9
PoOjA = 10

#my variable -->  #this is not acceptable because there is a space in between it
#my-variable --> Because there is a hyphen in the middle, but the actual reason is python is trating the hyphen as substraction

#below is some examples of acceptable variable naming conventions
myVariable = "Fine"
myvariable = "This is also fine"
my_variable = "This is also fine"
_myVariable = "This is also fine"
MYVAR = "This is also fine"

myVar2 = "This is acceptable"
#but
# 2myVar -> This is not acceptable

