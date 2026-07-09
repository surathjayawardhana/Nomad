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

        n = 1
        for i in range (1):
            for j in range(10):
                print("*" * (n*n))
                n+=1
        
        
        a = int(input("\nDo you want to try again(1/0): "))
        if a==0:
            break

    if (q==2):

        mn = 1
        sn = 1

        for i in range(12):
            for j in range(12):
                print(f"{mn} * {sn} = {mn*sn}")
                sn+=1
            mn+=1
            sn = 1
            print("\n")
        
        a = int(input("\nDo you want to try again(1/0): "))
        if a==0:
            break


    if (q==3):

        list = [1,2,3,4]
        x = 1
        for i in range(5):
            for j in range(1):
                print ((list[0]*x),(list[1]*x),(list[2]*x),(list[3]*x))
                x+=1
            
        a = int(input("\nDo you want to try again(1/0): "))
        if a==0:
            break

    if (q==4):

        a = 1
        for i in range (5):
            for i in range(1):
                print("*"*a)
                a+=1
        print("\n")
        x = 4
        y = 1
        for i in range (5):
            for i in range(1):
                print(" " * x,"*"*y)
                x-=1
                y+=1
        
        print("\n")

        d=5
        for i in range (5):
            for i in range(1):
                print("*"*d)
                d-=1
        print("\n")
        b=0
        c=5
        for i in range (5):
            for i in range(1):
                print(" " * b,"*"*c)
                b+=1
                c-=1

        print("\n")

        x = 4
        y = 1
        z = 1
        k = 0
        h = 5
        o = 5
        for i in range (1):
            for i in range(5):
                print(" " * x,"*"*y,"*"*z)
                
                x-=1
                y+=1
                z+=1
            for p in range(5):
                print(" " * k,"*"*h,"*"*o)
                k+=1
                h-=1
                o-=1

        print("\n")

        x = 4
        y = [1,3,5,7,9]
        g = [7,5,3,1,0]
        s = 1
        for i in range (1):
            for j in range(5):
                print(" " * x,"*"*y[j])
                x-=1
            for v in range(5):
                print(" "*s,"*"* g[v])
                s+=1

        a = int(input("\nDo you want to try again(1/0): "))
        if a==0:
            break

    if (q==5):

        d= [1,2,3,4,5]
        x = 1
        for i in range(6):
            
            for j in range(1):
                print(f"desk {d[0]} desk {d[1]} desk {d[2]} desk {d[3]} desk {d[4]}")
            
        
        a = int(input("\nDo you want to try again(1/0): "))
        if a==0:
            break

    if (q==6):
        f = 0
        icbox = 0
        ic =0
        for i in range(4):
            f+=1
            for j in range(6):
                icbox+=1
                for k in range(20):
                    ic+=1
        print(f"Total number of ice cream boxes = {icbox}")
        print(f"Total number of ice creams in the shop = {ic}")

        
        a = int(input("\nDo you want to try again(1/0): "))
        if a==0:
            break

    if (q==7):

        classrooms = 0
        students = 0
        examfee =0
        for i in range(5):
            classrooms+=1
            for j in range(25):
                students+=1
        print(f"Total number of students = {students}")
        print(f"Total examination fee collected = LKR.{students*500}")

        a = int(input("\nDo you want to try again(1/0): "))
        if a==0:
            break


    if (q==8):

        trees = 0
        orange =0
        for i in range(8):
            trees+=1
            for j in range(35):
                orange+=1
        print(f"The total number of oranges harvested = {orange}")
        
        a = int(input("\nDo you want to try again(1/0): "))
        if a==0:
            break

    if (q==9):

        rooms =0
        for i in range(6):
            for j in range(18):
                rooms+=1
        
        print(f"Total number of rooms = {rooms}")
        print(f"Total income for one night = LKR.{rooms * 12000}")
        
        a = int(input("\nDo you want to try again(1/0): "))
        if a==0:
            break

    if (q==10):

        passengers_on_f = 0
        total_passengers = 0
        x = 0

        for i in range(5):
            x+=1
            for j in range(30):
                for k in range(6):
                    total_passengers+=1
                    if x==1:
                        passengers_on_f+=1
                
                    
        print(f"Number of passengers on one flight = {passengers_on_f}")
        print(f"Total number of passengers on all flights = {total_passengers}")
    

        
        a = int(input("\nDo you want to try again(1/0): "))
        if a==0:
            break