credit = True
price = 10000000
if credit:
    print("put 10% down")
    down_payment = 0.10 * price
else:
    print("put 20% down")
    down_payment = price * 0.20
print(f"Down Payment: ${down_payment}")
