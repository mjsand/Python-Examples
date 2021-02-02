score = input("Enter Score: ")

try :
    sc = float(score)

except :
    print("Error: Value must be between 0.0 and 1.0.")
    quit()

def check_grade() :

    if sc > 1 :
        print("Error: Score cannot be greater than 1.0.")
    elif sc < 0 :
        print("Error: Score cannot be lower than 0.")
    elif sc >= 0.9 :
    	print("A")
    elif sc >= 0.8 :
        print("B")
    elif sc >= 0.7 :
        print("C")
    elif sc >= 0.6 :
        print("D")
    elif sc < 0.6 :
        print("F")


check_grade()
