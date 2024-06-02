# return fabonacci series of n numbers
def fibonacci(n):
    a = 0
    b = 1
    if n == 1:
        print(a)
    else:
        print(a)
        print(b)
        for i in range(2, n):
            c = a + b
            a = b
            b = c
            print(c)

user_choice = int(input("Enter any number from 1 to 100 to get fibnacci: "))
fibonacci(user_choice)
print("Thank you for using the fibonacci series generator!")