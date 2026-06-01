l=int(input("Enter a Question number: "))

if l==1:
    #Question 1
    #Write a Python program to input a number and check whether it is even or odd.

    # Get input from the user
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))

    # Display values before swapping
    print(f"\nBefore swapping: a = {a}")
    print(f"Before swapping: b = {b}\n")

    # Swapping...
    a, b = b, a

    # Display values after swapping
    print(f"After swapping: a = {a}")
    print(f"After swapping: b = {b}\n")
    input("Press Enter to exit...")


elif l==2:
    #Question 2
    #Write a Python program to input two numbers and display the larger number.

    x =int(input("Enter first number: "))
    y =int(input("Enter second number: "))

    if x>y:
        print("\n",f"Maximum number is {x}")
    else:
        print("\n",f"maximum number is {y}")

    input("\nPress Enter to exit...")

elif l==3:
    #Question 3
    #Write a Python program to input a number and determine whether it is positive or negative. Hint- Consider 0 as a positive number.
    num = int(input("\nEnter a number: "))

    if num > 0:
        print("\nThis number is positive.")
    elif num == 0:
        print("\nThis number is zero and considered positive according to question.")
    else:
        print("\nThis number is negative.")

    input("\nPress Enter to exit...")

elif l==4:
    #Question 4
    #Write a Python program to input student marks and display.

    #"Pass" if marks are 50 or above
    #"Fail" otherwise

    m = float(input("\nEnter your marks: "))

    if m>= 50:
        print("\nPassed")
    else:
        print("\nFailed")

    input("\nPress Enter to exit...")   

elif l==5:
    #Question 5
    #Write a Python program to input a person's age and determine whether the person is eligible to vote.

    age = int(input("\nEnter your age: "))

    if age>= 18:
        print("\nYou are eligible to vote.")
    else:
        print("\nYou are not eligible to vote.")
    
    input("\nPress Enter to exit...")

elif l==6:
    #Question 6
    #write a python program to input an integer and determine whether odd or even.

    num = int(input("\nEnter an integer: "))

    x = num % 2

    if x == 0:
        print("\nThis number is even.")
    else:
        print("\nThis number is odd.")
    
    input("\nPress Enter to exit...")

elif l==7:
    #Question 7
    #Write a python program to input a number and display whether it is:
    #positive, negative or zero.
    
    ddd = int(input("\nEnter a number: "))

    if ddd > 0:
        print("\nThis number is positive.")

    elif ddd == 0:
        print("\nThis number is zero.")

    else:
        print("\nThis number is negative.")

    input("\nPress Enter to exit...")

elif l==8:
    #Question 8
    #Write a python program to input three numbers and display the largest number.
    
    a = int(input("\nEnter first number: "))
    b = int(input("Enter second number: "))
    c = int(input("Enter third number: "))

    if a>b and a>c:
        print("\nThe largest number is", a)
    elif b>a and b>c:
        print("\nThe largest number is", b)
    else:
        print("\nThe largest number is", c)
    
    input("\nPress Enter to exit...")

else:
    print("\nThere is no question with that number you dumb fuck. Please try again.")
    input("\nPress Enter to exit...")