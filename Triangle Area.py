# Triangle Area
print("Triangle Area")
print("What is the type of triangle?")
print("1. Right-angled triangle")
print("2. Equilateral triangle")
print("3. Isosceles triangle")
print("4. Scalene triangle (all three side known)")
input_type = int(input("Enter the number corresponding to the triangle type: "))
if input_type == 1:
    print("Right-angled triangle")
    print("Enter the base and height of the triangle:")
    base = float(input("Base: "))
    height = float(input("Height: "))
    area = 0.5 * base * height
elif input_type == 2:
    print("Equilateral triangle")
    side = float(input("Enter the length of one side: "))
    area = (side ** 2 * (3 ** 0.5)) / 4
elif input_type == 3:
    print("Isosceles triangle")
    equal = float(input("Enter the length of the equal sides:"))
    different = float(input("Enter the length of the different side: "))
    if(different >= equal):
        print("Invalid input, the different side must be less than the equal sides.")
        exit()
    # Using Pythagorean theorem to calculate height
    # h^2 + (d/2)^2 = e^2
    height = (equal ** 2 - (different / 2) ** 2) ** 0.5
    area = (different * height) / 2
elif input_type == 4:
    print("Scalene triangle")
    a = float(input("Enter side a: "))
    b = float(input("Enter side b: "))
    c = float(input("Enter side c: "))
    if a + b <= c or a + c <= b or b + c <= a:
        print("Invalid input, the sum of any two sides must be greater than the third side.")
        exit()
    # Using Heron's formula to calculate area
    s = (a + b + c) / 2
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
else:
    print("Invalid input, please enter a number between 1 and 4.")
    exit()
print(f"The area of the triangle is: {area}")
print()