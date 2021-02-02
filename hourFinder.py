fname = input("Enter file name: ")
fhandle = open(fname)
time = []
hr_freq = dict()
for line in fhandle :
    if line.startswith("From") :
        if not line.startswith("From:") :
            words = line.split()
            time.append(words[5])
print(time)
hr = []
for i in time :
    a = i.split(':')
    hr.append(i[0:2])
ordered_hr = sorted(hr)

for i in ordered_hr :
    hr_freq[i] = hr_freq.get(i,0) + 1
print(hr_freq)

for k, v in hr_freq.items() :
    print(k, v)
