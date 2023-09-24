'''
Objective Questions
Fill in the Blanks:
1. 
(a) The smallest individual unit in a program is known as a "token".
(b) A word having special meaning reserved by a programming language is known as a "keyword".
(c) A "literal" is a sequence of characters surrounded by quotes.
(d) "Operators" are tokens that trigger same computation/action when applied to variables.
(e) A "variable" is a reserved named location that stores values.
(f) To determine the type of an object we use the "type()" function.
(g) The input() always returns 2 value of "strings" function.
(h) Blocks of codes are represented through "indentation".
(i) In "duck typing", the variable can hold values of different types at different times.
(j) In Python, the floating-point numbers have precision of "15" digits.
(k) Operators that act upon two operands are referred to as "binary" operators.
(l)"Floor division" truncates fractional remainders and gives only the whole part as the result.
(m)"Syntax" error does not stop execution but the program behaves incorrectly and produces undesired/wrong output.
(n)Trying to access a variable or file that doesn't exist is a kind of "NameError".


2. 
a) True
b) False
c) False
d) False
e) False
f) True
g) True
h) True
i) False
j) True
k) True
l) True


3. 
a) i
b) iv
c) iii
d) i
e) ii
f) i
g) iv
h) iv
i) i
j) iii
k) iv
l) iv
m) iii
n) iii

Unsolved:

5. 5.1: Variable names cannot start with a number.
93: Variable names cannot consist solely of numbers.
for: "for" is a reserved keyword in Python and cannot be used as a variable name.


6.
i) 8 5
ii) 0 2
iii) 15 250
iv) 66.66666666666667 126.66666666666667
v) 4 -10 7
vi) 8 8 0

9. 
Operators are special symbols or reserved words that are used to perform operations on values or variables. Unary operators are operators that work on a single operand, such as the negative sign (-5). Binary operators work on two operands, such as addition (+) or multiplication (*).

Examples of Unary operators:

Negation (-)
Identity (+)
Logical not (not)
Examples of Binary operators:

Addition (+)
Subtraction (-)
Multiplication (*)
Division (/)

10.
An expression is a combination of variables, values, and operators that can be evaluated to produce a value. A statement is a complete line of code that performs a specific task, such as assigning a value to a variable or printing a message to the console.

11. A Python program can contain the following components:

Modules
Statements
Expressions
Functions
Classes
Variables
Comments

12. A variable is a named location in memory used to store data. Variables are important for a program because they allow us to assign values to names and reuse them throughout the code. This makes the code more readable, easier to maintain, and less error-prone.

13. Dynamic Typing is a feature of Python that allows variables to hold values of any data type, without the need to specify the type of the variable beforehand. This means that you can assign an integer to a variable, and later assign a string to the same variable without any issues.

18. The code assigns the value 70 to both variables a and b.

19. The code is trying to assign a single value to two variables which is not possible.

20.
i) the "p" in print is capital which is wrong.
ii) b is not defined here and the "and" function has a capital A which is wrong.
iii) In the last line, semicolons should be commas
v) the variable should be on the left side of the assignment operator
iv) capital x is not defined.

21.
i) 13 22
ii) 2 3 6
iii) 7 49

22. Comments in Python are used to add notes or explanations to the code that are ignored by the interpreter when executing the program.

23.
i)
ii) Adding string and integer is not possible
iii) A is assigned a string value after being assigned an integer value which is not valid.

24. The output will be: 20 41
25. The output will be: 60 20 60
26. The output will be: 12 6.5 24
27. The output will be: a and b, : 5 13 16
28. you can not convert strng to integer
29. The input cl is a string, so we cannot subtract 1 from it.


'''



#Question 1: Display name
print("My name is Abhinav")
print()
#Question 2
print("DPSDUBAI","Grade 11","A",sep = "-")

print()

#Question 7


#Question 8 a)
print(8%3 + 8*3)
#b)
print((8+43)**1/2)
#c)
print((8)88**1/2 + (43)**1/2)
#d)
print(100//32)


print()
print()
print()

#Question 14
def calculate_area(base, height):
    area = 0.5 * base * height
    print(area)

print()

#Question 15
def calculate_area(length, width, shape_type):
    if shape_type == "rectangle":
        area = length * width
        return area
    elif shape_type == "triangle":
        area = (length * width) / 2
        return area
    else:
        return "Invalid shape type entered."

#Question 16
def print_pattern(num):
    for i in range(1, num+1):
        print("•" * i)

#Question 17
def convert_to_rupees(dollars):
    rupees = dollars * 84
#Example:
'''
print(convert_to_rupees(10))'''
    
#Question 30: Finding area of circle
r = eval(input("Type the radius: "))
print("The area of the circle is ",22/7 * r * r)

print()
print()
#Question 31: Finding average marks
num1 = eval(input("Type first number: "))
num2 = eval(input("Type second number: "))
num3 = eval(input("Type third number: "))
num4 = eval(input("Type fourth number: "))
num5 = eval(input("Type fifth number: "))
avg = (num1 + num2 + num3 + num4 + num5)/5
print(avg)

print()
print()
#Question 32: Finding area of traingle
b = eval(input("Type base: "))
h = eval(input("Type height: "))
print("Area of triangle is ",1/2 * b * h)

#Question 33
num = int(input("Enter a number: "))
for i in range(1, 6):
    print(num*i)


#Question 34
name = input("Enter name: ")
class_name = input("Enter class: ")
age = input("Enter age: ")
print("Name is",name,",class is",class_name,"and age is",age)
print("Name:", name)
print("Class:", class_name)
print("Age:", age)


#Question 35
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

a = a + b
b = a - b
a = a - b
b = b + c
c = b - c
b = b - c

print("After swapping: a =", a, "b =", b, "c =", c)


print()
print()

