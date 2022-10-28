def perimeter(x, y):
    return x + y + x + y
def area(x, y):
    return x * y

num1 = int(input("Enter length: "))
num2 = int(input("Enter width: "))

result1 = perimeter(num1, num2)
result2 = area(num1, num2)
print(f"Perimeter is {result1}")
print(f"Area is {result2}")