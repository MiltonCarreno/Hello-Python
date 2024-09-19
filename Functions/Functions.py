import math

def areaCircle(radius):
    return math.pi * radius * radius

def taxRate(money, tax):
    tax = tax / 100
    return money + (money * tax)

def tempCalc(f_temp):
    return (f_temp - 32) * (5/9)

radius = int(input("Enter radius: "))
print(f"Area of circle is {areaCircle(radius):.2f}")

money = int(input("Enter Money: "))
tax = int(input("Enter Tax: "))
print(f"Total is {taxRate(money, tax)}")

f_temp = int(input("Enter Fahrenheit: "))
print(f"The temperature in Celsius is {tempCalc(f_temp):.6}")