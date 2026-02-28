num = int(input("Enter a non-negative integer: "))

if num == 0:
    print("Factorial of 0 is 1")
else:
    factorial = 1
    for i in range(1, num + 1):
        factorial *= i
    print("Factorial of {} is {}".format(num, factorial))
