fname = input("Enter file name: ") #prompt user for txt file name
fhandle = open(fname)   #store text file as a handle
inp = fhandle.read()    #read file handle and store as variable
upper_inp = inp.upper() #convert all text in variable 'inp' to all uppercase
final = upper_inp.rstrip() #strip off extra line spaces inside text
print(final)
