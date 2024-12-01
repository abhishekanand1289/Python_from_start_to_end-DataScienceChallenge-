# -*- coding: utf-8 -*-
"""Copy of session-7-task.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Ia7arH2eruySsVTHjhHREwl9EAu_jRtZ

##`Q-1:` Rectangle Class
1. Write a Rectangle class in Python language, allowing you to build a rectangle with length and width attributes.

2. Create a Perimeter() method to calculate the perimeter of the rectangle and a Area() method to calculate the area of ​​the rectangle.

3. Create a method display() that display the length, width, perimeter and area of an object created using an instantiation on rectangle class.

Eg.
After making above classes and methods, on executing below code:-
```
my_rectangle = Rectangle(3 , 4)
my_rectangle.display()
```

`Output:`
```
The length of rectangle is:  3
The width of rectangle is:  4
The perimeter of rectangle is:  14
The area of rectangle is:  12
```
"""

class Rectangle():
  def __init__(self,l,b):
    self.length = l
    self.width = b

  def perimeter(self):
    return 2*(self.length + self.width)

  def area(self):
    return self.length * self.width

  def display(self):
    print(f"""
    The length of rectangle is: {self.length}
    The width of rectangle is:  {self.width}
    The perimeter of rectangle is: {self.perimeter()}
    The area of rectangle is: {self.area()}""")

rect = Rectangle(20,40)
rect.display()

"""##`Q-2: Bank Class`

1. Create a Python class called `BankAccount` which represents a bank account, having as attributes: `accountNumber` (numeric type), `name` (name of the account owner as string type), `balance`.
2. Create a constructor with parameters: `accountNumber, name, balance`.
3. Create a `Deposit()` method which manages the deposit actions.
4. Create a `Withdrawal()` method  which manages withdrawals actions.
5. Create an `bankFees()` method to apply the bank fees with a percentage of 5% of the balance account.
6. Create a `display()` method to display account details.
Give the complete code for the  BankAccount class.

Eg.
After making above classes and methods, on executing below code:-
```
newAccount = BankAccount(2178514584, "Mandy" , 2800)

newAccount.Withdrawal(700)

newAccount.Deposit(1000)

newAccount.display()
```

`Output:`
```
Account Number :  2178514584
Account Name :  Mandy
Account Balance :  3100 ₹
```
"""

class BankAccount():

  def __init__(self,a,n,b):
    self.account_num = a
    self.name = n
    self.balance = b

  def deposit(self, amount):
    self.dep_amount = amount
    self.balance += self.dep_amount
    return self.balance

  def withdrawl(self, cash):
    self.withdrawl_amt = cash
    if cash > self.balance:
      print("Insufficient Balance")
    else:
      self.balance = (self.balance-(0.05*self.balance))-self.withdrawl_amt
    return self.balance

  def display(self):
    print(f"""
    Account Number :  {self.account_num}
    Account Name :  {self.name}
    Account Balance : {self.balance}
    """)

bank = BankAccount(2178514584, "Mandy" , 100)
bank.deposit(10)
bank.withdrawl(100)
bank.display()

"""##`Q-3:Computation class`

1. Create a `Computation` class with a default constructor (without parameters) allowing to perform various calculations on integers numbers.
2. Create a method called `Factorial()` which allows to calculate the factorial of an integer n. Integer n as parameter for this method

3. Create a method called `naturalSum()` allowing to calculate the sum of the first n integers 1 + 2 + 3 + .. + n. Integer n as parameter for this method.

4. Create a method called `testPrime()` in  the Calculation class to test the primality of a given integer n, n is Prime or Not? Integer n as parameter for this method.

5. Create  a method called `testPrims()` allowing to test if two numbers are prime between them. Two integers are prime to one another if they have only `1` as their common divisor. Eg. 4 and 9 are prime to each other.

5. Create a `tableMult()` method which creates and displays the multiplication table of a given integer. Then create an `allTablesMult()` method to display all the integer multiplication tables 1, 2, 3, ..., 9.

6. Create a static `listDiv()` method that gets all the divisors of a given integer on new list called  Ldiv. Create another `listDivPrim()` method that gets all the prime divisors of a given integer.
"""

class Computation():

  def __init__(self):
    return

#Factorial of n
  def Factorial(self,n):
    fact = 1
    for i in range(1,n+1):
      fact = fact*i
    return fact

#Sum of n natural numbers
  def naturalsum(self,n):
    sum = 0
    for i in range(1,n+1):
      sum +=i
    return sum

#Test whether the integer is Prime
  def testprime(self,n):
    j = 0
    for i in range(1,n+1):
      if (n%i == 0):
        j+=1
    if j==2:
      return True
    else:
      return False

#Testing if two integers are prime to each other
  def testPrims(self,n1,n2):
    l1 = []
    l2 = []
    for i in range(1,n1+1):
      if n1%i==0:
        l1.append(i)

    for j in range(1,n2+1):
      if n2%j==0:
        l2.append(j)
    gcd_lst = []
    for i in range(len(l1)):
      for j in range(len(l2)):
        if l1[i] == l2[j]:
          gcd_lst.append(l1[i])
    gcd = max(gcd_lst)
    if gcd == 1:
      print(f"{n1} and {n2} are prime to each other")
    else:
      print(f"No they are not prims")

#Multiplication table of an Integer
  def tableMult(self,n):
    table = []
    for i in range(1,11):
      mul = n*i
      table.append(mul)
      print(f"{n} * {i} = {table[i-1]}")

#Multiplication table of an Integer
  def allTablesMult(self):
    for i in range(1,10):
      for j in range(1,11):
        a = i*j
        print(f"{i} * {j} =",a)
      print("              ")

#Divisors of a given integer
  def listDiv(self,n):
    l = []
    for i in range(1,n):
      if n%i==0:
        l.append(i)
    print(l)

#Prime Divisors list of a given integer
  def listDivPrim(self,n):
    pridiv_list = []
    for i in range(1,n):
      if (n%i==0 and self.testprime(i)):
        pridiv_list.append(i)
    return pridiv_list

c = Computation()
c.listDivPrim(60)

"""##`Q-4`: Build flashcard using class in Python.

Build a flashcard using class in python. A flashcard is a card having information on both sides, which can be used as an aid in memoization. Flashcards usually have a question on one side and an answer on the other.

**Example 1:**

Approach:

- Create a class named FlashCard.
- Initialize dictionary fruits using __init__() method. Here you have to define fruit name as key and it's color as value. E.g., {"Banana": "yellow", "Strawberries": "pink"}
- Now randomly choose a pair from fruits by using _random_ module and store the key in variable _fruit_ and _value_ in variable color.
- Now prompt the user to answer the color of the randomly chosen fruit.
- If correct print correct else print wrong.

Output:
```bash
welcome to fruit quiz
What is the color of Strawberries
pink
Correct answer
Enter 0, if you want to play again: 0
What is the color of watermelon
green
Correct answer
Enter 0, if you want to play again: 1
```
"""

import random
class FlashCard():

  def __init__(self):
    self.fruits = {
    "apple" : "red",
    "banana" : "yellow",
    "guava" : "green",
    "orange": "orange"
    }

  def quiz(self):
    print("Welcome to quiz!!!")
    while True:
      (fruits,colour)=random.choices(list(self.fruits.items()))[0]

      print(f"what is the colour of {fruits}?")

      user_input = input()

      if user_input == colour:
        print("Perfect! That's right")
      else:
        print("Sorry! It's a wrong answer. Please try again :-|")

      exit_option = int(input("Please enter '1' to exit or '0' to play again"))

      if exit_option==1:
        break

fc = FlashCard()
fc.quiz()

"""## `Q-5:` Problem 5 based on OOP Python.

TechWorld, a technology training center, wants to allocate courses for instructors. An instructor is identified by name, technology skills, experience and average feedback. An instructor is allocated a course, if he/she satisfies the below two conditions:
- eligibility criteria:
    - if experience is more than 3 years, average feedback should be 4.5 or more
    - if experience is 3 years or less, average feedback should be 4 or more
- he/she should posses the technology skill for the course

Identify the class name and attributes to represent instructors. Write a Python program to implement the class chosen with its attributes and methods.

**Note:**
- Consider all instance variables to be private and methods to be public.
- An instructor may have multiple technology skills, so consider instance variable, technology_skill to be a list.
- *check_eligibility()*: Return true if eligibility criteria is satisfied by the instructor. Else, return false
- *allocate_course(technology)*: Return true if the course which requires the given technology can be allocated to the instructor. Else, return false.

Represent a few objects of the class, initialize instance variables using setter methods, invoke
appropriate methods and test your program.
"""

class Course_tech():
  def __init__(self, name, skills_in_technology, experience, average_feedback):
    self.name = name
    self.technology_skills = skills_in_technology
    self.experience = experience
    self.average_feedback = average_feedback

  def check_eligibility(self):
    if self.experience > 3 and self.average_feedback >=4.5:
      return True
    elif self.experience <= 3 and self.average_feedback >=4.5:
      return True
    else:
      return False

  def allocate_course(self, technology):
    is_eligible = self.check_eligibility()
    if is_eligible == True:
      if technology in self.technology_skills:
        return "Allocate the course"
      else:
        return "Can't take the course"
    else:
      return "He/she not doesn't meet the requirements. Better luck next time :-|"

ct = Course_tech("Ramya", ["SQL", "Python", "ML"], 4, 4.5 )
ct.allocate_course("SQL")

