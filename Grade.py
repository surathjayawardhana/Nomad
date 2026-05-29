#> Write a program to output the “Grade” when student enter marks according to following criteria.
#	M >= 75	A
#   M >= 65	B
#	M >= 55	C
#	M >= 40	D
#	M <   40	Faill

while True:
    #Input Marks
    m = float(input("\nEnter Your Mark : "))

    if (m>= 75):
        print("\nYour grade = Grade A")
    elif (75 >m>= 65):
        print("\nYour grade = Grade B")
    elif (65 >m>= 55):
        print("\nYour grade = Grade c")
    elif (55 >m>= 40):
        print("\nYour grade = Grade S")
    else:
        print("\nYou are Failled")

    x = input("\nDo you want to run again (y/n) : ")
    if x== "n":
        break

