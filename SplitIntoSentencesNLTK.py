#load text
filename='metamorphosis_clean.txt'
file=open(filename,'rt')
text=file.read()
file.close()

#split into sentences
from nltk import sent_tokenize
sentences = sent_tokenize(text)
print(sentences[1])
