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
        s01 = int(input("Enter Marks of Subject 1: "))
        s02 = int(input("Enter Marks of Subject 2: "))
        s03 = int(input("Enter Marks of Subject 3: "))
        s04 = int(input("Enter Marks of Subject 4: "))
        s05 = int(input("Enter Marks of Subject 5: "))

        cc1 = float(input("Enter Credit Hours of Subject 1: "))
        cc2 = float(input("Enter Credit Hours of Subject 2: "))
        cc3 = float(input("Enter Credit Hours of Subject 3: "))
        cc4 = float(input("Enter Credit Hours of Subject 4: "))
        cc5 = float(input("Enter Credit Hours of Subject 5: "))

        marks = [s01, s02, s03, s04, s05]
        credit_hours = [cc1, cc2, cc3, cc4, cc5]

        A = 4.0
        A_minus = 3.7
        B_plus = 3.3
        B = 3.0
        B_minus = 2.7
        C_plus = 2.3
        C = 2.0
        C_minus = 1.7
        D = 1.0
        F = 0.0

        #find grade points value for each subject

        grade_points = []
        for i in range (len(marks)):
            if marks[i] >= 90:
                grade_points.append(A)
            elif marks[i] >= 85:
                grade_points.append(A_minus)
            elif marks[i] >= 80:
                grade_points.append(B_plus)
            elif marks[i] >= 75:
                grade_points.append(B)
            elif marks[i] >= 70:
                grade_points.append(B_minus)
            elif marks[i] >= 65:
                grade_points.append(C_plus)
            elif marks[i] >= 60:
                grade_points.append(C)
            elif marks[i] >= 55:
                grade_points.append(C_minus)
            elif marks[i] >= 50:
                grade_points.append(D)
            else:
                grade_points.append(F)
        
        #calculate Quality Points for each subject
        quality_points = []
        for i in range (len(grade_points)):
            quality_points.append(grade_points[i] * credit_hours[i])
        
        #calculate total quality points and total credit hours
        total_quality_points = sum(quality_points)

        total_credit_hours = sum(credit_hours)

        #calculate GPA
        GPA = total_quality_points / total_credit_hours
        print("\nGPA: ", GPA)
        i=input("\ndo you want to try another question? (y/n): ")
        if (i == 'n'):
            break
    
    

