number = int(number) * int(number)

result = 1
number = 1
while number > 0:
    number = int(input("Enter number: "))
    exponent = int(input("Enter exponent: "))
    print(f'{number} raised to {exponent} is {result}')
    if number < 0:
        result = result * number
print("Bye!")

