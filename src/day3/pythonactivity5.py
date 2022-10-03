name = input("Enter name: ")
grade1 = input("Enter grade in Physics: ")
grade2 = input("Enter grade in Algebra: ")
grade3 = input("Enter grade in Programming: ")
average = ((float(grade1)+float(grade2)+float(grade3)) / 3)
print(f'{name} average grade is {average}')

if average < 78:
    print("Failure")
elif 78 <= average <= 82:
    print("Fair")
elif 83 <= average <= 88:
    print("Average Student")
elif 89 <= average <= 94:
    print("Dean Lister")
elif 95 <= average <= 100:
    print("President Lister")
else:
    print("Invalid grade")
