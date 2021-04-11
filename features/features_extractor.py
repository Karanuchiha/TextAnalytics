from type_token_ratio import type_token_ratio
from l2_syntactic_complexity_analyzer import l2_syntactic_complexity_analyze_text
from readability_scores import get_flesch_reading_ease, get_smog_index, get_flesch_kincaid_grade
from lca_and_readability_scores.lca.postag_lemm_lca import get_lexical_complexity_analysis_sanitized
import nltk
import json
from nltk.stem import WordNetLemmatizer

nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')
lemmatizer = WordNetLemmatizer()

def extract_features_from_text(text):
    response = dict()

    l2sca = l2_syntactic_complexity_analyze_text(text)

    # type token ratio
    response['ttr'] = type_token_ratio(text)

    # l2sca scores
    response['l2sca'] = l2sca
    response['words_per_t_unit'] = l2sca['W']/l2sca['T']
    response['words_per_clauses'] = l2sca['W']/l2sca['C']

    # readability scores
    response['flesch_reading_ease'] = get_flesch_reading_ease(text)

    # lca
    response['lca'] = get_lexical_complexity_analysis_sanitized(text, lemmatizer)

    return response

text = ("Playing games has always been thought to be important to "
    "the development of well-balanced and creative children; "
    "however, what part, if any, they should play in the lives "
    "of adults has never been researched that deeply. I believe "
    "that playing games is every bit as important for adults "
    "as for children. Not only is taking time out to play games "
    "with our children and other adults valuable to building "
    "interpersonal relationships but is also a wonderful way "
    "to release built up tension.")

# response = extract_features_from_text(text)
# print(response)