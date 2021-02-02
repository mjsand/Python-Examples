balls = [('red', 5), ('blue', 2), ('yellow', 3), ('green', 1), ('orange', 2), ('black', 2)]
def fillBag(balls):
    global bag
    bag = dict(balls) 
    return bag
   
    
def totalBalls():
    total = sum(bag.values())
    
    return total
    
def probOf():
    color = input('Enter a color: ')
    prob =  bag[color] / totalBalls()
    return prob
    
def probAll():
    probDict = {}
    for color in bag:
        probDict[color] = bag[color] / totalBalls()
    
    return probDict
    
fillBag(balls)
print(fillBag(balls))
totalBalls()
print(totalBalls())
print(probOf())
probAll()
print(probAll())