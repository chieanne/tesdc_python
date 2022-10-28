name = []
numbers = []

ctr = 0
while ctr < 5:
    nam = input(f"Enter athlete {ctr + 1}: ")
    num = int(input(f"Enter sales {ctr + 1}: "))
    name.insert(ctr, nam)
    numbers.insert(ctr, num)
    ctr += 1

total = 0
for ele in range(0, len(numbers)):
    total = total + numbers[ele]




print(name)
print(numbers)

print(f'Total Sales: {total}')