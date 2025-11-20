
# ============================================
# PROGRAM 1: Positive / Negative / Zero
# ============================================
Num= int(input("enter the number"))
if Num > 0:
    print("this is positive number")
elif Num == 0:
    print("this is zero")
else:
    print("this negative number")

# ============================================
# PROGRAM 2: Even or Odd
# ============================================
Number = int(input("enter the number"))
if Number % 2 == 0:
    print("here the number is even")
else:
    print("here the number is odd")

# ============================================
# PROGRAM 3: Leap Year
# ============================================
year = int(input("enter the year"))
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("this year is leap year")
else:
    print("this year is not leap year")

# ============================================
# PROGRAM 4: Greatest of Two Numbers
# ============================================
num1 = int(input("enter the number"))
num2 = int(input("enter the number"))
if num1 > num2:
    print("num1 is greater", num1)
else:
    print("num2 is greater", num2)

# ============================================
# PROGRAM 5: Voting Eligibility
# ============================================
Age = int(input("enter the age"))
if Age >= 18:
    print("you are eligible for vote")
else:
    print("you are not eligible for vote")

# ============================================
# PROGRAM 6: Vowel or Consonant
# ============================================
Alphabet = input("enter the alphabet")
if Alphabet in 'aeiou':
    print("it is vowel")
else:
    print("it is consonant")

# ============================================
# PROGRAM 7: Divisible by 5
# ============================================
number = int(input("enter the number"))
if number % 5 == 0:
    print("number is divisible by 5:", number)
else:
    print("number is not divisible by 5:", number)

# ============================================
# PROGRAM 8: Single-digit / Two-digit / More
# ============================================
Num = int(input("enter the number"))
if -9 <= Num <= 9:
    print("single digit")
elif 10 <= Num <= 99:
    print("two digit")
else:
    print("more than two digit")

# ============================================
# PROGRAM 9: Pass or Fail
# ============================================
marks = int(input("enter the marks"))
if marks >= 40 and marks <= 100:
    print("student is Pass")
else:
    print("student Fail")

# ============================================
# PROGRAM 10: Multiple of 3 and 7
# ============================================
number = int(input("enter the number"))
if number % 3 == 0 and number % 7 == 0:
    print("number is multiple of both 3 and 7.")
else:
    print("number is not multiple of both")

# ============================================
# PROGRAM 11: Greatest of Three (Nested If)
# ============================================
n1 = int(input("enter n1"))
n2 = int(input("enter n2"))
n3 = int(input("enter n3"))
if n1 > n2 and n1 > n3:
    print("bigger no is:", n1)
elif n2 > n1 and n2 > n3:
    print("bigger no is:", n2)
else:
    print("bigger no is:", n3)

# ============================================
# PROGRAM 12: Age Classification
# ============================================
age = int(input("enter the age"))
if age < 13:
    print("child")
elif 13 <= age <= 19:
    print("teenager")
elif 20 <= age <= 59:
    print("adult")
else:
    print("senior")

# ============================================
# PROGRAM 13: Grade Assignment
# ============================================
Marks = int(input("enter Marks"))
if 90 <= Marks <= 100:
    print("Grade A")
elif 75 <= Marks <= 89:
    print("Grade B")
elif 50 <= Marks <= 74:
    print("Grade C")
elif 35 <= Marks <= 49:
    print("Grade D")
else:
    print("Fail")

# ============================================
# PROGRAM 14: Triangle Type
# ============================================
side1 = int(input("side1"))
side2 = int(input("side2"))
side3 = int(input("side3"))
if (side1 + side2 > side3) and (side1 + side3 > side2) and (side2 + side3 > side1):
    if side1 == side2 == side3:
        print("equilateral")
    elif side1 == side2 or side2 == side3 or side1 == side3:
        print("isosceles")
    else:
        print("scalene")
else:
    print("not valid")

# ============================================
# PROGRAM 15: Uppercase / Lowercase / Digit / Special
# ============================================
char = input("enter character")
if 'A' <= char <= 'Z':
    print("Uppercase")
elif 'a' <= char <= 'z':
    print("Lowercase")
elif '0' <= char <= '9':
    print("Digit")
else:
    print("Special character")

# ============================================
# PROGRAM 16: Electricity Bill
# ============================================
unit = int(input("enter units"))
if unit <= 100:
    print(unit * 5)
elif unit <= 200:
    print(unit * 7)
else:
    print(unit * 10)

# ============================================
# PROGRAM 17: Largest of Four (Nested)
# ============================================
nu1 = int(input("n1"))
nu2 = int(input("n2"))
nu3 = int(input("n3"))
nu4 = int(input("n4"))
print(max(nu1, nu2, nu3, nu4))

# ============================================
# PROGRAM 18: Century + Leap Year
# ============================================
year = int(input("enter year"))
if year % 100 == 0:
    print("century year")
    if year % 400 == 0:
        print("leap year")
    else:
        print("not leap year")
else:
    print("not century year")

# ============================================
# PROGRAM 19: BMI Classification
# ============================================
weight = float(input("weight"))
height = float(input("height"))
bmi = weight / height**2
if bmi < 18.5:
    print("underweight")
elif 18.5 <= bmi <= 24.9:
    print("normal")
elif 25 <= bmi <= 29.9:
    print("overweight")
else:
    print("obese")

# ============================================
# PROGRAM 20: Smallest of Three
# ============================================
n1 = int(input("n1"))
n2 = int(input("n2"))
n3 = int(input("n3"))
print(min(n1, n2, n3))

# ============================================
# PROGRAM 21: Armstrong Numbers (100–999)
# ============================================
for num in range(100, 1000):
    s = sum(int(d)**3 for d in str(num))
    if s == num:
        print(num)

# ============================================
# PROGRAM 22: First n Primes
# ============================================
n = int(input("how many primes?"))
count = 0
num = 2
while count < n:
    prime = True
    for i in range(2, num):
        if num % i == 0:
            prime = False
            break
    if prime:
        print(num)
        count += 1
    num += 1

# ============================================
# PROGRAM 23: Divisible by 3 + Digit Sum <= 10
# ============================================
for num in range(1, 501):
    if num % 3 == 0:
        if sum(int(d) for d in str(num)) <= 10:
            print(num)

# ============================================
# PROGRAM 24: Pyramid of Stars
# ============================================
n = int(input("height"))
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))

# ============================================
# PROGRAM 25: Pangram Check
# ============================================
sen = input("sentence").lower()
alphabet = "abcdefghijklmnopqrstuvwxyz"
if all(ch in sen for ch in alphabet):
    print("pangram")
else:
    print("not pangram")

# ============================================
# PROGRAM 26: Twin Primes
# ============================================
for num in range(2, 100):
    prime1 = all(num % i for i in range(2, int(num**0.5)+1))
    prime2 = all((num+2) % i for i in range(2, int((num+2)**0.5)+1))
    if prime1 and prime2:
        print(num, num+2)

# ============================================
# PROGRAM 27: Harshad Number
# ============================================
num = int(input("enter number"))
s = sum(int(d) for d in str(num))
if num % s == 0:
    print("Harshad")
else:
    print("Not Harshad")

# ============================================
# PROGRAM 28: Pascal Triangle
# ============================================
n = int(input("rows"))
for i in range(n):
    val = 1
    print(" "*(n-i-1), end="")
    for j in range(i+1):
        print(val, end=" ")
        val = val * (i - j) // (j + 1)
    print()

# ============================================
# PROGRAM 29: Sum of Squares Series
# ============================================
n = int(input("n"))
print(sum(i*i for i in range(1, n+1)))

# ============================================
# PROGRAM 30: Reverse Number + Prime Check
# ============================================
def is_prime(n):
    if n <= 1: return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
num = int(input("number"))
rev = int(str(num)[::-1])
if is_prime(rev):
    print("prime")
else:
    print("not prime")

# ============================================
# PROGRAM 31: Repeated Sum of Digits > 100
# ============================================
total = 0
while total <= 100:
    num = int(input("enter"))
    total += sum(int(d) for d in str(num))
print("Exceeded 100")

# ============================================
# PROGRAM 32: Duck Number
# ============================================
num = input("enter")
if num[0] != '0' and '0' in num:
    print("duck number")
else:
    print("not duck")

# ============================================
# PROGRAM 33: Happy Number
# ============================================
def square_sum(n):
    return sum(int(d)**2 for d in str(n))
num = int(input("number"))
seen = set()
while num != 1 and num not in seen:
    seen.add(num)
    num = square_sum(num)
print("Happy number" if num == 1 else "Not happy")

# ============================================
# PROGRAM 34: Largest Prime Factor
# ============================================
num = int(input("enter"))
n = num
f = 2
while f * f <= n:
    if n % f == 0:
        n //= f
    else:
        f += 1
print("largest prime factor:", n)

# ============================================
# PROGRAM 35: Repeat until Palindrome
# ============================================
while True:
    s = input("string")
    if s == s[::-1]:
        print("palindrome")
        break
    print("not palindrome")

# ============================================
# PROGRAM 36: Digital Root
# ============================================
n = int(input("n"))
if n == 0:
    print(0)
else:
    print(9 if n % 9 == 0 else n % 9)

# ============================================
# PROGRAM 37: Collatz Sequence
# ============================================
n = int(input("n"))
while n != 1:
    print(n)
    n = n//2 if n % 2 == 0 else 3*n+1
print(1)

# ============================================
# PROGRAM 38: ATM Simulation
# ============================================
balance = int(input("enter balance"))
while True:
    print("1.Check 2.Deposit 3.Withdraw 4.Exit")
    c = input()
    if c == '1':
        print(balance)
    elif c == '2':
        amt = int(input("deposit"))
        balance += amt
    elif c == '3':
        amt = int(input("withdraw"))
        if amt > balance:
            print("no balance")
        else:
            balance -= amt
    elif c == '4':
        break
    else:
        print("invalid")

