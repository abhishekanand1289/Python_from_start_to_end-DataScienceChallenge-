# -*- coding: utf-8 -*-
"""Copy of session11-task.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/135uliFHdx9N9TcdXUpPS-AX1-fn4QcVs

## Exception Handling

###`Q-1`: You are given a function definition. There might be several issues on execution of this function. You are asked to do exception handling for diffrent errors that this function goes in to `without altering this function`. And print error text.

Function parameters `l -> list, s -> could be anything`

```
def function(l: list, s, **args):
    last_element = l[-1]
    
    l[int(s)]=10
    any_element = l[int(s)+10]
    l[s]=10
    
    res = sum(l)
    
    p = args['p']
    # print(p)
    return res/last_element * p + any_element

```
Check for different function calls:-

```
function([1,2,1], 12)
function([1,2,1]*9, '1-2')
function([1,'2',1]*9, 12)
function([1,'2',1]*9, 12)
function([1,2,0]*9, 12  )
function([1,2,1]*9, 12, p=None)
function([1,2,0]*9, 12, p=10)
```
"""

def function(l: list, s, **args):
    last_element = l[-1]

    l[int(s)]=10
    any_element = l[int(s)+10]
    l[s]=10

    res = sum(l)

    p = args['p']
    return res/last_element * p + any_element

try:
  output = function([1,2,3]*9, 12, p=10)
except IndexError as v:
  print(type(v))
  print(v)
except ValueError as v:
  print(type(v))
  print(v)
except TypeError as v:
  print(type(v))
  print(v)
except KeyError as v:
  print(type(v))
  print(v)
except ZeroDivisionError as v:
  print(type(v))
  print(v)
else:
  print(output)
finally:
  print("Dhani vadalu bro")

"""###`Q-2:` You are given a code snippet. There might be several issues on execution of this code. You are asked to do exception handling for diffrent errors, condition is what ever happens we need to execute last line printing correct result of `sum of elements`.

List have elemnts as any no of  `key-pair dict with key as list index and value as any integer`, `integers` and `numeric-strings`. There is always only one element in the dict.


```
l = [{0:2},2,3,4,'5', {5:10}]
# For calculating sum of above list
s=0
for i in range(len(l)):
    #You can Edit code from here
    s += l[i].get(i)
    s += l[i]
    s += int(l[i])


print(s)
```
"""

l = [{0:2},2,3,4,'5', {5:10}]
s=0
for i in range(len(l)):
  try:
    s += l[i]
  except TypeError:
    try:
      s += l[i].get(i)
    except AttributeError:
      s += int(l[i])
print(s)

"""### `Q-3:`: File Handling with Exception handling

Write a program that opens a text file and write data to it as "Hello, Good Morning!!!". Handle exceptions that can be generated during the I/O operations. Do not show the success message on the main exception handling block (write inside the else block).
"""

try:
  with open("text_file.txt",'w') as f:
    f.write("Hello, Good Morning!!!")
except IOError:
  print("Error loading/writing file")
else:
  print("Succesfull")

"""### `Q-4`: Number game program.

Write a number game program. Ask the user to enter a number. If the number is greater than number to be guessed, raise a **ValueTooLarge** exception. If the value is smaller the number to be guessed the, raise a **ValueTooSmall** exception and prompt the user to enter again. Quit the program only when the user enters the correct number. Also raise **GuessError** if user guess a number less than 1.
"""

import random

class ValueTooLarge(Exception):
  def display(self):
    print("ValueTooLarge")
class ValueTooSmall(Exception):
  def display(self):
    print("ValueTooSmall")
class GuessError(Exception):
  def display(self):
    print("Guess must be only between 1 and 100")

n = random.randint(1,100)

while True:
  try:
    user_guess = int(input("What's your guess? "))
    if user_guess == n:
      print("Great! you won")
      break
    elif user_guess < 1 or user_guess > 100:
      raise GuessError
    elif user_guess > n:
      raise ValueTooLarge
    elif user_guess < n:
      raise ValueTooSmall
    elif user_guess < 1:
      raise GuessError
  except ValueTooLarge as v:
    v.display()
  except ValueTooSmall as s:
    s.display()
  except GuessError as g:
    g.display()

"""### `Q-5:` Cast vote

Write a program that validate name and age as entered by the user to determine whether the person can cast vote or not. To handle the age, create **InvalidAge** exception and for name, create **InvalidName** exception. The name will be invalid when the string will be empty or name has only one word.

Example 1:

Input:

```bash
Enter the name:               goransh singh
Enter the age: 25
```

Output:

```bash
Goransh Singh  Congratulation !!! You can vote.
```
"""

class InvalidAge(Exception):
  def display(self):
    print("           ")
    print("You must be 18years old to vote")
class InvalidName(Exception):
  def display(self):
    print("                                                              ")
    print("Invalid Name :- Please Enter your FullName(Firstname Lastname)")

class Vote():
  def __init__(self):
    self.__name = input("Please Enter your Full name: ")
    self.__age = int(input("Please enter your age: "))

  def Validation(self):
    name = self.__name.split(" ")
    try:
      if len(name) < 2:
        raise InvalidName
      elif self.__age < 18:
        raise InvalidAge
    except InvalidName as i:
      i.display()
    except InvalidAge as a:
      a.display()
    else:
      print(f"{self.__name} Congratulations!!! You are eligible to vote")

v = Vote()
v.Validation()

"""### `Q-6`: Write a python function which infinitely prints natural numbers in a single line. Raise the **StopIteration** exception after displaying first 20 numnbers to exit from the program."""

class StopIteration(Exception):
  def display(self):
    print("\nMaximum limit to print Natural numbers is 20")
def display(i):
  count = 0
  while True:
    try:
      i += 1
      count += 1
      if count == 21:
        raise StopIteration
    except StopIteration as s:
      s.display()
      break
    else:
      print(i, end=" ")

display(1000)

