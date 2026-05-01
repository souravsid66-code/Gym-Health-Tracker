"""Generate prime number list using lower and uper limit"""
lower = int(input("Enter the lower number: "))
upper = int(input("Enter the upper number: "))

for num in range(lower, upper + 1):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num)
