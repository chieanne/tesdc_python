numbers = []
ctr = 0
while ctr < 2:
    num = int(input(f"Enter number {ctr+1}: "))
    numbers.insert(ctr, num)
    ctr += 1
print("Loop Done")

# display list value
print("Displaying input")
print(numbers)