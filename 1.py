while True:
    print("**********************************************************************************************")
    print("\nQuestion 01: ")
    print("Question 02: ")
    print("Question 03: ")
    print("Question 04: ")
    print("Question 05: ")
    print("Question 06: ")
    print("Question 07: ")
    print("Question 08: ")
    print("Question 09: ")
    print("Question 10: ")

    q = int(input("\nEnter your Question no: "))
    print("\n**********************************************************************************************\n")

    if (q==1):

        #Question 1: Hotel Billing System
        #Write a program to calculate the total hotel bill using room charge per day, number of days,
        #food charges, and service charge percentage. Display subtotal, service charge, and final
        #bill.

        charge_p_day = int(input("Room charge per day: "))
        noofday = int(input("Enter Days you stay: "))
        food_c = int(input("Enter Food Charges: "))
        service_c = int(input("service Charge Presentage: "))

        x = (charge_p_day*noofday)+food_c
        s = (x/100)*service_c

        print(f"SubTotal = {x}")
        print(f"service charge = {s}")
        print(f"Final bill = {x+s}")
        input()


        
        a = int(input("\nDo you want to try again(1/0): "))
        if a==0:
            break

    if (q==2):

        #Question 2: Student GPA Calculator
        #Write a program to input marks for 4 subjects and calculate total, average, and GPA using
        #a simple formula.

        sub = []
        marks = []
        for i in range(4):
            x = str(input("Enter Subject Name = "))
            y = int(input("Enter Subject Marks = "))
            sub.append(x)
            marks.append(y)

        total = 0
        t = "Total"
        print("_" * 33)
        for j in range (4):
            print(f"|{sub[j]:^15}|{marks[j]:^15}|")
            print("_" * 33)
            total = total + marks[j]

        print(f"|{t:^15}|{total:^15}|")
        print("_" * 33)

        input()
        
        a = int(input("\nDo you want to try again(1/0): "))
        if a==0:
            break


    if (q==3):

        #Question 3: Vehicle Trip Cost Estimator
        #Write a program to calculate total trip cost using distance traveled, fuel efficiency, fuel
        #price per liter, and highway charges. Display fuel used, fuel cost, and final trip cost.
        
        dis = float(input("distance traveled - "))
        fe = int(input("fuel efficiency - "))
        fp = int(input("fual price per liter - "))
        hw_c = int(input("highway charges - "))

        fu = (dis/fe)
        fc = fu * fp
        f = fc + hw_c

        print("Fual Used - " ,fu,"L")
        print("Fual cost - " ,fc,"LKR")
        print("Final Cost - " ,f,"LKR")

        a = int(input("\nDo you want to try again(1/0): "))
        if a==0:
            break

    if (q==4):

        #Question 4: Employee Payroll System
        #Write a program to calculate employee salary details using basic salary, overtime hours,
        #overtime rate, bonus, and tax percentage. Display gross salary, tax amount, and net salary.

        basic = int(input("Enter Basic Salary = "))
        ot = int(input("Enter #OT Houers = "))
        otr = int(input("Enter OT Rate = "))
        Bonus = int(input("Enter Bonus = "))
        Tax = int (input("Enter Tax% = "))

        gs = basic + (ot*otr) + Bonus
        t = (gs/100)* Tax
        net = gs -t

        print(f"\nG salary = {gs} \nTax = {t} \nNet Salary = {net} ") 
        
        a = int(input("\nDo you want to try again(1/0): "))
        if a==0:
            break

    if (q==5):

        for i in range(1,6):
            print(5, end="x")
            print(i, end="=")
            print(5*i)
        

        
        
        a = int(input("\nDo you want to try again(1/0): "))
        if a==0:
            break

    if (q==6):

        x = 0 
        y = 5


        for i in range(1,6):
            print(" "*(4-x), end="")
            print("*"*i,"*"*(6-y))
            x+=1
            y-=1

        x=0
        y=5
        for j in range(1,6):
            print(" "*(5-y), end="")
            print("*"*(5-x),"*"*y)
            x+=1
            y-=1
        
        
        a = int(input("\nDo you want to try again(1/0): "))
        if a==0:
            break

    if (q==7):

        
        
        a = int(input("\nDo you want to try again(1/0): "))
        if a==0:
            break


    if (q==8):

        
        
        a = int(input("\nDo you want to try again(1/0): "))
        if a==0:
            break

    if (q==9):

        
        
        a = int(input("\nDo you want to try again(1/0): "))
        if a==0:
            break

    if (q==10):

        
        
        a = int(input("\nDo you want to try again(1/0): "))
        if a==0:
            break