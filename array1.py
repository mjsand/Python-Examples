cars = ['chevy', 'dodge', 'ford', 'toyota']
name = 'gabby'
name2 = name[::2]
print(name2)

cars2 = cars[::2]
print(cars2)


numbers = [3, 7, 13, 1, 9, 0, 52, 27]
numbers.sort(key = abs, reverse=True)
print(numbers)

list = []
n = int(input('Enter number of players: '))
for i in range(0, n) :  #creating range of players, prompting user for their names, and then entering them into an array
    ele = (input('name: '))
    list.append(ele)

print(list)
