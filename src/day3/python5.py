# age test 5
age = int(input("Enter your age: "))

if 0 <= age <= 12:
    print("Child")
elif 13 <= age <= 17:
    print("Young Adult")
elif 18 <= age <= 59:
    print("Adult")
elif 60 <= age <= 100:
    print("Senior")
else:
    print("invalid age!")
print("Goodbye!")