# chalculate the area and perimeter of a cercle

r=float(input("enter the radius of the cercle: \n"))
pi=3.14

get = int(input("enter 1 for area and 0 for perimeter: \n"))

if get == 1:
    area = pi * r * r
    print("\nThe area of the cercle is: ", area,"\n")
elif get == 0:
    perimeter = 2 * pi * r
    print("\nThe perimeter of the cercle is: ", perimeter,"\n")
else:
    print("\ninvalid input")

input("\npress enter to exit")
