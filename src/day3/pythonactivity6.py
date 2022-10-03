number = int(input("Enter number: "))
exponent = int(input("Enter exponent: "))

ctr = exponent
while ctr <= int(exponent):
    result = number ** exponent
    print(f'{number} raised to {exponent} is {result}')
    ctr += 1


