import pickle
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

nltk.download('stopwords')

#load the model and countvectorizer
with open('chatDjango/classifier.pkl', 'rb') as model_file:
    classifier = pickle.load(model_file)
with open('chatDjango/count_vectorizer.pkl', 'rb') as vectorizer_file:
    cv = pickle.load(vectorizer_file)

def preprocess_message(message):
    message = re.sub('[^a-zA-Z]', ' ', message)
    message = message.lower()
    message = message.split()
    ps = PorterStemmer()
    all_stopwords = stopwords.words('english')
    all_stopwords.remove('not')
    message = [ps.stem(word) for word in message if not word in set(all_stopwords)]
    message = ' '.join(message)
    return message

def predict_sentiment_message(message):
    message = preprocess_message(message)
    X_new =cv.transform([message]).toarray()
    return classifier.predict(X_new)

