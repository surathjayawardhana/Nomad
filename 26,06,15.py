while True:
    print("**********************************************************************************************")
    print("\nQuestion 1: ")
    print("Question 2: ")
    print("Question 3: ")
    print("Question 4: ")
    print("Question 5: ")
    print("Question 6: ")
    print("Question 7: ")
    print("Question 8: ")
    print("Question 9: ")
    print("Question 10: ")

    q = int(input("\nEnter your Question no: "))
    print("\n**********************************************************************************************")

    if (q==1):

        weight = int(input("\nEnter Your Bagage Weight: "))

        if weight <= 20:
            print("\nNo Extra Charge appled")
        elif 20 < weight < 30 :
            print("\extra charge appled")
            print((weight-20)* 200,"LKR" )
        else:
            print("\nBagage not allowed")
        
        a = int(input("\nDo you want to try again(1/0): "))
        if a==0:
            break

    if (q==2):

        salary = int(input("Enter your salary: "))

        if salary >= 100000:
            print("\n Bonus: ",(salary/100)*15)

        elif salary >= 50000:
            print("\n Bonus: ",(salary/100)*10)

        else:
            print("\n No Bonus: ")    
        
        a = int(input("\nDo you want to try again(1/0): "))
        if a==0:
            break


    if (q==3):
        t= 0
        v= 0
        for i in range(10):
            t = t + 1
            v = v +t
        print(v)
        
        a = int(input("\nDo you want to try again(1/0): "))
        if a==0:
            break

    if (q==4):
        n = 1
        m= 0
        for i in range (10):
            a = int(input(f"Enter your {n} number: "))
            m = m+a 
        avg = (m/10)
        print (f"\n AVG =", (m/10))

        if avg  < 50:
            print("\nFaill")
        else:
            print("\nPass") 
        
        
        a = int(input("\nDo you want to try again(1/0): "))
        if a==0:
            break

    if (q==5):
        b=0
        while True:
            x = int(input("Enter Your Number: "))
            if x == -1:
                break
            else:
                b = b+x
        
        print(f"\nSum = {b}")

        
        
        a = int(input("\nDo you want to try again(1/0): "))
        if a==0:
            break

    if (q==6):

        qr = str(input("\nEnter Your Word: "))

        a = qr.count("a")
        e = qr.count("e")
        i = qr.count("i") 
        o = qr.count("o") 
        u = qr.count("u") 

        p = qr.count("A")
        q = qr.count("E")
        r = qr.count("I") 
        s = qr.count("O") 
        t = qr.count("U") 

        count =(a+e+i+o+u+p+q+r+s+t)

        print(count)

        
        a = int(input("\nDo you want to try again(1/0): "))
        if a==0:
            break

    if (q==7):

        num = int(input("\nEnter Your Number: "))



        
        
        a = int(input("\nDo you want to try again(1/0): "))
        if a==0:
            break

    if (q==8):

        while True:
            
            age = int(input("\nEnter your age: "))
            if age >= 18:
                print ("Eleggeble to vote")
            elif 0 < age < 18:
                print ("Not Eleggeble to vote")
            elif age == -1:
                print ("Program Ended")
                break
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