
p = float(input("Enter the principal amount: "))
r = float(input("Enter the rate of interest rate: "))
t = int(input("Enter the number of years: "))
print("************************************************************************************************************")
A = p * (1+ (r/100)) ** (t)

print("\nTotal investment: ", A)
print("Total interest earned: ", A-p)
input("\n\nPress Enter to exit")