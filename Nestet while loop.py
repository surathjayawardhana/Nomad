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
        
        T=0
        while(T<5):
            T+=1
        print("Total =",T)

        a = int(input("\nDo you want to try again(1/0): "))
        if a==0:
            break

    if (q==2):

        f=1
        T=0
        while(f<6):
            x= int(input(f"Enter your number {f}: ")) 
            T= T+x  
            f+=1

        print(f"\nTotal {T}")       
        
        a = int(input("\nDo you want to try again(1/0): "))
        if a==0:
            break


    if (q==3):

        fc = 1
        even=0
        odd=0
        while(fc<6):
            x = int(input(f"Enter your number {fc}: "))
            fc+=1
            T = (x%2)
            if T == 0:
                even+=1
            else:
                odd+=1
        
        print(f"\nThere are {even} even numbers")
        print(f"There are {odd} even numbers")
        
        a = int(input("\nDo you want to try again(1/0): "))
        if a==0:
            break

    if (q==4):

        c = 0
        n = 1
        d = 0
        while(c<3):
            c+=1
            while(d<3):
                print(n,end=" ")
                n+=1
                d+=1
            print("\n")
            d = 0
            n = 1
        
        a = int(input("\nDo you want to try again(1/0): "))
        if a==0:
            break

    if (q==5):

        ol=0
        il=0
        star ="*"
        while(ol<4):
            ol+=1
            while(il<4):
                print(star,end=" ")
                il+=1
            print("\n")
            il =0

        
        a = int(input("\nDo you want to try again(1/0): "))
        if a==0:
            break

    if (q==6):
        
        ol=0
        il=0
        n = 1
        x = 1
        m = 1
        while(ol<4):
            ol+=1
            while(il<x):
                print(n,end=" ")
                il+=1
                n+=1
            print("\n")
            n =1
            m+=1
            x+=m
        
        r = 1
        while(r<=4):
            c=1
            while(c<=r):
                print(c,end=" ")
                c+=1
            print("\n")
            r+=1
        
        
        a = int(input("\nDo you want to try again(1/0): "))
        if a==0:
            break

    if (q==7):

        
        
        a = int(input("\nDo you want to try again(1/0): "))
        if a==0:
            break


    if (q==8):

        r=1
        c= 5
        x = 5
        m= 0
        while(r<=5):
            while(0<c<=5):
                print("*",end=" ")
                c-=1
            print("\n")
            r+=1
            m+=1
            c = x-m

        
        a = int(input("\nDo you want to try again(1/0): "))
        if a==0:
            break

    if (q==9):

        rows = 0
        rn = 1
        ln =1
        while(rows !=5): 
            c=0
            while(c != 12):
                print(f"{rn} * {ln} = {rn*ln}")
                ln+=1
                c+=1
            print("\n")
            rows+=1
            rn+=1
            ln =1
        
        a = int(input("\nDo you want to try again(1/0): "))
        if a==0:
            break

    if (q==10):

        
        
        a = int(input("\nDo you want to try again(1/0): "))
        if a==0:
            break