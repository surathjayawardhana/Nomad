#A supermarket sells 10 different items. Each item has an item code, item name, and price. 
#Using an appropriate data structure, write a program to store the information given below.4

item_code = ['ITM001','ITM002','ITM003','ITM004','ITM005','ITM006','ITM007','ITM008','ITM009','ITM010']
item_name = ['Rice','Sugar','Milk Powder','Bread','Eggs','Butter','Tea','Cooking Oil','Soap','Shampoo']
price = [250.00,280.00,1450.00,180.00,520.00,780.00,650.00,950.00,220.00,890.00]

#   The supermarket requires a system to automate its billing process. 
#   When the cashier scans or enters an item code using the barcode machine, the system should: 
# 1. Ask the cashier to enter the quantity. 
# 2. Find the relevant item name and unit price. 
# 3. Calculate the total price of the selected item. 
# 4. Allow the cashier to enter multiple items. 
# 5. Calculate the final bill amount. 
# 6. Display the bill with the item code, item name, quantity, unit price, and total price.
total = 0
ic = []
iname = []
q = []
up = []
while True:
    scan = str(input("Getting Input from Barcode Scaner: "))
    x = 0
    for i in range(10):
        if scan == item_code[i]:
            x = i
            break
    quantity = float(input(f"Enter Quantity of {item_name[x]}: "))
    temp_price = quantity*price[x]
    print(f"\nPrice for {quantity} of {item_name[x]} is {temp_price}")
    total = total + temp_price
    ic.append(item_code[x])
    q.append(quantity)
    up.append(price[x])
    iname.append(item_name[x])
    
    countmeout = str(input("Do you want to add another item (y/n):"))
    print("\n")
    print("*" * 55,"\n")
   

    if countmeout == "n" or countmeout == "N":
        print("-" * 55,"\n")
        print(f"{'Code':<8}{'Item':<20}{'Qty':>5}{'Price':>10}")
        print("-" * 55,"\n")

        for j in range(len(ic)):
            print(f"{ic[j]:<8}{iname[j]:<20}{q[j]:>5}{up[j]:>10}")
        
        print("-" * 55,"\n")

        print(f"\nTotal Price = LKR {total}")
        input()
        break

