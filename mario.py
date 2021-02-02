def mario():
    while True:
        num = input('Enter a number between 1 and 8: ')
        try :
            num = int(num)
        except ValueError :
            print('Error: Entry must be an integer.')
            continue
        if int(num) < 1 or int(num) > 8 :
            print('Error: Entry must be between 1 and 8.')
            continue
        else :
            break
    for i in range(0, num) :
        print(" " * (num-i),'#' * (i+1))

mario()
