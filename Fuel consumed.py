# getting inputs 
distance = float(input("Enter the distance traveled (in km): "))
fuel_efficiency = float(input("Enter the fuel efficiency of the vehicle (in km per liter): "))
fuel_price = float(input("Enter the price of fuel per liter: "))
highway_chargers = float(input("Enter the cost of highway chargers: "))

# calculating fuel consumed

print("\nCalculating fuel consumption and total cost...")
fuel_consumption = distance / fuel_efficiency
fuel_cost = fuel_consumption * fuel_price
total_cost = fuel_cost + highway_chargers

# displaying the result
print(f"\nFuel consumed: {fuel_consumption:.3f} liters")
print(f"Total fuel cost: LKR. {fuel_cost:.3f}")
print(f"Total cost including highway chargers: LKR. {total_cost:.3f}")

#This will hold the console open until the user presses Enter, allowing them to see the results before exiting.
input("\nPress Enter to exit...")