class TextAnalyzer(object):
    
    def __init__ (self, text):
        # remove punctuation
        no_punct_text=text.replace(",","").replace(".","").replace("!","").replace("?","")
        
        # make text lowercase
        standard_text=no_punct_text.lower()
        self.standard_text=standard_text
    def freqAll(self):        
        # split text into words
        words=[]
        words=self.standard_text.split()
        # Create dictionary
        freq={}
        for word in words:
            freq[word]=words.count(word)
        return freq
    def freq(self,word):
        Dic=self.freqAll()
        if word in Dic:
            print(Dic[word])
        else:
            print(0)