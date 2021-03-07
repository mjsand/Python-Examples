## this function searches a word bank or text file for the specified word, letter, or character and returns the number of occurrences

def Word_Search(file):
    
    file_handle = open(file)
    words = file_handle.read().lower().split()
    print(words)
    user_word = input('Enter the word you seek: ')
    count = 0
    word_pos = []
    for word in words:
        if user_word == words[word]:
            count += 1
            indx = words.index(word)
            word_pos.append(indx)
            
    print(count)
    print(word_pos)
    
    
Word_Search('mbox-short.txt')