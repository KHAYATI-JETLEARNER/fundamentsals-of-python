#rules for creating variables
#1. variable names can only contain letters, numbers and underscores
#2. variable names cannot start with a number
#3. variable names cannot be a reserved keyword in python

#creating variables
name = "khayati"
age = 30
print("my name is",name)
print("i am ",age,"years old")

#datatypes
#float--- any decimal number
#string/str --- any character inside inverted commas
#boolean --- true or false
#integer/int --- whole number

x=10
print(type(x))

#string concatination(adding strings together)
text="hello"
text1=" World"

ftext=text+text1
print(ftext)

print("my name is "+"Khayati Jain")

#type conversion
print("my height is "+str(5))

marks="math :"
number=20
print(marks + str(number))