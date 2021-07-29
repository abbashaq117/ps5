def distirctCode(district):
    if district == "I":
        credit = 250
    else:
        if district == "O":
            credit = 500
    
    return credit

# Main
print("Please enter lastName")
lastname = input()
print("Please enter credit hours")
credit = float(input())
print("Please enter district code I=(250) O=(550)")
district = input()
tuition = distirctCode(district)
print(lastname + "owed" + str(tuition))
