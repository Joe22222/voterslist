print("joe","dpsdubai",sep = "@")
print("dubai", end = "_2023")
print("Hello")
print()
print()
print()

#Arithmetic operations
num1 = eval(input("Type first number: "))
num2 = eval(input("Type second number: "))
ch = eval(input(''' Sum - 1,
Dif - 2,
Pro - 3
Div - 4

Choice: '''))
if ch ==1:
    print(num1 + num2)
elif ch ==2:
    print(num1 - num2)
elif ch ==3:
    print(num1 * num2)
else:
    print(num1/num2)

#Logical operations
print("Hi" and 0)
print("Hi" or 0)

#Relational operations
x = int(input())
y = int(input())
print(is x>y) #Indentity

list1 = [1,2,3,4]
print(is 10 in list1) #Membership and Identity


