from textblob import TextBlob

bios = [
    "I absolutely love meeting new people and exploring events!",
    "This event was terrible and poorly organized.",
    "It was okay, not too bad but not great either.",
    "Amazing experience! Would definitely join again.",
    "I didn't like the crowd, felt uncomfortable."
]

print("\nSentiment Analysis Results:\n")

for bio in bios:
    blob = TextBlob(bio)
    print(f"Text: {bio}")
    print(f"Polarity: {blob.sentiment.polarity}")
    print(f"Subjectivity: {blob.sentiment.subjectivity}")
    print("-" * 50)