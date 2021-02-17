## this function prompts the user for a number, then lists all divisors of that number.

def Divisors():
    
    user_num = int(input('Enter an integer: '))
    divisor_list = []
    
    for i in range(1, user_num+1):
        if user_num % i == 0:
            divisor_list.append(i)
    print(divisor_list)
    
    
Divisors()