# Assessment Question 1 – Pharmacy Management System

# A pharmacy sells 10 different medicines. Each medicine has a medicine code, medicine name, and unit price. 
# Using an appropriate data structure, write a program to store the information given below.
# The pharmacy requires a system to automate its billing process. When the pharmacist scans or enters a medicine code, 
# the system should:

## Ask the pharmacist to enter the quantity. 
## Find the corresponding medicine name and unit price. 
## Calculate the total price of the selected medicine. 
## Allow the pharmacist to enter multiple medicines. 
## Calculate the final bill amount. 
## Display the bill showing the medicine code, medicine name, quantity, unit price, and total price.

Medicine_code = ["MED001","MED002","MED003","MED004","MED005","MED006","MED007","MED008","MED009","MED010",]
Medicine_name = ["Paracetamol","Vitamin C","Cough Syrup","Antacid","Pain Relief Gel","Face Mask Pack","Hand Sanitizer","Bandage Roll","Antibiotic Cream","Digital Thermometer"]
Price = [120,450,780,350,920,180,520,250,680,2150]

total = 0
ic = []
iname = []
q = []
up = []

while True:
    scan = str(input("Getting Input from Barcode Scaner: "))
    x = 0
    for i in range(10):
        if scan == Medicine_code[i]:
            x = i
            break
    quantity = float(input(f"Enter Quantity of {Medicine_name[x]}: "))
    temp_price = quantity*Price[x]
    print(f"\nPrice for {quantity} of {Medicine_name[x]} is {temp_price}")
    total = total + temp_price
    ic.append(Medicine_code[x])
    q.append(quantity)
    up.append(Price[x])
    iname.append(Medicine_name[x])
        
    countmeout = str(input("Do you want to add another item (y/n):"))
    print("\n")
    print("*" * 55,"\n")
    

    if countmeout == "n" or countmeout == "N":
        print("-" * 55,"\n")
        print(f"|{'Code':<8}|{'Item':<20}|{'Qty':>5}|{'Price':>10}|")
        print("-" * 55,"\n")

        for j in range(len(ic)):
            print(f"|{ic[j]:<8}|{iname[j]:<20}|{q[j]:>5}|{up[j]:>10}|")
            
        print("-" * 55,"\n")

        print(f"\nTotal Price = LKR {total}")
        input()
        break