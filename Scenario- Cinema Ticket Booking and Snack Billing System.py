#Scenario: Cinema Ticket Booking and Snack Billing System

#getting input

print("-"*50,)
Casier_name = str(input("Enter Casier's name = "))
coutomer_name = str(input("Enter Costamer's name = "))
Ticket_type = int(input ("Enter ticket Type (Child = 1 / Student = 2 / Adult = 3) = ")) 
Snak_YN = str(input("Do you want any snack (Yes/No) = ")).upper()
print("-"*50,"\n")

#data verification

import string
c = Casier_name.isalpha()
co = coutomer_name.isalpha()

#Casier_name
while True:
    if c == True:
        break
    else:
        print("-"*50,"")
        print("Invalid Casier name; check again")
        Casier_name = str(input("Enter Casier's name = "))
        c = Casier_name.isalpha()
        print("-"*50,"\n")

#coutomer_name
while True:
    if co == True:
        break
    else:
        print("-"*50,"")
        print("Invalid coutomer name; check again")
        coutomer_name = str(input("Enter coutomer's name = "))
        co = coutomer_name.isalpha()
        print("-"*50,"\n")

#Ticket_type
while True:
    if Ticket_type in (1,2,3):
        break
    else:
        print("-"*50,"")
        print("Invalid Ticket_type; check again")
        Ticket_type = int(input ("Enter ticket Type (Child = 1 / Student = 2 / Adult = 3) = ")) 
        print("-"*50,"\n")

#snack
while True:
    if Snak_YN in ("YES") or Snak_YN in ("NO"):
        break
    else:
        print("-"*50,"")
        print("Invalid answer for [Do you want any snack (Yes/No) = ]; check again")
        Snak_YN = str(input("Do you want any snack (Yes/No) = ")).upper()
        print("-"*50,"\n")

#Collect and Store Ticket Details

print("-"*50,"")
Ticket_count = int(input("Enter Ticket Count = "))

Ticket_categery = []
Ticket_price = []
S_number =[]

for k in range (Ticket_count):
    Ticket_cate = str(input("\nEnter Ticket categary (VIP/Standard/Premium) = ")).upper()
    while True:
        if Ticket_cate in ("VIP","STANDARD","PREMIUM"):
            break
        else:
            print("-"*50,"")
            print("Invalid answer for [ Enter Ticket categary ]; check again")
            Ticket_cate = str(input("Enter Ticket categary (VIP/Standard/Premium) = ")).upper()
            print("-"*50,"\n")
    Seat_no = int(input("Enter Seat number = "))

    Ticket_categery.append(Ticket_cate)
    S_number.append(Seat_no)

    if Ticket_cate == "VIP":
        Ticket_price.append(2500)
    elif Ticket_cate == "PREMIUM":
        Ticket_price.append(2000)
    else:
        Ticket_price.append(1500)

print("-"*50,"\n")


# Collect and Store Snack Details
Snak_name = []
Snak_price = []

if Snak_YN == "YES":
    while True:
        sn = str(input("Enter Snak Name = "))
        sp = int(input("Enter Snak price = "))

        Snak_name.append(sn)
        Snak_price.append(sp)

        quest = str(input("Do You want to add another one of snak(y/n) = ")).upper()

        if quest == "N":
            break

#Calculate Ticket Information

sum = 0
max = 0
avg = 0

for i in range(Ticket_count):
    sum = sum + Ticket_price[i]
    if max < Ticket_price[i]:
        max = Ticket_price[i]
        min = Ticket_price[i]

avg = sum/Ticket_count

VIP = Ticket_categery.count("VIP")
STANDARD = Ticket_categery.count("STANDARD")
PREMIUM = Ticket_categery.count("PREMIUM")

#Calculate Discounts

if Ticket_type == 1:
    Discount = (sum/100)* 15
elif Ticket_type == 2:
    Discount = (sum/100)* 10
else:
    Discount = 0

if Ticket_count >= 5:
    G_Discount = (sum/100)*5
else:
    G_Discount = 0

F_Discount = Discount + G_Discount

#Analyse Snack Information
if Snak_YN == "YES":
    Snak_sum = 0
    Most_expensive_Snak = 0
    Least_expensive_Snak = 0
    expensive_snack_count = 0

    for i in range (len(Snak_price)):
        Snak_sum = Snak_sum + Snak_price[i]

        if Most_expensive_Snak < Snak_price[i]:
            Most_expensive_Snak = Snak_price[i]

        if Least_expensive_Snak > Snak_price[i]:
            Least_expensive_Snak = Snak_price[i]

        if Snak_price[i] > 500:
            expensive_snack_count += 1

#Calculate and Classify the Final Bill
if Snak_YN == "YES":
    Total_Bill = (sum - F_Discount) + Snak_sum
else:
    Total_Bill = (sum - F_Discount)


if Total_Bill >= 10000:
    Booking = "Large"
elif Total_Bill >= 5000:
    Booking = "Regular"
else:
    Booking = "Small"

m = "Ticket_categery"
n = "Seat_no"
o = "Ticket_price"
print("-"*50,"\n")
print("-"*50)
print("BILL NO: 80085")
print("-"*50,"\n")

print("\n","-"*50)
print(f"|{m:^15}|{n:^15}|{o:^15}|")
print("-"*50)

for i in range (Ticket_count):
    print(f"|{Ticket_categery[i]:^15}|{S_number[i]:^15}|{Ticket_price[i]:^15}|")
print("-"*50,"\n")

p = "Snak_name"
q = "Snak_price"

if Snak_YN == "YES":
    print("-"*50)
    print(f"|{p:^15}|{q:^15}|")
    print("-"*50)

    for j in range (len(Snak_price)):
        print(f"|{Snak_name[j]:^15}|{Snak_price[j]:^15}|")

    print("-"*50,"\n")


print("-"*50)
print(f"Total Ticket Price = {sum}")  
if Snak_YN == "YES":
    print(f"Total Snack Price = {Snak_sum}")
print(f"Total Discount = {F_Discount}")
print(f"Booking = {Booking}")
print("-"*50,"\n")


print("-"*50)
print(f"\nTotal Bill = {Total_Bill}")
print("-"*50,"")

input()
