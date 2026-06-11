x=[0,9,8,7,6,5,4,3,2,1]
c = 0
for i in range(10):
    x[i] = int(input(f"Enter your numbers: "))
    c = c+ x[i]

print(f"\nSum = {c}\n")

r=[0,9,8,7,6]
d = 0
for i in range(5):
    r[i] = int(input(f"Enter your numbers: "))

for j in range(5):
    if r[j] > r[0] and r[j] > r[1] and r[j] > r[2] and r[j] > r[3] and r[j] > r[4]:
        d = r[j]

print(f"\nLagest number is: {r[i]}")

input()

