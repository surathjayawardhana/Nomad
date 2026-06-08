print("Hey now Say now\n")

T = int(input("Enter Temperate 'C: "))
H = int(input("Enter Humidity %: "))
W = int(input("Enter Wind Speed Km/h: "))

if H > 80:
    if T > 30:
        if W > 40:
            print("Severe Storm Warning")
        else:
            print("Heavy Rain Expected")
    else:
        print("Cloudy Weather")
else:
    if T > 35:
        print("Heat Wave Alert")
    else:
        print("Normal Weather")

input("Press Enter For Exit")