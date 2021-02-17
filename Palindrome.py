## this function reads a string input from the user, and determines whether it is a palindrome

def palindrome():
    
    word = input('Enter a word: ').lower()
    reverse_word = word[::-1]
    
    if word == reverse_word:
        print('Yes,', word, 'is a palindrome.')
        
    else:
        print('No,', word, 'is not a palindrome.')
        
palindrome()