"""Check the largest number among three numbers entered by the user."""
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

if num1 >= num2 and num1 >= num3:
    print(f"{num1} is the largest")
elif num2 >= num1 and num2 >= num3:
    print(f"{num2} is the largest")
else:
    print(f"{num3} is the largest")
