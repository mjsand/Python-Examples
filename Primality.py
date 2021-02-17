## this function asks the user for an integer, and determines whether this number is prime or not

def primality():
    
    try: 
        num = int(input('Enter a number to check: '))
        
    except:
        print('That is not a number. Please enter a number.')
        
    for i in range(2, num):
        if num % i != 0:
            print(num, 'is a prime number.')
        else:
            print(num, 'is not a prime number.')
            
primality()
    