from random import randrange

def randomNumberGame():
    
    n = randrange(100)
    count = 0
    
    while True:
        
        try: 
            guess = int(input('Enter a number:'))
            count += 1
        except ValueError:
            print('Error: Please enter an integer.')
            continue
        
        if guess == n :
            print('Congratulations! You won in', count, 'guesses.')
            break
        
        elif guess < n :
            print ('Not quite. Try a bigger number.')
        elif guess > n :
            print('Not quite. Try a smaller number.')
            
randomNumberGame()