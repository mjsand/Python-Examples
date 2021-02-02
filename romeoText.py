fname = input("Enter file name: ")
fhandle = open(fname)
list = []
unique_list = []

for line in fhandle :       #iterating through fhandle and splitting each line of text up into separate lists
    a = line.split()        #splitting lines of text file up into elements and storing them in a
    list.append(a)          #appending list with individual elements of a

l0 = list[0]
l1 = list[1]
l2 = list[2]
l3 = list[3]
unique_list = l0 + l1 + l2 + l3     #breaking list[] apart into (4) separate lists, then combining them into one big list
order = sorted(unique_list)         #alphabetically ordering unique_list
final_unique_list = []
for i in order :
    if i not in final_unique_list :         #creating new list with only unique elements
        final_unique_list.append(i)
print(final_unique_list)
