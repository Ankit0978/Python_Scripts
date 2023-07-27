# a = "50"
# b = "3"
# print("The value of ", a, " + ", 3," is: ", int(a) + int(b))
# print("The value of ", a, " - ", 3," is: ", int(a) - int(b))
# print("The value of ", a, " * ", 3," is: ", int(a) * int(b))
# print("The value of ", a, " / ", 3," is: ", int(a) / int(b))

# # Input Function
# x = input("Enter first number: ")
# y = input("Enter second number: ")
# print(int(x) + int(y))

# x = input()
# print("My name is ",x)

# a = input("enter first number :" )
# b = input ("enter second number :" )
# print(a+b)

# print (""" He said i have
# no problem 
# what do u have""")

# name = "Harry,shubham"
# print(name[0:7])

# fruit = "mango"
# len1 = len(fruit)
# print("Mango is a", len1, "letter word")
# print(fruit[3:4])
# print(fruit[::-1])

# alpha = "mango"
# for i in alpha:
#     print(i)

# nm = "harry"
# print(nm[-4:-2])
# #print(nm[1:3])

# a = "hari!!!! !hari!!!!! !!!!!hari??? ??hari,,,"
# print(a.upper())
# print(a.lower())
# print(a.rstrip("!"))
# print(a.replace("hari","john"))
# print(a.split(" "))
# print(a.capitalize())

# str1 = "Welcome to the team"
# print(len(str1))
# print(str1.center(50))
# print(a.count("h"))

# str2 = "Welcome To The Console0000"
# print(str2.endswith("!"))
# print(str2.endswith("to",4,10))
# print(str2.find("to"))
# print(str2.find("the"))
# # print(str2.index("sssh"))
# print(str2.isalnum())
# print(str2.isalpha())
# str1 = "hi my name is ankit"
# print(str1.islower())
# str3 ="These all are '        '    printable characters.\n"
# print(str3.isprintable())
# str4 = "                   "
# print(str4.isspace())
# print(str2.istitle())
# print(str2.startswith("Welcome"))
# print(str2.swapcase())
# print(str2.title())

# a = int(input("Enter your age: "))
# print("Your age is: ",a)
# if (a>18):
#     print("You can drive")
# else:
#     print("You can't drive")

# x = int(input("Enter the value of x: "))

# match x:
#     case 0:
#         print(" x is zero")
#     case 4:
#         print(" x is 4")
#     case _ if x !=90:
#         print(x, "is not 90")
#     case _ if x !=80:
#         print(x , "is not 80")
#     case _:
#         print(x)

# For loops in string:
# name = "Abhishek"
# for i in name:
#     print(i)
#     if i =="k":
#         print("K is the last letter")

# For loops in list:
# list1 = ["Red","green","apple","blue"]
# for x in list1:
#     print(x)
#     for i in x:
#         print(i)

# for i in range(0,100):
#     print(i)

# for x in range(0,100,2):
#     print(x)

# z = int(input("Enter the number: "))
# while (z<=38):
#     z=int(input("Enter your number: "))
#     print(z)
# print("Done with the loop")

# y = 5
# while (y>0):
#     print(y)
#     y = y-1

# count = -5
# while (count>0):
#     print(count)
#     count = count -1
# else:
#     print("I am inside else")


# while True:
#     number = int(input("Input a positive number: "))
#     print(number)
#     if not number>0:
#         break

# for i in range(12):
#     if (i==10):
#         break
#     print("5 X", i+1 , "=", 5 *(i +1))
# print("Loop ko chodkar bahar aa jaayo")

# for z in range(11):
#     if (z ==9):
#         print("Skip the iteration")
#         continue
#     print("5 X", z , "=", 5 * z)

# for i in range(1,101,1):
#     print(i, end = " ")
#     if (i == 50):
#         break
#     else:
#         print("Missisippi")
# print("Thank you")

# y = 0
# while True:
#     print(y)
#     y = y + 1
#     if (y==100):
#         break

# def calculate_gmean (a,b):
#     mean = (a*b)/(a+b)
#     print(mean)
# def isgreater(a,b):
#     if (a>b):
#         print("First is greater than second")
#     else:
#         print("Second is greater than first")
# a= 20
# b= 30
# calculate_gmean(a,b)
# isgreater(a,b)
# c = 60
# d = 40
# calculate_gmean(40,60)
# isgreater(c,d)

# def average(a=1,b=7):
#     print("The average is", (a+b)/2)
# average(4,6)


# def average(a=2,b=9):
#     print("the average is", (a+b)/2)
# average(4)

# def average (*numbers):
#     sum = 0
#     for i in numbers:
#         sum = sum + i
#     print("Average is: ", sum/len(numbers))

# average(1,2,3,4,5,6,7,8,9)
    
# def name(**name):
#     print("Hello,", name["fname"], name["lname"], name["mname"])

# name(mname="Peter",lname="Johnson",fname="Smith")

# marks = [3,5,6,"Harry", True]
# if 7 in marks:
#     print("Yes")
# else:
#     print("No")

# if "Harry" in marks:
#     print("Yes")
# else:
#     print("No")

# if "arry" in "Harry":
#     print("Yes")
# else:
#     print("No")

# from _typeshed import IdentityFunction


# l = [45,35,43,65,75]
# # print(l)
# l.sort()
# print(l)
# l.reverse()
# print(l)   
# print(l.count(35))
# print(l)

# x = [23,45,67,78,89]
# print(x)
# b = x.copy()
# b[0]= 0
# print(b)

# b.insert(2,65)
# print(b) 

# z = [1,23,34,4,4)
# print(z)
# g = z+g
# Print(g)

# tup = (1,2,3,45,5,"green")
# print(tup[2:4])
# if 4 in tup:
#     print("2 is present in tup")
# else:
#     print("Not present")

# tup2 = tup[1:4]
# print(tup2)

# countries = ("Germany","russia","Iraq","Boho")
# list1=[]
# for i in countries:
#     # print(i)
#     if i =="Germany" or i =="russia":
#         pass
#     else:
#         list1.append(i)
# print(list1)
# temp = list(countries)
# print(temp)
# temp.append("Russia")
# print(temp)           # add item
# temp.pop()  
# print(temp)                   # remove item
# temp[2] = "finland"             # change item
# countries = tuple(temp)
# print(countries)

# f = [1,2,1,2,3,4,3]
# l=[]

# for i in f:
#     if i in l:
#         pass
#     else:
#         l.append(i)
# print(l)

# countries = ("Finland","Bangladesh")
# count1 = ("Iraq","Germany")
# count2 = countries + count1
# print(count2)

# print(count1.index("Iraq"))

# list1 = [1,1,1,1,2,2,3,3,4,4,5,5]
# list2=[]
# for i in list1:
#     if i in list2:
#         pass
#     else:
#         list2.append(i)
# print(list2)

# countries = ("Iraq","Bangladesh","Sudan","Africa")
# temp2 = list(countries)
# print(temp2)
# temp2.append("Russia")
# print(temp2)
# temp2.pop(3)
# temp2[2]="Finland"
# countries = tuple(temp2)
# print(countries)

# tuple1 = (1,23,4,3,5,6,3,8,3,90)
# res = tuple1.count(3)
# print("The count of tuple is: ", res)

# tup1 = [1,2,34,4,55,5,6]
# res1 = list(tup1)
# print(res1)

# import time
# timestamp = time.strftime("%H:%M:%S")
# hour = int(time.strftime("%H"))
# hour = int(input("Enter hour: "))
# print(hour)

# if (hour>=0 and hour<12):
#     print("Good morning sir")
# elif(hour>=12 and hour <17):
#     print("Good aftrenoon")
# elif(hour>=17 and hour<0):
#     print("Good night sir")

# name = "Ankit"
# country = "Paris"
# print(f"My name is {name} and my country is {country}")

# print(f"{2*30}")
# print(f" The name of {{country}} is {{name}} is finland ")
# print("")

# def fucn(n):
#     """ This function takes the function, 
#     returns the square of the function """
#     print(n*2)
# print(fucn(2))
# print(fucn.__doc__)

# def factorial(n):
#     if (n==0 or n==1):
#         return(1)
#     else:
#         return n * factorial(n-1)
# print(factorial(3))
# print(factorial(4))
# print(factorial(5))
# print(factorial(0))

# def fibbonaci(n):
#     if (n==0):
#         return(0)
#     elif (n==1):
#         return(1)
#     else:
#         return fibbonaci(n-1) + fibbonaci(n-2)
# print(fibbonaci(0))
# print(fibbonaci(1))
# print(fibbonaci(2))
# print(fibbonaci(3))
# print(fibbonaci(4))
# print(fibbonaci(5))
# print(fibbonaci(6))

# harry ={}
# print(type(harry))

# set1= {1,2,3,45,5,5,6}
# set2= {34,5,6,6,7,765,7,7}
# set3= (75,85,95,0)
# # print(set1.union(set2))
# # set1.update(set2)
# # print(set1,set2)
# # print(set1.intersection(set2))
# # print(set2.symmetric_difference(set1))
# # print(set1.difference(set2))
# # print(set1.isdisjoint(set2))
# # print(set1.isdisjoint(set3))
# print(set1.issuperset(set2))
# print(set1.issubset(set2))

# set4 = {"Berlin","tokyo"}
# set4.add("Paris")
# print(set4)
# set4.remove("Berlin")
# print(set4)


# setx= {2,3,4,5,6}
# set2= setx.pop()
# print(setx)
# print(set2)

# del setx
# print(setx)
# setz = clear().set2

# dic = {
#     367: "harry",
#     478: "ankit",
#     589: "shivam"
# }

# print(dic[367])

dic2 = {"name":"Karan", "age":19 , "eligible":True}
# print(dic2)
# print(dic2["name"])
# print(dic2.get("age"))
# print(dic2.get("eligible"))
# print(dic2.values())
# print(dic2.keys())

# for keys in dic2.keys():
#     print(dic2.keys())
#     print(dic2.values())
    
# for key,value in dic2.items():
#     print(f"The value corresponding to the key {key} is 
#     {value}")

# ep1 = {123:45, 143: 47, 45:467, 78:63}
# ep2 = {34:44, 67:89}
# ep1.update(ep2)
# print(ep1)
# ep1.pop(123)
# print(ep1)

# for i in range(6):
#     print(i)
#     if i==4:
#         break

# else:
#     print("there is no i")

# a = int(input("enter the given number"))
# print(f"Multiplication table of {a} is: ")
# try:
#     for i in range(0,11):
#         print(f"{int(a)} X {i} = {int(a)*i }")
# except Exception as e:
#     print(e)

# print("Some imp lines of code")
# print("End of program")

# try:
#     print(int(input("Enter an integer: ")))
# except ValueError:
#     print("Number enetered is not an integer")


# try:
#     num = int(input("Enter the given number"))
#     a = [6,3]
#     print(a[num])
# except ValueError:
#     print("Numbered enter is not an integer")
# except IndexError:
#     print("Index error")5

# def func1():
#     try:
#         l = [1,3,4,7]
#         i = int(input("Enter the index number"))
#         print(l[i])
#         return 1
#     except:
#         print("Some error occured")
#         return 0

#     finally:
#         print("This code will always execute")
    
# x = func1()
# print(x)

# a = int(input("Enter the number between 5 and 9"))
# if (a<5 or a>9):
#     raise ValueError("Value should be between 5 and 9")


# a = 330
# b = 3303
# print("A") if a>b else print("=")if a ==b else print("B")

marks = [10,23,45,67,98,1,40]

# for mark in marks:
#     print(mark)
#     if (index ==3):
#         print("Harry, awesome")
#     index +=1

# for index,mark in enumerate(marks, start=3):
#     print(mark)
#     if (index==3):
#         print("Harry, awesome")

name = "coding ninjas"
print(name.replace("a","x"))
print(name)