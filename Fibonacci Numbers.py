terms = int(input("Enter a number up to how many terms you want the Fibonacci Numbers : "))


def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


if terms <= 0:
    print("Please enter a positive number rather than 0.")
else:
    print("The Fibonacci numbers : ", end=" ")
    for i in range(terms):
        print(fibonacci(i), end=" ")
