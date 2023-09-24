#Practical Implementations

#Counting number of occurrences of a character in a string
str = input("Type a string: ")
ch = input("Enter the character to be searched: ")
count = 0
for character in str:
    if character ==ch:
        count+=1
print("Number of times character",ch,"occurs in the string is: ",count)

#Print string in reverse order
str = input("Type a string: ")
for i in range(-1,-len(str)-1,-1):
    print(str[i],end="")

#Printing name pattern
name = input("Enter name: ")
for i in range(0,len(name)+1):
    print(name[0:i])

#Printing longest substring of a string
string = input("Enter a string")
length = len(string)
maxlength = 0
maxsub = ""
sub = ""
lensub = 0
for a in range(length):
    if string[a] in "aeiou" or string[a] in "AEIOU":
        if lensub>maxlength:
            maxsub=sub
            maxlength=lensub
            sub = ""
            lensub = 0
        else:
            sub+=string[a]
            lensub = len(sub)
            a+=1
print("Max length consonant is: ",maxsub, end = " ")
print("with", maxlength,"characters")

#Program to accept string and return string having first letter of each word in capital letter
str1 = input("Type a string: ")
print("Original string:",str1)
str2 = ""
x = str1.split()
for a in x:
    str2 += a.capitalize() + " "
print(str2)

#Program that accepts a strign and prints string after capitilizing every other letter in string
string = input("Type a string")
length = len(string)
print("Original string: ",string)
string2 = " "
for a in range(0,length,2):
    string2+=string[a]
    if a<length-1:
        string2+=string[a+1].upper()
print("Result: ",string2)

'''Write a progoram that reads a line and prints its frequency chart like,
Number of uppercase letters
Number of lowercase letters
Number of alphabets
Number of digits'''
line = input("Enter a line: ")
lowercount = uppercount = 0
digitcount = alphacount = 0
for a in line:
    if a.islower():
        lowercount +=1
    elif a.isupper():
        uppercount+=1
    elif a.isdigit():
        digitcount+=1
    if a.isalpha():
        alphacount+=1
print("Number of uppercase letters: ",uppercount)
print("Number of lowercase letters: ",lowercount)
print("Number of alphabets: ",alphacount)
print("Number of digits: ",digicount)


#Solved Questions

#To check if a string is palindrome or not
str = input("Enter the string: ")
l = len(str)
p = l-1
index = 0
while(index<p):
    if(str[index]==str[p]):
        index+=1
        p = p-1
    else:
        print("String is not a palindrome")
        break
else:
    print("String is a palindrome")

#Write a program that reads a line, then counts and displays how many words are there in the line
line = input("Enter line: ")
x = line.split()
cnt = 0
for i in x:
    cnt+=1
print(cnt)

#Write a program  that reads a string and then prints a string that capitalizes every other letter in string
str = input("Enter a string: ")
length = len(str)
print("original string:",str)
str2 = ""
for a in range(0,length):
    if a%2==0:
        str2 += string[a]
    else:
        str2+= str[a].upper()
print(str2)

#Write a program that reads a line, then counts how many times a substring "is" appears in the line and displays the count
str1 = input("Enter line: ")
str2 = "is"
L = str1.split()
cnt = 0
for i in L:
    if i ==str2:
        cnt+=1
print("Substring is appearing: ",cnt)

#Write a program that reads a string and displays the longest substring of the given string
str1 = input("Enter a string: ")
word = str1.split()
maxlength = 0
maxword = ""
for i in word:
    x = len(i)
    if x>maxlength and i.isalpha()==True:
        print(i)
        maxlength = x
        maxword = i
print("Substring with maximum length is: ",maxword)

#Write a program to remove vowels from a string
str = input("Enter a string: ")
strx = ""
for i in str.lower():
    if i !=  "a" and "e" and "i" and "o" and "u" :
        strx+=i
print("New word without any vowels is",strx.capitalize())

#Write a program to input a string having some digits and reutrn the sum of digits present in the string
a = input("Enter a string with digit: ")
c = 0
for i in a:
    if i.isdigt():
        c+=int(i)
print(c)


#Unsolved Questions

'''#6
Substring, 'work', found at index: 0
Substring, 'har, found at index: 5
Doesn't contain given substring

#7
i) Computer Science
ii) Scienc
iii) Cmue cec
iv) Computer ScienceComputer Science
v) enisrtpo

#8
a) sequence = 'sequence'
index = sequence.find('e', sequence.find('e') + 1, sequence.find('e', sequence.find('e') + 1) + 1)
print(index)

b) string = 'FuNTioN'
changed_string = string.swapcase()
print(changed_string)

c) string = 'School'
exists = 'Whether' in string
print(exists)


#9
a) s = "Global Warming"
print( s[-4 : ] )

b) s = "Global Warming"
print( s[-4 : ] )


#10
#mINDAwORKA

#11
s = input ("Enter a String :- ")
word = s.split("h")
print(word)


#12
input_string = input("Type a string: ")
words = input_string.split()
title_case_words = [word.capitalize() for word in words]
title_case_string = ' '.join(title_case_words)
print(title_case_string)

#13
def replace_blanks_with_hyphens(sentence):
    modified_sentence = sentence.replace(' ', '-')
    print(modified_sentence)

#14
s = "INSTITUTE"
word = s.split("T")
print(word)

#15
mmin
y Py
My Python Program
My Python Programming
My Python
My

#16
s = input("Enter a string :-")
print("Number of a in string :-" , s.count("a") )
print("Number of e in string :-" , s.count("e") )
print("Number of i in string :-" , s.count("i") )
print("Number of o in string :-" , s.count("o") )
print("Number of u in string :-" , s.count("u") )

#17
line = input("Enter a Line :-")
print("Number of 'is' in line :-" , line.count("is") )

#18
s = input("Enter a string :-")
new = ""

for i in s :
    if i != "i" :
        new += i

print(new)


#Case Study

#To check validity of phone number
val = False
while val is not True:
    num = input("Type your phone number: ")
    if len(num) ==12:
        if num[3] and num[7] == "-":
            if (num[:3] and num[4:7] and num[8:12]).isdigit():
                print("This is a valid number.")
                val = True
            else:
                print("Not a valid number.")
                val = False
        else:
            print("Enter a valid number.")
            val = False
    else:
        print("Enter a valid number.")
        val = False

#Finding out statistics relating to sentences
txt = input("Type a sentence: ")
count_word = 1
count_chr = len(txt)
count_alnum = 1
for i in txt:
    if i == " ":
        count_word+=1
    elif  i.isalnum():
        count_alnum+=1
    else:
        print("Enter a valid text")
perc = (count_alnum)/(count_chr) * 100
print("Number of words are",count_word)
print("Number of characters are",count_chr)
print("Percentage of alphanumeric characters is",perc)
'''
