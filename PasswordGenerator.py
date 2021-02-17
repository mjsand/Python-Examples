## this function will generate a random password upon user request. It will be a mix of uppercase and lowercase letters, 
## as well as special characters, and numbers.

import string
from random import choices


def Password_generator(char_count):
    
    alpha_lower_string = string.ascii_lowercase
    alpha_upper_string = string.ascii_uppercase
    letters = []
    for i in alpha_lower_string:
        letters.append(i)
    for i in alpha_upper_string:
        letters.append(i)
        
    special_chars_list = ['!', '@', '#', '$', '%', '^', '&', '*', '?']
    
    password_character_size = int(char_count)
    
    char_list = letters + special_chars_list

    password = ''.join(choices(char_list, k=password_character_size))
    print(password)  
    
    
Password_generator(14)