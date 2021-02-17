## generates fibonacci numbers according to user input
def Fibonacci(user_input):
    
    n1 = 1
    n2 = 1
    fib = []
    count = 0
    while count < user_input:
        fib.append(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1
        
    print(fib)
              
user_input = int(input('Enter the number of fibonacci numbers you would like to generate: '))
Fibonacci(user_input)