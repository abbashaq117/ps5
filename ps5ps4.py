def jobcode(code):
    if code == "L":
        pay = 25
    else:
        if code == "A":
            pay = 30
        else:
            if code == "J":
                pay = 50
    
    return pay

# Main
print("Please enter your lastname")
lastname = input()
print("Please enter your jobcode L(25), A(30),J(50)")
jobCode = input()
print("Please enter hours worked")
hw = float(input())
rate = jobcode(jobCode)
print(lastname + " Worked this many hours: " + str(hw) + " and made this much:  " + str(rate * hw))
