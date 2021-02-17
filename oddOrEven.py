## determine whether user input number is odd or even

def Even_or_Odd(num):
    while True:
        if num < 0:
            print('Error. Please enter a positive number')
            break
    
        if num % 2 == 0:
                print('Even')
                break
        else :
                print('Odd')
                break

Even_or_Odd(5)