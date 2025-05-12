def fatorial(n):
    if n<2:
        return 1
    else:
        return n*(fatorial(n-1))
n=int(input("Enter a number: "))
print("the factorial of",n,"is: ",fatorial(n))