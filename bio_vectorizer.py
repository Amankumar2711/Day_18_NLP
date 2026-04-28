from sklearn.feature_extraction.text import TfidfVectorizer
from text_cleaner import clean_bio

bios = [
    "Expert in Python and Machine Learning for social good.",
    "Professional Chef who loves outdoor Hiking and mountains.",
    "Machine Learning enthusiast and mountain hiker."
]

# Clean bios first
cleaned_bios = [clean_bio(bio) for bio in bios]

vectorizer = TfidfVectorizer()

tfidf_matrix = vectorizer.fit_transform(cleaned_bios)

print("\nVocabulary:\n", vectorizer.get_feature_names_out())
print("\nTF-IDF Matrix Shape:", tfidf_matrix.toarray().shape)

print("\nTF-IDF Matrix:\n", tfidf_matrix.toarray())