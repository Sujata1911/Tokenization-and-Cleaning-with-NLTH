#load data
filename = 'metamorphosis_clean.txt'
file = open(filename,'rt')
text=file.read()
file.close()

#split into words
from nltk.tokenize import word_tokenize
tokens = word_tokenize(text) #equivalent to split()
#print(tokens[:100])
#from nltk import sent_tokenize
#sentences = sent_tokenize(text)
#print(sentences[:50])

#convert to lowercase
tokens = [w.lower() for w in tokens]

#remove punctuations from each word
import string
table = str.maketrans('','',string.punctuation)
stripped = [w.translate(table) for w in tokens]

#filter out punctuations
#remove remaining tokens that are not alphabetic
words = [word for word in stripped if word.isalpha()]
print(words[:100])

#filter out stopwords
#NOTE: 
#"from nltk.corpus import stopwords
#stop_words = stopwords.words('english')
#print(stop_words)"
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))
woords = [w for w in words if not w in stop_words]
print(words[:100])
