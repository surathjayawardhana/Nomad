#basic IF condition 
#Write a programe to find the maximum out of two numbers?

num1 = int(input("enter First number    : "))
num2 = int(input("enter Second Number   : "))

if (num1>num2):
    print(f"\n{num1} is the Bigger number")
else:
    print(f"{num2} is the bigger number")

input("\nclick enter for next..")

#Write a program to check person eligibilitiy to vote?

age = int(input("\nEnter your age : "))

if age>=18:
    print("\nYou are eligibilitiy to vote in sri lanka")
else:
    print("\nYou are not eligibilitiy to vote in sri lanka")

input ("\nclick enter for next")

#> Write a program to check number is even or odd?

numx = float(input("\nEnter your number     = "))
x =numx%2
if x == 0:
    print("\nThis is an even number")
else:
    print("\nThis is an odd number")

input("\nclick enter for next")

#Write a program for find a maximum out of three numbers?

n01 = float(input("\nEnter Your 1st Number    :"))
n02 = float(input("Enter Your 2nd Number    :"))
n03 = float(input("Enter Your 3rd Number    :"))

if (n01>n02) and (n01>n03):
    print(f"\nThe maximum number is {n01}")
elif (n02>n01) and (n02>n03):
    print(f"\nThe maximum number is {n02}")
else:
    print(f"\nThe maximum number is {n03}")

input("\nclick enter for next")

