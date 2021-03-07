## this function calculates the factorial of a number using recursion

def factorial(num):
    
    fact = 1
    while num > 1:
        fact = fact * num
        num -= 1      
    print(fact)
    
num = 6
factorial(num)