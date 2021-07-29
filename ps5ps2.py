def comp(bats, key):
    average = float(bats) / key
    
    return average

# Main
print("Please enter your last name")
lastname = input()
print("Please enter number of hits")
bats = int(input())
print("Please enter bats at the keyboard")
key = int(input())
average = float(bats) / key
print(lastname + "'s batting average is " + str(average))
