#Getting_input

sales = float(input("Enter Sales 1: "))
max = sales

sano = 2

for i in range (9):
    sales = float(input(f"Enter Sales {sano}: "))
    if (sales>max):
        max = sales
    sano = sano+1

print(f"Maximum is {max}")


input()