#Ask the user for their name and greet them.
name = input("Enter your name:")
print("Hello", name, "! Welcome to Hyderabad.")

#Read two integers and add them.
a = int(input("Enter first number: "))
b = int(input("Enter second number:"))
total = a + b
print("Sum:", total)

#Check whether an integer is even or odd.
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")

#Classify a number Positive, negative, or zero.
num = int(input("Enter a number: "))
if num > 0:
    print("Positive number")
elif num < 0:
    print("Negative number")
else:
    print("Zero")

#Find the larger of two values.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
if a > b:
    print("Larger number:", a)
elif b > a:
    print("Larger number:", b)
else:
    print("Both numbers are equal")

#Find the largest of three values
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
if a >= b and a >= c:
    print("Largest number:", a)
elif b >= a and b >= c:
    print("Largest number:", b)
else:
    print("Largest number:", c)

#Find the smallest of three values
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
if a <= b and a <= c:
    print("Smallest number:", a)
elif b <= a and b <= c:
    print("Smallest number:", b)
else:
    print("Smallest number:", c)

#Check whether a year is a leap year.
year = int(input("Enter a year: "))
if year % 400 == 0:
    print("Leap year")
elif year % 100 == 0:
    print("Not a leap year")
elif year % 4 == 0:
    print("Leap year")
else:
    print("Not a leap year")

#Check divisibility by both 5 and 11.
num = int(input("Enter a number: "))
if num % 5 == 0 and num % 11 == 0:
    print("Divisible by both 5 and 11")
else:
    print("Not divisible by both 5 and 11")

#Pass if score is at least 40.
score = int(input("Enter your score: "))
if score >= 40:
    print("Pass")
else:
    print("Fail")
    
