import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import string

# Download resources (only first time)
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

lemmatizer = WordNetLemmatizer()

def clean_bio(text):
    # Lowercase
    text = text.lower()

    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))

    # Tokenize
    tokens = word_tokenize(text)

    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    filtered = [w for w in tokens if w not in stop_words]

    # Lemmatization
    lemmatized = [lemmatizer.lemmatize(word) for word in filtered]

    return " ".join(lemmatized)

# Test
if __name__ == "__main__":
    sample_bio= input()
    
    # sample_bio = "I love Hiking in the mountains and Coding late at night!"
    print("Cleaned Bio:", clean_bio(sample_bio))