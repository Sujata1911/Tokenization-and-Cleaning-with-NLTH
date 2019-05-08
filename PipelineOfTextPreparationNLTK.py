#load text
filename = 'metamorphosis_clean.txt'
file = open(filename,'rt')
text = file.read()
file.close()

#split into words
from nltk.tokenize import word_tokenize
tokens = word_tokenize(text)

#convert into lowercase
tokens = [w.lower() for w in tokens]

#remove punctuation from each word
import string
table = str.maketrans('','',string.punctuation)
stripped = [w.translate(table) for w in tokens]

#remove remaining tokens that arent alphabetic
words = [word for word in stripped if word.isalpha()]

#filter out stopwords
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))
words = [w for w in words if not w in stop_words]
print(words[:100])
