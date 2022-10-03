result = 0
number = 1
while number > 0:
    number = int(input("Enter a number[enter a (-) value to exit]: "))
    if number < 0:
        print("Exiting")
    else:
        result = result + number
        print(result)
print("Bye!")