"""
Name: Sachin Bagri
Enrollment: 0103CS231354
Batch: 6
Batch Time: 12:10 PM to 1:50 PM
"""

# 1. Write a program to check whether a number is positive, negative, or zero.
Num = int(input("enter the number"))
if Num > 0:
    print("this is positive number ")
elif Num == 0:
    print("this is zero")
else:
    print("this nagative number")

# 2. Write a program to check whether a number is even or odd.
Number = int(input("enter the number"))
if Number % 2 == 0:
    print("here the number is even")
else:
    print("here the number is odd")

# 3. Write a program to check if a given year is a leap year or not.
year = int(input("enter the year"))
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("this year is leap year")
else:
    print("this year is not leap year ")

# 4. Write a program to find the greatest of two numbers.
num1 = int(input("enter the numeber"))
num2 = int(input("enter the number"))
if num1 > num2:
    print("num1 is greater", num1)
else:
    print("num2 is greater", num2)

# 5. Write a program to check whether a person is eligible to vote (age >= 18).
Age = int(input("enter the age"))
if Age >= 18:
    print("you are eligible for vote")
else:
    print("you are not eligible for vote")

# 6. Write a program to check whether a given character is a vowel or consonant.
Alphabet = input("enter the alphabet")
if Alphabet in "aeiou":
    print("it is vowel")
else:
    print("it is cosonant")

# 7. Write a program to check if a number is divisible by 5.
number = int(input("enter the number"))
if number % 5 == 0:
    print("number is divisible by 5:", number)
else:
    print("number is not divisible by 5:", number)

# 8. Write a program to determine whether a given number is a single-digit,
#    two-digit, or more than two-digit number.
Num = int(input("enter the number "))
if Num >= -9 and Num <= 9:
    print("is single digit")
elif Num >= 10 and Num <= 99:
    print("is two digit")
else:
    print("more than two digit")

# 9. Write a program to check whether a student has passed or failed (passing marks = 40).
marks = int(input("enter the marks"))
if marks >= 40 and marks <= 100:
    print("student is Pass")
else:
    print("student Fail")

# 10. Write a program to find whether the entered number is a multiple of both 3 and 7.
number = int(input("enter the number"))
if number % 3 == 0 and number % 7 == 0:
    print("number is multiple of both 3 and 7.")
else:
    print("number is not multiple of both.")

# Ladder If & Nested If:

# 1. Write a program to find the greatest among three numbers.
n1 = int(input("enter the n1"))
n2 = int(input("enter the n2"))
n3 = int(input("enter the n3"))
if n1 > n2 and n1 > n3:
    print("bigger no is:", n1)
elif n2 > n3 and n2 > n3:
    print("bigger no is :", n2)
else:
    print("bigger no is: ", n3)

# 2. Write a program to classify a person based on age:
#    Child (<13), Teenager (13-19), Adult (20-59), Senior (60+).
age = int(input("enter the age"))
if age < 13:
    print("child")
elif age >= 13 and age <= 19:
    print("teenager ")
elif age >= 20 and age <= 59:
    print("adult")
else:
    print("senior")

# 3. Write a program to assign grades based on marks:
#    90-100: A, 75-89: B, 50-74: C, 35-49: D, <35: Fail.
Marks = int(input("enter the Marks"))
if Marks >= 90 and Marks <= 100:
    print("pass Grade:A")
elif Marks >= 75 and Marks <= 89:
    print("pass Grade:B")
elif Marks >= 50 and Marks <= 74:
    print("pass Grade:B")
elif Marks >= 35 and Marks <= 49:
    print("pass Grade:B")
else:
    print("Fail")

# 4. Write a program to check the type of triangle (equilateral, isosceles,
#    or scalene) based on sides.
side1 = int(input("enter the side1"))
side2 = int(input("enter the side2"))
side3 = int(input("enter the side3"))
if (side1 + side2 > side3) and (side1 + side3 > side2) and (side2 + side3 > side1):
    if side1 == side2 == side3:
        print("equilateral")
    elif side1 == side2 or side2 == side3 or side1 == side3:
        print("isosceles")
    else:
        print("scalene")
else:
    print("not valid")

# 5. Write a program to check if a character is uppercase, lowercase, digit, or special symbol.
char = input("enter the character")
if "A" <= char <= "Z":
    print("Uppercase letter")
elif "a" <= char <= "z":
    print("Lowercase letter")
elif "0" <= char <= "9":
    print("Digit")
else:
    print("Special character")

# 6. Write a program to calculate electricity bill based on units:
#    Up to 100 units: ₹5 per unit,
#    101–200 units: ₹7 per unit,
#    Above 200 units: ₹10 per unit.
unit = int(input("enter the unit"))
bill = 0
if unit <= 100:
    bill = unit * 5
    print(bill)
elif unit > 100 and unit <= 200:
    bill = unit * 8
    print(bill)
else:
    bill = unit * 10
    print(bill)

# 7. Write a program to determine the largest of four numbers using nested if.
nu1 = int(input("enter the n1"))
nu2 = int(input("enter the n2"))
nu3 = int(input("enter the n3"))
nu4 = int(input("enter the n4"))
if nu1 >= nu2 and nu2 > nu3 and nu3 > nu4:
    print("n1 is greater number")
elif nu2 >= nu1 and nu2 > nu3 and nu3 > nu4:
    print("n2 is greater number")
elif nu3 >= nu1 and nu3 > nu2 and nu3 > nu4:
    print("n3 is greater number")
else:
    print("n4 is greater number")

# 8. Write a program to check if a given year is a century year and also a leap year.
year = int(input("Enter a year "))
if year % 100 == 0:
    print("this is century year", year)
    if year % 400 == 0:
        print("this is also leap year", year)
    else:
        print("this is not a leap year", year)
else:
    print("this not a century year", year)

# 9. Write a program to classify BMI value:
#    Underweight (<18.5), Normal (18.5-24.9),
#    Overweight (25-29.9), Obese (30+).
weight = float(input("enter the weight"))
height = float(input("enter the height"))
bmi = weight / height ** 2
print("Your BMI is: {bmi:.2f}")
if bmi < 18.5:
    print("your are underweight")
elif 18.5 <= bmi <= 24.9:
    print("You are Normal.")
elif 25 <= bmi <= 29.9:
    print("You are Overweight.")
else:
    print("You are Obese.")

# 10. Write a program to display the smallest number among three using nested if.
n1 = int(input("enter the number "))
n2 = int(input("enter the number "))
n3 = int(input("enter the number "))
if n1 < n2 and n1 < n3:
    print("this is smaller number:", n1)
elif n2 < n1 and n2 < n3:
    print("this is smaller number is", n2)
else:
    print("this is smaller number ", n3)

# For Loop and While Loop problems are also included...
