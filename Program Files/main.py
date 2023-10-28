from sklearn.datasets import load_files
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pandas as pd

# Load dataset
fake_news = load_files(r"D:\Downloads\FakeNewsDataset")
X, y = fake_news.data, fake_news.target

# Convert labels to binary class labels (0 and 1)
y = [0 if i == b'real' else 1 for i in y]

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# CountVectorizer for feature extraction
count_vect = CountVectorizer()
X_train_counts = count_vect.fit_transform(X_train)
X_test_counts = count_vect.transform(X_test)

# TfidfTransformer for weighting features
tfidf_transformer = TfidfTransformer()
X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)
X_test_tfidf = tfidf_transformer.transform(X_test_counts)

# Multinomial Naive Bayes Classifier
clf = MultinomialNB().fit(X_train_tfidf, y_train)

# Predict on test data
y_pred = clf.predict(X_test_tfidf)

# Calculate and print accuracy
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)