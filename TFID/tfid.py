from sklearn.feature_extraction.text import TfidfVectorizer

#dataset1 = [
  #  "I enjoy reading about Machine ",
 #   "I would enjoy tits a walk in the park",
 #   "I was reading tits in the library"
#]

def TFIDF(dataset):
    tfIdfVectorizer=TfidfVectorizer(use_idf=True)
    tfIdf = tfIdfVectorizer.fit_transform(dataset)
    return tfIdf

#print(TFIDF(dataset1).toarray())
