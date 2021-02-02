with open('members.txt', 'r+') as writeFile :
    with open('inactive.txt', 'a+') as appendFile :
        writeFile.seek(0)               ###starting at the zero point in the txt file
        members = writeFile.readlines()  ### creating list members for lines of text 
        inactive = appendFile.readlines()
        header = members[0]                 ### setting the headers as the first element in members
        members.pop(0)                  ### removing headers from members
        
        for member in members :
            if 'no' in member :
                inactive.append(member)
        
                
        writeFile.seek(0)
        writeFile.write(header)
        for member in members :
            if member in inactive :
                appendFile.write(member)
            else :
                writeFile.write(member)
            
        
        writeFile.truncate()