fname = input("Enter file name: ")
fhandle = open(fname)
list = []
senders = dict()
for line in fhandle :
    if line.startswith("From") :
        if not line.startswith("From:") :
            words = line.split()
            list.append(words[1])
for name in list :
    senders[name] = senders.get(name,0) + 1

maxcount = None
maxsender = None
for sender,count in senders.items() :
    if maxcount is None or maxcount  < count :
        maxsender = sender
        maxcount = count
print(maxsender, maxcount)
print(senders)
print(list)