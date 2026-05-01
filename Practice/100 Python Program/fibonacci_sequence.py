"""Create a fibonacci sequence"""
A = 0
B = 1

num = int(input("Enter a number for Fibonacci sequence: "))
if num == 1:
    print(A)

else:
    print(A)
    print(B)
    for i in range(1,num-1):
        C = A + B
        A = B
        B = C
        print(C)
