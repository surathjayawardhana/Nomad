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

        a=["hey","now",5,True]
        print(a)
        a.append("killer")
        a.append(False)
        len.a
        
        
        a = int(input("\nDo you want to try again(1/0): "))
        if a==0:
            break

    if (q==2):
        
        sale=[5000,5500,45000,75022,5000,54862,10005]

        x= int(input("enter your day (1,2,3,4,5,6,7): "))

        for i in range(7):
            if i == x:
                c = x-1
                print(sale[c])
                break

        
        
        
        a = int(input("\nDo you want to try again(1/0): "))
        if a==0:
            break


    if (q==3):

        #a hardeware owner want a system to stor infomation about 10 products and the salary parameters;
        #Design a program that allow user to enter value above system and display;

        p_id = ['E001','E002','R003','U456','T675','L987','W234','M875','M453','654B']
        p_name = ['cement','soil','nails','block','wire','tap','pipes','paint','nuts','balt']
        p_price = [3500,20000,5,100,8000,4200,1200,12000,75,50]
        
        print("+------+----------+--------+")
        print("| ID   | Name     | Price  |")
        print("+------+----------+--------+")
        for j in range (10):    
            print(f"| {p_id[j]:<4} | {p_name[j]:<8} | {p_price[j]:<6} |")
        print("+------+----------+--------+")  
               
            

        a = int(input("\nDo you want to try again(1/0): "))
        if a==0:
            break

    if (q==4):

        p_id=[]
        p_name=[]
        p_price=[]

        for i in range (10):
            p_id.append(str(input(f"\nEnter product {i+1} Id: ")))
            p_name.append(str(input(f"Enter product {i+1} name: ")))
            p_price.append(int(input(f"Enter product {i+1} price: ")))
        
        print("+------+----------+--------+")
        print("| ID   | Name     | Price  |")
        print("+------+----------+--------+")
        for j in range (10):    
            print(f"| {p_id[j]:<4} | {p_name[j]:<8} | {p_price[j]:<6} |")
        print("+------+----------+--------+")

        a = int(input("\nDo you want to try again(1/0): "))
        if a==0:
            break

    if (q==5):

        #Select any field acording to your priferences and store 3 parameters of 5 object in the selected 
        # team and output in a proper structure.

        Album=[]
        Genre=[]
        Artist=[]
        th=('ˢᵗ','ⁿᵈ','ʳᵈ','ᵗʰ','ᵗʰ')

        for i in range (5):
            Album.append(str(input(f"\nEnter Your {i+1}{th[i]} favourite Album: ")))
            Genre.append(str(input(f"Enter Music Genre of the {i+1}{th[i]} Album: ")))
            Artist.append(str(input(f"Enter Artist Name of the {i+1}{th[i]} Album: ")))
        
        print("+--------------+------------+-----------------+")
        print("| Album        | Genre      | Artist          |")
        print("+--------------+------------+-----------------+")
        for j in range (5):    
            print(f"| {Album[j]:<12} | {Genre[j]:<10} | {Artist[j]:<15} |")
        print("+--------------+------------+-----------------+") 
        
        a = int(input("\nDo you want to try again(1/0): "))
        if a==0:
            break

    if (q==6):
        #we remember thouge set of value is the maximum value at start.
        #now we can copiere remainging values one ofter another specila those values are grather to our current maximum.
        #if the value grater than currunt maximium it will be assign as a maximum otherwise we don't change the maximum.


        list_max = [78,56,23,52,98,1]
        kkk = 0
        for i in range(len(list_max)):
            if kkk < list_max[i]:
                kkk = list_max[i]

        print(f"Max value = {kkk}")
        
        a = int(input("\nDo you want to try again(1/0): "))
        if a==0:
            break

    if (q==7):

        min_list=[87,-65,-4,14,-112]
        kkk=0
        for i in range(len(min_list)):
            if kkk > min_list[i]:
                kkk = min_list[i]
                
        print(f"Minimum = {kkk}")
        
        a = int(input("\nDo you want to try again(1/0): "))
        if a==0:
            break


    if (q==8):

        find=[12,48,7,25,36,9,63,31]
        lev = 0
        for i in range(len(find)):
            if 25==find[i]:
                lev = i

        print(f"25 is in find list: find[{lev}]")

        
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