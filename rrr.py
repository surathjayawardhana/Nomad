while True:
    print("**********************************************************************************************")
    print("\nQuestion 1: ")
    print("Question 2: ")
    print("Question 3: ")
    print("Question 4: ")
    print("Question 5: ")
    q = int(input("\nEnter your Question no: "))
    print("\n**********************************************************************************************")
    if (q==1):
        x=0
        total = 0
        avg = 0
        highest = 0
        lowest = 10000000000000000000000000
        #Assume sales are always lower than 10000000000000000000000000:
        for i in range(1,7):
            x = float(input(f"Enter Day {i} sales: "))
            if (highest < x):
                highest = x
            
            if (lowest > x):
                lowest = x

            total = total + x
            avg = total / 7
        
        print(f"\nTotal: {total}")
        print(f"Avarage: {avg}")
        print(f"Highest: {highest}")
        print(f"Lowest: {lowest}")
        
        a = int(input("\nDo you want to try again(1/0): "))
        if a==0:
            break

    if (q==2):

        user = [1,2,3,4,5]
        for i in range (5):
            user[i] = int(input(f"ENTER USER {user[i]} CONSUMEMD NO. OF UNITS: "))
            
            if user[i] <= 100:
                T = user[i]*10
                print(f"Your bill = {T} LKR")

            elif 200 >= user[i] > 100:
                p1 = user[i] -100
                T = (p1* 15) + (100* 10)
                print(f"Your bill = {T} LKR")
            
            elif user[i] > 200:
                p1 = user[i] - 200
                T = (p1* 20) + (100* 10) + (100*15)
                print(f"Your bill = {T} LKR")

            
        a = int(input("\nDo you want to try again(1/0): "))
        if a==0:
            break


    if (q==3):

        att = [0,1,2,3,4,5,6,7,8,9]
        avg = 0
        P =0
        F =0
        total = 0
        for i in range(10):
            att[i] = int(input(f"Enter Your Attendece: "))

            if att[i] >= 75:
                P = P+1
            else:
                F= F+1
            total = total + att[i] 

        avg = total/10
        print(f"\nAvarage = {avg}")
        print(f"No. of students Eligible = {P}")
        print(f"No. of student Not Eligible = {F}")

        a = int(input("\nDo you want to try again(1/0): "))
        if a==0:
            break

    if (q==4):
        total =0
        no = 1
        avg = 0
        inp = 0

        while True:
            inp = float(input(f"Enter your purchased No {no}: "))
            no = no + 1
            total = total + inp
            if inp==0:
                break

        no = no-2
        avg = total/no
        print(f"\nTotal Bill: {total}")
        print(f"No. of Items: {no}")
        print(f"Avarage price of items: {avg}")       
        
        a = int(input("\nDo you want to try again(1/0): "))
        if a==0:
            break

    if (q==5):

        ab = 50000
        Wa = 0
        no = 0
        while True:
            Wa = int(input("Enter Withdrawel Ammount: "))
            if ab >= Wa:
                ab = ab - Wa
                no = no + 1
                print("Withdrawal successful")
                ark = int(input("\nDo you want to do another transfaction(1/0): "))
                if ark == 0:
                    break
            else:
                print("\nInsuffcient Balance")
        print(f"\nRemaing Balance: {ab}")
        print(f"Total amount of withdrawel: {50000- ab}")
        print(f"No. of successful Withdrawal {no}")

        
        a = int(input("\nDo you want to try again(1/0): "))
        if a==0:
            break