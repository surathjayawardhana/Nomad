Engin =[1,2,3,4]

Engin[0] = int(input("Enter Engin 01 Temp: "))
Engin[1] = int(input("Enter Engin 02 Temp: "))
Engin[2] = int(input("Enter Engin 03 Temp: "))
Engin[3] = int(input("Enter Engin 04 Temp: \n"))

j=1
safe = 0
nm = 0

for i in range (4):
    if 200 < Engin[j] < 850:
        print(f"Engin {j}: Safe")
        safe = safe + 1
        j=j+1
    else:
        print(f"Engin {j}: Maintenance Required")
        nm = nm+1
        j=j+1

print(f"\nSafe Engines = {safe}")
print(f"Maintenance Required = {nm}")
input()

