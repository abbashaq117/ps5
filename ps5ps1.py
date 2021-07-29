def comptotal(qty, price):
    total = qty * price
    if total > 10000:
        total = total * 0.9
    else:
        total = total
    
    return total

# Main
print("Please enter the qty")
qty = float(input())
print("Please enter the price")
price = float(input())
comptotal(qty, price)
total = comptotal(qty, price)
print(total)
