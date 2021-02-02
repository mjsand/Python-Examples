# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fhandle = open(fname)
count = 0
a = []  #empty list to store spam values in
for line in fhandle :
    if line.startswith("X-DSPAM-Confidence:") :
        count = count + 1           # counting number of lines with spam value
        #print(line)
        spam_value = float(line[20:26])    # declaring variable to represent float of spam values
        a.append(spam_value)        # creating list a of spam values

#print(count)
#print(a)
x = 0               # declaring variable x to start the summation of values in a
for i in a :        # creating a loop that will add the values of a together
    x += i          # command that states that x is equal to the summed values of i
#print(x)
avg_spam_value = x / count          # finding the mean of all the values in a
print('Average spam confidence:', avg_spam_value)
