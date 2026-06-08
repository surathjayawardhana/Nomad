while True:
    q = int (input("\nEnter your damn question no: "))

    if q == 1:
        print("_____________________________________________________________________________________________________________")
        print("\nQuestion 01")
        print("Voting Eligibilitiy Verification system")

        age = int(input("\nEnter Your age: "))
        cit = int(input("Are you a ctizen of sri Lanka (1/0):"))
        if cit == 1:
            if age >= 18:
                print("\nYou're eligibil to vote")
            else:
                print("\nYou're Not eligibil to vote")
        elif cit == 0:
            print("\nYou're Not eligibil to vote")
        else:
            print("\nInvalid Respond")

        do = input("\nDo you want to try again (y/n): ")
        if do == "n" or do == "N":
            break
        print("_____________________________________________________________________________________________________________")


    if q == 2:
        print("_____________________________________________________________________________________________________________")
        print("\nQuestion 02")
        print("ATM Cash Withdrawal System")

        pin = int(input("\nEnter Your PIN Number: "))
        if pin == 1234:
            amount = int(input("\nEnter Withdrawal Amount: "))
            if amount <= 100000:
                print ("\nWithdrawel Succressful")
                print (f"Your account balance is: LKR. {100000-amount}")
            else:
                print("\nSorry, Your Account ballence is: 100000")
        else:
            print("\nInvalid PIN Number")
        do = input("\nDo you want to try again (y/n): ")
        if do == "n" or do == "N":
            break
        print("_____________________________________________________________________________________________________________")

    if q == 3:
        print("_____________________________________________________________________________________________________________")
        print("\nQuestion 03")
        print("Student Scholarship Evaluation")

        mark = int(input("\nEnter Your Marks: "))
        F_inc = int (input("Enter Your Family Income: "))

        if mark >= 75:
            if F_inc < 50000:
                print("\nYour Scholarship is approved")
            else:
                print("\nYour Scholarship is Not approved")
        else:
            print("\nYour Scholarship is Not approved")
    
        do = input("\nDo you want to try again (y/n): ")
        if do == "n" or do == "N":
            break
        print("_____________________________________________________________________________________________________________")


    if q == 8:
        print("_____________________________________________________________________________________________________________")
        print("\nQuestion 08")
        print("Grade Classification")

        Marks = int (input("\nEnter your Marks: "))

        if Marks >= 75:
            print ("\nYour Grade = A")
        elif 75 > Marks >= 65:
            print ("\nYour Grade = B")
        elif 65 > Marks >= 50:
            print ("\nYour Grade = C")
        else:
            print("\nYou're Faill")
        
        do = input("\nDo you want to try again (y/n): ")
        if do == "n" or do == "N":
            break
        print("_____________________________________________________________________________________________________________")

    if q == 7:
        print("_____________________________________________________________________________________________________________")
        print("\nQuestion 07")
        print("Hotel Reservation and check-in system(Hard)")

        Room = bool(input("\nDo rooms available (True/False): "))
        c_id = int(input("Enter your C_ID: "))
        AP = bool(input("Do willing to pay advance payment (True/False): "))
        SFN = bool(input("Do you willing to stay at least one night (True/False): "))

        if Room == True:
            if (c_id % 2) == 0:
                if AP== True and SFN == True:
                    print("\nYou're succressfully checked in")
            else:
                print("\nYour c_id Invalid ")
        else:
            print("\nRooms not available")
        do = input("\nDo you want to try again (y/n): ")
        
        if do == "n" or do == "N":
            break
        print("_____________________________________________________________________________________________________________")


