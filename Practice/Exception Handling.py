# Handling DivisionError using try-except block
def safe_divide(numerator,denominator):
    try:
        result = numerator/denominator
        return result
    except ZeroDivisionError:
        print("Error: Cannot Divide by Zero.")
        return None
#Test Case
numerator=int(input("Enter the numerator:"))
denominator=int(input("Enter the denominator:"))
print(safe_divide(numerator,denominator))

