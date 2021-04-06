# Adapted from: https://www.geeksforgeeks.org/python-lemmatization-approaches-with-examples/
import sys
import nltk
from nltk.stem import WordNetLemmatizer
nltk.download('averaged_perceptron_tagger')
from nltk.corpus import wordnet

print(sys.stdin)
sentence = 'the cat is sitting with the bats on the striped mat under many badly flying geese'

nltk.download('wordnet')
lemmatizer = WordNetLemmatizer()

def pos_tagger(nltk_tag):
    if nltk_tag.startswith('J'):
        return wordnet.ADJ
    elif nltk_tag.startswith('V'):
        return wordnet.VERB
    elif nltk_tag.startswith('N'):
        return wordnet.NOUN
    elif nltk_tag.startswith('R'):
        return wordnet.ADV
    else:          
        return None


# tokenize the sentence and find the POS tag for each token
pos_tagged = nltk.pos_tag(nltk.word_tokenize(sentence))  

lemmatized_sentence = ""
for word, tag in pos_tagged:
    tagForLemmatize = pos_tagger(tag)
    # if tag is None:
        # if there is no available tag, do nothing
        # lemmatized_sentence += " " + word
    if tagForLemmatize is not None:        
        # else use the tag to lemmatize the token
        lemmatized_sentence += " " + lemmatizer.lemmatize(word, tagForLemmatize) + "_" + tag
  
print(lemmatized_sentence)