product = input("Enter product: ")
price = float(input("Enter price: "))

if 0 <= price <= 10000:
    print("No Discount")
elif 10001 <= price <= 20000:
    print(f'Discount is {(price) * (0.05)}')
    print(f'Net Price is {(price) - ((price) * (0.05))}')
elif 20001 <= price <= 50000:
    print(f'Discount is {(price) * (0.10)}')
    print(f'Net Price is {(price) - ((price) * (0.10))}')
elif 50001 <= price <= 100000:
    print(f'Discount is {(price) * (0.15)}')
    print(f'Net Price is {(price) - ((price) * (0.15))}')
else:
    print(f'Discount is {(price) * (0.20)}')
    print(f'Net Price is {(price) - ((price) * (0.20))}')
print("Happy Shopping!")
