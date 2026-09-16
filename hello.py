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