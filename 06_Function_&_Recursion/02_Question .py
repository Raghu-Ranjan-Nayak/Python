#Write a function to print factorial of n
def fact(n):
    fact = 1 
    while n >= 1:
        fact *= n
        n -= 1
    print(fact)

fact(5)