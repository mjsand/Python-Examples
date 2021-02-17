## this function asks the user for a long string containing multiple words, and returns the string back but in reverse order.

def Reverse_Word_Order(sentence):
    
    print(sentence)
    words = sentence.split(' ')
    reversed_sentenced = ' '.join(words[::-1])
    print(reversed_sentenced)
    
Reverse_Word_Order('My name is Jimmy and I like dogs')
