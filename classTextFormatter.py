class analysedText(object):
    
    ### formatting text input to prepare for dictionary
    def __init__ (self, text):
        formattedText = text.lower().replace('.', '').replace('!', '').replace(',', '').replace('?', '').replace("'", "")
        self.fmtText = formattedText     
    
    
    ### creating a list from previous formatted text, then putting that list into a dictionary
    def freqAll(self):        
        wordList = self.fmtText.split()
        wordDict = dict()
        for word in wordList:
            wordDict[word] = wordDict.get(word,0) + 1
        return wordDict   
     

    ### giving frequency of any given word       
    def freqOf(self,word):
        freqDict = self.freqAll()
        if word in freqDict:
            return freqDict[word]
        else:
            return 0


### in the sample text field between ' ', paste your text. replace words 'balls' with any word you want to compute the frequency of.
        
SampleText = analysedText('Jimmy cracked corn and I dont care. Jimmy sucked a bing bong and I dont care. Jimmy ate a dog and shat in the hat on the cat by the mat. The End.')
#SampleText2 = analysedText(input('Enter the name of your text file: '))
print(SampleText.freqAll())   
print(SampleText.freqOf('balls'))   