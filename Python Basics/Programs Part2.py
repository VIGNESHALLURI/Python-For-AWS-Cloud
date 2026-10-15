#Swap two values without a temporary variable.
a = 10
b = 20
a, b = b, a
print("a =", a)
print("b =", b)

#Convert 25 Celsius to Fahrenheit.
celsius = 25
fahrenheit = (celsius * 9/5) + 32
print("Fahrenheit:", fahrenheit)

#Convert kilometers to miles.
kilometers = 10
miles = kilometers * 0.621371
print("Miles:", miles)

#Calculate area using length and width.
length = 10
width = 5
area = length * width
print("Area:", area)

#Calculate circle area using pi = 3.14159.
pi = 3.14159
radius = 5
area = pi * radius * radius
print("Circle area:", area)

#Calculate simple interest.
principal = 10000
rate = 5
time = 2
interest = (principal * rate * time) / 100
print("Simple interest:", interest)

#Find the average of three values.
a = 10
b = 20
c = 30
average = (a + b + c) / 3
print("Average:", average)

#Convert 135 minutes to hours and minutes.
minutes = 135
hours = minutes // 60
remaining_minutes = minutes % 60
print("Hours:", hours)
print("Minutes:", remaining_minutes)

#Print the code point for A.
character = "A"
print(ord(character))

#Print the character for code point 66.
number = 66
print(chr(number))
