from sklearn.feature_extraction.text import CountVectorizer
import numpy as np

#function to calculate cosine similarity between two vectors
def cosine_similarity(v1, v2):
    return np.dot(v1, v2) / (np.sqrt(np.dot(v1, v1)) * np.sqrt(np.dot(v2, v2)))

# Read the input file
with open('doc1.txt', 'r') as f:
    doc1 = f.read()

with open('doc2.txt', 'r') as f:
    doc2 = f.read()

#create a vectorizer object
vectorizer = CountVectorizer()

#build a vocabulary of words from the documents
vectorizer.fit([doc1, doc2])

print("Vocabulary: ", vectorizer.vocabulary_)

#transform the documents to vectors
doc1_vector = vectorizer.transform([doc1])
doc2_vector = vectorizer.transform([doc2])

print("doc1_vector: ", doc1_vector.toarray())
print("doc2_vector: ", doc2_vector.toarray())

#calculate cosine distance between the two vectors
print("Cosine distance: ", 1 - cosine_similarity(doc1_vector.toarray()[0], doc2_vector.toarray()[0]))
