print("hello")
a = 1
b = True
c = "Harry"
d = None
print(a, b, c, d)
print("the type of a is",type(a))
print("the type of b is",type(b))
print("the type of c is",type(c))
print("the type of d is",type(d))      
a1 =  complex(8, 2)
print(a1)
print("the type of a1 is",type(a1))
list1 = [8, 2.3, [-4, 5],["apple"]]
print(list1)

tuple1 = (("parrot", "sparrow","lion"), ("tiger"))
print(tuple1)

dict1 = {"name": "harry", "age":19, "drive" : True}
print(dict1)

print(5+6)
print(6-5)
print(14*8)
print(15/9)
print(4**6)
print(56//4)
print(56%4)

#Create a calculator capable of performing addition, subtraction, mutiplication, division operation on two numbers. your program should format the output in a readable manner.
A = int(input("enter first number : "))
B = int(input("enter second number : "))
print("Addition : ",A + B)
print("Subtraction : ",A - B)
print("Multiplication : ",A * B)
print("Division : ",A / B)

a = 1
b = 2
print(a + b)
a = "1"
b = "2"
print(a + b)
print(int(a) + int(b))

#Explicit typecasting
string = "15"
number = 7
string_number = int(string)
sum = string_number + number
print("the sum of both the numbers is : ",sum)

#Implicit typecasting
a = 5
b = 2.5
print(a + b)

#user input
a = input("enter your name : ")
print("My name is :" ,a)

x = input("enter first number : ")
y = input("enter second number : ")
print(x + y)
print(int(x) + int(y))

name = "ravi"
friend = "shyam"
apple = '''apple,
i am good
i am gorgeous
"this is nice'''
print("hari, " + name)
print(apple)
#indexing
print(name[0])
print(name[3])
print(name[2])
print(name[1])
#print(name[4]) throws error as the index is out of range
print("Lets use a for loop\n")
for character in apple:
    print(character)

#string slicing
name = "ravi, ravina"
print(name[0:4])
print(len(name))
print(name[2:4])

nm = "Harry"
print(nm[-4:-2])

#strings are immutable
a = "!!!Harry!!!!!!! !!! Harry Harry"
print(len(a))
print(a)
print(a.upper())
print(a.lower())
print(a.rstrip("!"))
print(a.replace("Harry", "RAVI"))
print(a.split(" "))
blogHeading = "introduction to python"
print(blogHeading.capitalize())

str1 = "Welcome to the Console!!!"
print(len(str1))
print(len(str1.center(60)))
print(str1.center(60))
print(a.count("Harry"))

str1 = "Welcome to the Console!!!"
print(str1.endswith("!!!"))
print(str1.endswith("to", 2, 10))

str1 = "he's name is Dan. He is an honest man."
print(str1.find("is"))
print(str1.find("ish"))
# print(str1.index("ish"))

str1 = "WelcomeToTheConsole"
print(str1.isalnum())
str1 = "Welcome"
print(str1.isalpha())
str1 = "Welcome00"
print(str1.isalpha())
str1 = "Welcome235"
print(str1.isalpha())

str1 = "hello world"
print(str1.islower())
str1 = "Hello world"
print(str1.islower())

str1 = "We wish you a mery christmas"
print(str1.isprintable())
str1 = "We wish you a mery christmas\n"
print(str1.isprintable())

#using Spacebar
str1 = "       "
print(str1.isspace())
#using tab 
str1 = "    "
print(str1.isspace())

str1 = "World Health Organization"
print(str1.istitle())
str1 ="To kill a Mocking bird"
print(str1.istitle())

str1 = "hello world"
print(str1.startswith("hello"))

str1 = "HeLLo wOrld"
print(str1.swapcase())

str1 = "His name is mariya"
print(str1.title())

#if-else statement
a = int(input("Enter your age : "))
print("your age is : ",a)
#conditional statement
# >, < , >=, <=, ==, !=
print(a>18)
print(a<18)
print(a>=18)
print(a<=18)
print(a==18)
print(a!=18)
if(a>=18):
    print("you can drive")
else:
    print("you cannot drive")

applePrice = 10
budget = 200
if(budget - applePrice > 50):
    print("Alexa,add 1 kg Apple to the card")
else:
    print("Alexa, do not add Apple to the card") 

num = int (input("Enter the value of num : "))
if(num<0):
    print("The number is negative.")
elif(num==0):
    print("The number is zero.")
elif(num==999):
    print("The number is special.")
else:
    print("The number is positive.")     

#nested statement
num = 18
if(num<0):
    print("The number is negative.")
elif(num>0):
    if(num<=10):
        print("number is between 1-10")
    elif(num<=20):
        print("number is between 11-20")
    else:
        print("number i greater than 20")
else:
    print("The number is zero.")

#question
a = int(input("enter the time : "))
if(4 <= a < 12):
    print("Good Morning")
elif(12 <= a < 16):
    print("Good Afternoon")
else:
    print("Good evening")

#match case statement
x = int(input("enter the value of x : "))
match x:
    case 0:
        print("x is zero")
    case 1:
        print("x is 1")
    case 7:
        print("x is 7")
    
    case _ if x!=90:
        print(x, "is not 90")
    case _ if x!=40:
        print(x, "is not 40")
    case _:
        print(x)

#loops
name = "abhishek"
for i in name:
    print(i)
    if(i =="b"):
        print("This is something special!")
 
colors = ["Red", "Green", "Blue", "Yellow"]
for color in colors:
    print(color)
    for i in color:
        print(i) 
#range():
for i in range(101):
    print(i)
for k in range(14):
   print(k+1)    
for k in range(1, 20001):
    print(k)   
for g in range(1, 12, 2):
        print(g)
#i = 0
#while(i<=3):
   # print(i)
   # i = i+1
#i = int (input("enter the number: "))
#while(i<=38):
 #   i = int(input("enter the number: "))
  #  print(i)      
#print("done with the loop")
count = -5
while (count > 0):
   print(count)
   count = count - 1
else:
    print("i am inside else") 
#function
def calculategmean(a,b):
    mean = (a*b)/(a+b)
    print(mean)

def isgreater(a,b):
    if(a>b):
        print("First number is greater")
    else:
        print("Second number is greater")     

def islesser(a,b):
   pass
a = 9
b = 8
isgreater(a,b)
#if(a>b):
 #   print("First number is greater")
#else:
 #   print("Second number is greater")    
#gmean1 = (a*b)/(a+b)
#print(gmean1)
calculategmean(a,b)

c = 8
d = 7
isgreater(c,d)
#if(c>d):
#    print("First number is greater")
#else:
 #   print("Second number is greater")    
#gmean2 = (c*d)/(c+d)
#print(gmean2)
calculategmean(c,d)
def average(a=5,b=7):
    print("the average is:", (a+b)/2)
#average(4,6)
average()

def name(fname, mname = "jhon", lname = "whatson"):
    print("Hello", fname, mname, lname)
name("Amy", "Agrawal","Singh")

def average(*numbers):
    print(type(numbers))
    sum = 0
    for i in numbers:
        sum = sum + i
    #print("Average is : ", sum/len(numbers))
    return 7
    return sum / len(numbers)

c = average(5,6,5,6,7,8,9,10)      
print(c)
def name(**name):
    print(type(name))
    print("Hello", name["fname"], name["mname"], name["lname"])

name(mname = "buchannan", lname = "barner", fname = "james") 
l = [1,2,3,4,]
print(l)
print(type(l))
print(l[0])
print(l[1])
print(l[2])
print(l[3])