NUM1 = int(input("Enter the first number: "))
NUM2 = int(input("Enter the second number: "))
NUM3 = int(input("Enter the third number: "))

if (NUM1 > NUM2 and NUM1 < NUM3) or (NUM1 < NUM2 and NUM1 > NUM3):
    print("\nThe middle number is: ", "First number")
elif (NUM2 > NUM1 and NUM2 < NUM3) or (NUM2 < NUM1 and NUM2 > NUM3):
    print("\nThe middle number is: ", "Second number")
else:    print("\nThe middle number is: ", "Third number")
input("\nPress Enter to exit...")