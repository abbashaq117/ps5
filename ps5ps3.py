def cost(miles, gallons):
    costofgallon = gallons * 2.5

# Main
print("Enter what city your going to")
city = input()
print("Enter the miles traveled")
miles = float(input())
print("Enter gallons used")
gallons = float(input())
costg = gallons * 2.5
print("Your city is: " + city + "miles traved are: " + str(miles) + "and amount paied for gallons is: " + str(costg))
