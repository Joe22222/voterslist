'''
Objective:
1.
a) Statements
b) Flowcharts
c) for loop and while loop
d) for loop
e) break
f) infinite
g) while loop
h) inner loop
i) continue
j) header

2. 
(a) False
(b) False
(c) True
(d) True
(e) True
(f) True
(g) False
(h) False
(i) True
(j) True
(k) True

3.
a) flowchart
b) for statement
c) colon
d) if
e) 101
f) do-while
g) infinite
h) for
i) i)
j) iii)
k) continue
l) pass
m) indentation
'''
'''
Unsolved:
1.A compound statement represents a group of statements executed as a unit.
2. Statement that unconditionally transfers program control within a function .
3. A loop may contain another loop in its body.
Example: for i in range (1, 6):
    for j in range (1, i):
        print ("*", end = ' ')
    print ()

4. The update expressions change the value of loop variable. The update expression is given as a statement inside the body of while loop.
5. (i) Mark >= 100 and Mark < 70
(ii) Num > 0 and Num < 5 and Num != 2
(iii) Answer == 'N' or Answer == 'n'
(iv) Age >= 18 and gender == 'male'
(v) City == 'Kolkata' or City == 'Mumbai'

6. code = input ("Enter season code: ")
if code == 'w':
    print ("winter season")
elif code == 'r':
    print ("rainy season")
else:
    print ('summer season')


7. (i)
guru99 1
guru99 2
guru99 3

(ii)
100
200
300

(iii)
20
16


(iv)
1   1
2   1
2   2
3   1
3   2
3   3
4   1
4   2
4   3
4   4
5   1
5   2
5   3
5   4
5   5

(v)
10
11
12
13
14

(vi)
11
13
15
17
19

8. Output: ok
9. Output: oo
10. a) 9
b) 59049
c) error
d) 55
e) 1.0
f) 27.2
g) 10.0
h) error
i) True
j) True
11.'Else’ is used along with ‘if’ to define the alternative path if the condition mentioned in the ‘if’ statement is incorrect.
If more than one statements need to be evaluated, ‘elif’ construct is used.

12.
a) 20
22
24
26
28
b)
I
N
D
I
A
c)
0
0
4
4
12
'''
#13
x = int (input ("Enter the number : "))
if  x > 0:
    print ("positive number ")
elif x == 0 :
    print ("zero number ")
else :
    print ("negative number ")

#14
temp = float(input("Enter temperature = "))
unit = input("Enter unit of temperature (c or f) =")
if unit=="F" or unit == "f" :
    c = (5/9)*(temp - 32)
    print("Temperature in celsius = ",c,"C")
elif unit=="C" or unit == "c" :
    f = (9/5)*temp + 32
    print("Temperature in Fahrenheit = ",f,"F")
else :
    print("Invalid unit ")

#15
for i in range (10, 20, 2):
    print (i)

#16
num1 = float(input("Enter the First number:- "))
num2 = float(input("Enter the Second number:- "))
operator = input ("Enter Operator:- ")
if operator == "+":
    print (num1 + num2)
elif operator == "-":
    print (num1 - num2)
elif operator == "*":
    print (num1 * num2)
elif operator == "/":
    print (num1 / num2)
else:
    print ("invalid input")

#17
num = eval(input("Type a number: "))
for i in range(1,num + 1):
       factorial = factorial*i
       print("The factorial of",num,"is",factorial)

#18
num = int(input("Enter the Binary number:- "))
print (int(str(num), 2))

#19
num = input("Enter a number :-")
sum = 0
for i in num :
    sum += int (i)

print("Sum of digit :- ", sum)

#20
def primex():
    prime= []
    for num in range(2, 30):
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            prime.append(num)
    print("Prime numbers below 30:")
    for primex in prime:
        print(primex)

#21
x = int(input("Enter x :-"))
n = int(input("Enter n :-"))
sum = 0

for i in range(n+1):
    if (i+1) % 2 == 0:
        num = (x ** i) / math.factorial( i+1 )
        sum -= num
    else :
        num = (x ** i) / math.factorial( i+1 )
        sum += num
print("Sum :-", sum)

#22
x = int(input("Enter x :-"))
n = int(input("Enter n :-"))
sum = 1
for i in range(2,n+1):
    if i % 2 == 0:
        num = (x ** i) / math.factorial( 2*i )
        sum -= num
    else :
        num = (x ** i) / math.factorial( 2*i )
        sum += num
print("Sum : ", sum)

#22
x = eval(input("x value: "))
n = eval(input("n value: "))
s = 1
sign = -1
power = 2
fact = 1
for i in range(n):
    fact = 1
    for j in range(1,2*power+1):
        fact*=j
    print(fact)
    s+= ((x**power)/fact)*sign
    sign *= -1
    power+=1
print(s)


#23
num = int(input("Enter the number:- "))
sum = 0
for i in range (2, num + 2):
    t = 0
    for j in range (1, i):
        t += j
    print ("Term", (i - 1), ":", t)
    sum += term
print ("Sum of", num, "term is", sum)

#24 i)
def print_pattern (x) :
    for i in range (1, x + 1) :
        print (i * "*")
num = int (input ("Enter the number : - "))
print_pattern (num)

#ii)
for i in range (1, 6):
    print (chr(64 + i) * i)

#iii)    
a = "54321"
for i in range (1, 6):
    print (a[-i:])
