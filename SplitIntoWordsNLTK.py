#load text
filename='metamorphosis_clean.txt'
file=open(filename,'rt')
text=file.read()
file.close()

#Split into words, punctuations will also be considered as words here
from nltk.tokenize import word_tokenize
tokens = word_tokenize(text)
print(tokens[:100])
