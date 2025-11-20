# Name: Sachin Bagri
# Enrollment: 0103CS231354
# Batch: 6
# Batch Time: 12:10PM to 1:50PM

# 1. Write a program to check whether a number is positive, negative, or zero.
Num = int(input("enter the number: "))
if Num > 0:
    print("this is positive number")
elif Num == 0:
    print("this is zero")
else:
    print("this nagative number")

# 2. Write a program to check whether a number is even or odd.
Number = int(input("enter the number: "))
if Number % 2 == 0:
    print("here the number is even")
else:
    print("here the number is odd")

# 3. Write a program to check if a given year is a leap year or not.
year = int(input("enter the year: "))
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("this year is leap year")
else:
    print("this year is not leap year")

# 4. Write a program to find the greatest of two numbers.
num1 = int(input("enter the first number: "))
num2 = int(input("enter the second number: "))
if num1 > num2:
    print("num1 is greater", num1)
else:
    print("num2 is greater", num2)

# 5. Write a program to check whether a person is eligible to vote (age >= 18).
Age = int(input("enter the age: "))
if Age >= 18:
    print("you are eligible for vote")
else:
    print("you are not eligible for vote")

# 6. Write a program to check whether a given character is a vowel or consonant.
Alphabet = input("enter the alphabet: ")
if Alphabet in 'aeiou':
    print("it is vowel")
else:
    print("it is cosonant")

# 7. Write a program to check if a number is divisible by 5.
number = int(input("enter the number: "))
if number % 5 == 0:
    print("number is divisible by 5:", number)
else:
    print("number is not divisible by 5:", number)

# 8. Write a program to determine whether a given number is a single-digit, two-digit, or more than two-digit number.
Num = int(input("enter the number: "))
if Num >= -9 and Num <= 9:
    print("is single digit")
elif Num >= 10 and Num <= 99:
    print("is two digit")
else:
    print("more than two digit")

# 9. Write a program to check whether a student has passed or failed (passing marks = 40).
marks = int(input("enter the marks: "))
if marks >= 40 and marks <= 100:
    print("student is Pass")
else:
    print("student Fail")

# 10. Write a program to find whether the entered number is a multiple of both 3 and 7.
number = int(input("enter the number: "))
if number % 3 == 0 and number % 7 == 0:
    print("number is multiple of both 3 and 7.")
else:
    print("number is not multiple of both.")

# Ladder If & Nested If:
# 1. Write a program to find the greatest among three numbers.
n1 = int(input("enter the first number: "))
n2 = int(input("enter the second number: "))
n3 = int(input("enter the third number: "))
if n1 > n2 and n1 > n3:
    print("bigger no is:", n1)
elif n2 > n3 and n2 > n3:
    print("bigger no is :", n2)
else:
    print("bigger no is: ", n3)

# 2. Write a program to classify a person based on age: Child (<13), Teenager (13-19), Adult (20-59), Senior (60+).
age = int(input("enter the age: "))
if age < 13:
    print("child")
elif age >= 13 and age <= 19:
    print("teenager")
elif age >= 20 and age <= 59:
    print("adult")
else:
    print("senior")

# 3. Write a program to assign grades based on marks: 90-100: A, 75-89: B, 50-74: C, 35-49: D, <35: Fail.
Marks = int(input("enter the Marks: "))
if Marks >= 90 and Marks <= 100:
    print("pass Grade:A")
elif Marks >= 75 and Marks <= 89:
    print("pass Grade:B")
elif Marks >= 50 and Marks <= 74:
    print("pass Grade:C")
elif Marks >= 35 and Marks <= 49:
    print("pass Grade:D")
else:
    print("Fail")

# 4. Write a program to check the type of triangle (equilateral, isosceles, or scalene) based on sides.
side1 = int(input("enter the side1: "))
side2 = int(input("enter the side2: "))
side3 = int(input("enter the side3: "))
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
char = input("enter the character: ")
if 'A' <= char <= 'Z':
    print("Uppercase letter")
elif 'a' <= char <= 'z':
    print("Lowercase letter")
elif '0' <= char <= '9':
    print("Digit")
else:
    print("Special character")

# 6. Write a program to calculate electricity bill based on units:
unit = int(input("enter the unit: "))
bill = 0
if unit <= 100:
    bill = (unit * 5)
    print(bill)
elif unit > 100 and unit <= 200:
    bill = (unit * 8)
    print(bill)
else:
    bill = unit * 10
    print(bill)

# 7. Write a program to determine the largest of four numbers using nested if.
nu1 = int(input("enter the n1: "))
nu2 = int(input("enter the n2: "))
nu3 = int(input("enter the n3: "))
nu4 = int(input("enter the n4: "))
if nu1 >= nu2 and nu2 > nu3 and nu3 > nu4:
    print("n1 is greater number")
elif nu2 >= nu1 and nu2 > nu3 and nu3 > nu4:
    print("n2 is greater number")
elif nu3 >= nu1 and nu3 > nu2 and nu3 > nu4:
    print("n3 is greater number")
else:
    print("n4 is greater number")

# 8. Write a program to check if a given year is a century year and also a leap year.
year = int(input("Enter a year: "))
if year % 100 == 0:
    print("this is century year", year)
    if (year % 400 == 0):
        print("this is also leap year", year)
    else:
        print("this is not a leap year", year)
else:
    print("this not a century year", year)

# 9. Write a program to classify BMI value: Underweight (<18.5), Normal (18.5-24.9), Overweight (25-29.9), Obese (30+).
weight = float(input("enter the weight: "))
height = float(input("enter the height: "))
bmi = weight / height**2
print(f"Your BMI is: {bmi:.2f}")
if bmi < 18.5:
    print("your are underweight")
elif 18.5 <= bmi <= 24.9:
    print("You are Normal.")
elif 25 <= bmi <= 29.9:
    print("You are Overweight.")
else:
    print("You are Obese.")

# 10. Write a program to display the smallest number among three using nested if.
n1 = int(input("enter the number: "))
n2 = int(input("enter the number: "))
n3 = int(input("enter the number: "))
if n1 < n2 and n1 < n3:
    print("this is smaller number:", n1)
elif n2 < n1 and n2 < n3:
    print("this is smaller number is", n2)
else:
    print("this is smaller number ", n3)

# For Loop Problems

# 1. Write a program using a for loop to print all Armstrong numbers between 100 and 999.
print("Armstrong numbers between 100 and 999:")
for num in range(100, 1000):
    hundreds = num // 100
    tens = (num // 10) % 10
    ones = num % 10
    sum_of_digitcubes = hundreds ** 3 + tens ** 3 + ones ** 3
    if num == sum_of_digitcubes:
        print(num)

# 2. Write a program to generate and display the first n prime numbers using a for loop.
n = int(input("Enter prime numbers you want: "))
print("The first prime numbers are:", n)
count = 0
num = 2
for _ in range(10000):
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=' ')
        count += 1
    if count == n:
        break
    num += 1

# 3. Write a program to display all numbers from 1 to 500 that are divisible by 3, but the sum of their digits should not exceed 10.
for num in range(1, 501):
    if num % 3 == 0:
        sumofdigit = 0
        temp = num
        while temp > 0:
            sumofdigit += temp % 10
            temp //= 10
        if sumofdigit <= 10:
            print(num)

# 4. Write a program using a for loop to print a pyramid of stars (*) of height n.
n = int(input("Enter height of pyramid: "))
for i in range(1, n + 1):
    spaces = n - i
    stars = 2 * i - 1
    print(' ' * spaces + '*' * stars)

# 5. Write a program to accept a string and check whether it is a pangram (contains all 26 alphabets at least once) using a for loop.
sentences = input("Enter a sentence: ").lower()
alphabet = "abcdefghijklmnopqrstuvwxyz"
is_pangram = True
for letter in alphabet:
    if letter not in sentences:
        is_pangram = False
        break
if is_pangram:
    print("the sentence is a pangram")
else:
    print("the sentence is not a pangram")

# 6. Write a program using a for loop to print all twin primes between 1 and 100.
for num in range(2, 100):
    num_isprime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            num_isprime = False
            break
    if num_isprime:
        next_num = num + 2
        next_isprime = True
        for j in range(2, int(next_num**0.5) + 1):
            if next_num % j == 0:
                next_isprime = False
                break
        if next_isprime and next_num <= 100:
            print((num, next_num))

# 7. Write a program that accepts a number from the user and prints whether it is a Harshad number (number divisible by the sum of its digits) using a for loop.
num = int(input("Enter a number: "))
sum_digits = 0
temp = num
for digit in str(num):
    sum_digits += int(digit)
if sum_digits != 0 and temp % sum_digits == 0:
    print(f"{temp} is a Harshad number.")
else:
    print(f"{temp} is NOT a Harshad number.")

# 8. Write a program to generate Pascal’s Triangle up to n rows using a for loop.
n = 3
for i in range(n):
    print(' ' * (n - i - 1), end='')
    value = 1
    for j in range(i + 1):
        print(value, end=' ')
        value = value * (i - j) // (j + 1)
    print()

# 9. Write a program using a for loop to display the sum of the series: 1^2 + 2^2 + ... + n^2
n = int(input("Enter the number: "))
total_sum = 0
for i in range(1, n + 1):
    total_sum += i * i
print("sum of the series is 1^2 + 2^2 + ... +", n, "^2 is:", total_sum)

# While Loop Problems

# 1. Write a program using a while loop to find the reverse of a number and check if the reversed number is prime.
def is_prime(n):
    if n <= 1:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True
num = int(input("Enter a number: "))
revrse = 0
temp = num
while temp > 0:
    digit = temp % 10
    revrse = revrse * 10 + digit
    temp //= 10
print("Original Number", num)
print("Reversed Number", revrse)
if is_prime(revrse):
    print("It is a prime number:", revrse)
else:
    print("It is not a prime number:", revrse)

# 2. Write a program that continues to accept numbers from the user until the sum of digits of all numbers entered becomes greater than 100.
total_sum = 0
while total_sum <= 100:
    num = int(input("Enter a number: "))
    digit_sum = 0
    temp = num
    while temp > 0:
        digit_sum += temp % 10
        temp //= 10
    total_sum += digit_sum
    print("sum of digit", total_sum)
print("Sum of digits exceeded 100")

# 3. Write a program using a while loop to check whether a number is a Duck number (a number containing zero but not starting with zero).
num = int(input("Enter a number: "))
if num == 0:
    print("it is Not a Duck number (number is zero).")
else:
    temp = num
    found_zero = False
    while temp > 0:
        digit = temp % 10
        if digit == 0:
            found_zero = True
        temp //= 10
    if found_zero:
        print("it is a duck number ", num)
    else:
        print("it is not a duck number", num)

# 4. Write a program using a while loop to accept a number and check if it is a Happy number.
num = int(input("Enter a number: "))
count = 0
max_iterations = 100
while num != 1 and count < max_iterations:
    sum_square = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum_square += digit * digit
        temp //= 10
    num = sum_square
    count += 1
if num == 1:
    print("It is a Happy number.")
else:
    print("It is NOT a Happy number.")

# 5. Write a program using a while loop to find the largest prime factor of a given number.
num = int(input("Enter a number: "))
n = num
largest_factor = 1
factor = 2
while n > 1:
    if n % factor == 0:
        largest_factor = factor
        n //= factor
    else:
        factor += 1
print("largest prime factor is", largest_factor)

# 6. Write a program to repeatedly accept a string from the user until the string entered is a palindrome.
while True:
    s = input("Enter a string: ")
    if s == s[::-1]:
        print("it is palindrone", s)
        break
    else:
        print("it is not a palindrone", s)

# 7. Write a program using a while loop to compute the sum of digits of a number until the result becomes a single-digit number (Digital root).
n = int(input("Enter a number: "))
if n == 0:
    digital_root = 0
else:
    digital_root = 9
    if n % 9 == 0:
        digital_root = 9
    else:
        digital_root = n % 9
print("Digital root is:", digital_root)

# 8. Write a program using a while loop to generate the Collatz sequence for a given number.
n = 10
print("Collatz sequence:")
while n != 1:
    print(n)
    if n % 2 == 0:
        n = n // 2
    else:
        n = 3 * n + 1
print(1)

# 9. Write a program to simulate an ATM machine using a while loop.
balance = int(input("enter the balance: "))
while True:
    print("\n1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    choice = input("Choose (1-4): ")
    if choice == '1':
        print("Balance is", balance)
    elif choice == '2':
        amount = int(input("Deposit amount: "))
        balance += amount
        print("Deposited money", amount)
    elif choice == '3':
        amount = int(input("Withdraw amount: "))
        if amount > balance:
            print("not sufficient balance")
        else:
            balance -= amount
            print("Withdrawn an ammount", amount)
    elif choice == '4':
        print("exit")
        break
    else:
        print("invalid choice")
