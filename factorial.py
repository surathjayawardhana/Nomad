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

        num = int(input("Enter your number: "))
        temp=0
        f=1
        c=0
        fn = []

        for i in range(num):
            if num ==0 or num == 1:
                print("factorials are = 1")
            else:
                temp = num - c
                fn.append(temp)
                f= temp*f
                c+=1
        print(f"\nfactorials are = {fn}")
        print(f"final value = {f}")


        
        a = int(input("\nDo you want to try again(1/0): "))
        if a==0:
            break

    if (q==2):

        count = 0
        num=[]
        for i in range(5):
            num.append(int(input("Enter your number: ")))
            if num[i] <= 1:
                print("This is not a prime number")
                continue
            else:
                prime = True
                for j in range(2,num[i]):
                    if num[i] % j == 0:
                        prime= False
                        break
            if prime:
                count = count+1
        print(f"There are {count} of prime numbers")                    

        
        a = int(input("\nDo you want to try again(1/0): "))
        if a==0:
            break


    if (q==3):

        
        
        a = int(input("\nDo you want to try again(1/0): "))
        if a==0:
            break

    if (q==4):

        
        
        a = int(input("\nDo you want to try again(1/0): "))
        if a==0:
            break

    if (q==5):

        
        
        a = int(input("\nDo you want to try again(1/0): "))
        if a==0:
            break

    if (q==6):

        
        
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