while True:
    q = int(input("Enter Question Number: "))

    if (q==1):
        print("\nQuestions N01  Hotel Billing System\n")

        room_charges = int(input("Enter Room Charges per day: "))
        no_of_days = int(input("Enter Number of days: "))
        food_charges = int(input("Enter Food Charges: "))
        service_charges_presetage = int(input("Enter Service Charges for Presetage: "))

        sub_total = (room_charges * no_of_days) + food_charges
        service_charges = (sub_total * service_charges_presetage) / 100
        Final_Bill = sub_total + service_charges

        print("\nSub Total: ", sub_total)
        print("Service Charges: ", service_charges)
        print("Final Bill: ", Final_Bill)

        i=input("\ndo you want to try another question? (y/n): ")
        if (i == 'n'):
            break

    elif (q==2):
        print("\nQuestions N02  Student GPA Calculator")
        s01 = int(input("Enter your maths marks"))
        s02 = int(input("Enter your programing fundermentel Marks"))
        i=input("\ndo you want to try another question? (y/n): ")
        if (i == 'n'):
            break
    
    

