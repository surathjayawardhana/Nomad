while True:
    print("Question 0 - Test")
    print("Question 1 - Scollership Award")
    print("Question 2 - discount")
    print("Question 3 - Promotion")
    print("Question 4 - Electrcity Bill\n")

    q = int(input("Enter a Question Number: "))

    if q == 0:
        print("\ntest\n")
        c = 2
        if c == 2:
            if c < 3:
                print("\nc is less than 3")

        e= int(input("\nDo you want to continue? (1/0): "))
        if e == 0:
            break

    if q ==1:
        print("\nQuestion 1\n")
        
        att = int(input("Enter a your attendance percentage: "))
        avgm = int(input("Enter your average marks: "))

        if att >= 80:
            if avgm >= 75:
                print("\nScollership Awarded")
            else:
                print("\nScollership Not Awarded")
        else:
            print("\nInsuffcient Attendance")


        e = int(input("\nDo you want to continue? (1/0): "))
        if e == 0:
            break
    
    if q == 2:
        print("\nQuestion 2\n")
        
        cid = int(input("enter coustomer ID: "))
        pa = float(input("Enter Perchersed ammount: "))
        pcid = cid % 2

        if pcid == 0:
            if pa >= 10000:
                print("\n 20% " "discount Available")
                dis = pa - ((pa/100)*20)
                print(f"\n Final Amount =",dis)
            else:
                print("\n 10% " "discount Available")
                dis = pa - ((pa/100)*10)
                print(f"\n Final Amount =",dis)
        else:
            print("No discount Available")

        e = int(input("\nDo you want to continue? (1/0): "))
        if e == 0:
            break

    if q == 3:
        print("\nQuestion 3\n")
        
        ys = int(input("Enter your years of servies: "))
        ps = float(input("Enter your performance Score: "))

        if ps >= 85:
            if ys >= 3:
                print("\nPromotion Approved")
            else:
                print("\nMore experience Required")
        else:
            print("\nPreformance Improvement Required")

        e = int(input("\nDo you want to continue? (1/0): "))
        if e == 0:
            break

    if q == 4:
        print("\nQuestion 4\n")
        
        units = int(input("Enter Consumed Electrical Units: "))
        if units <= 30:
            final = units*20
            print(f"\nConsumed Units = {units}")
            print(f"Totle Bill = {final}")

        elif 30< units <= 60:
            first = 30*20
            second = (units - 30)* 40
            final = first + second
            print(f"\nConsumed Units = {units}")
            print(f"Totle Bill = {final}")

        elif units > 60:
            first = 30*20
            second = 30* 40
            therd = (units - 60)*60
            final = first + second + therd
            print(f"\nConsumed Units = {units}")
            print(f"Totle Bill = {final}")



        e = int(input("\nDo you want to continue? (1/0): "))
        if e == 0:
            break
        else:
            continue

    elif q > 4:
        print("invalid number")