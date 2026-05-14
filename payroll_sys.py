#payroll_system
import math

b = float(input("Enter the basic salary: "))
nd = int(input("Enter the number of days worked: "))
eh = int(input("Enter the number of extra hours worked: "))
print("\nCalculating payroll...")
par = (5 / 100)
exh = 250
tax = (12/100)

Total_salary = b + (nd * (b*par)) + (exh*eh)
Tax_amount = Total_salary * tax
Net_salary = Total_salary - Tax_amount

print("\nTotal Salary: ", Total_salary)
print("Tax Amount: ", Tax_amount)
print("Net Salary: ", Net_salary)
input("\nPress Enter to exit...")