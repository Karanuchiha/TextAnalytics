## Lexical Complexity Analyzer

`$> python3 postag-lemm-lca.py input.txt`

1. Implicit POS-Tagging + Lemmatization
2. Lexical Complexity Analyzer

Output:

```
[nltk_data] Downloading package averaged_perceptron_tagger to
[nltk_data]     /Users/boris/nltk_data...
[nltk_data]   Package averaged_perceptron_tagger is already up-to-
[nltk_data]       date!
[nltk_data] Downloading package wordnet to /Users/boris/nltk_data...
[nltk_data]   Package wordnet is already up-to-date!
{'wordtypes': 76, 'swordtypes': 36, 'lextypes': 69, 'slextypes': 36, 'wordtokens': 104, 'swordtokens': 55, 'lextokens': 94, 'slextokens': 55, 'ld': '0.90', 'ls1': '0.59', 'ls2': '0.47', 'vs1': '0.23', 'vs2': '0.69', 'cvs1': '0.59', 'ndw': 76, 'ndwz': 41, 'ndwerz': '42.90', 'ndwesz': '42.10', 'ttr': '0.73', 'msttr': '0.80', 'cttr': '5.27', 'rttr': '7.45', 'logttr': '0.93', 'uber': '29.87', 'lv': '0.73', 'vv1': '0.85', 'svv1': '9.31', 'cvv1': '2.16', 'vv2': '0.12', 'nv': '0.69', 'adjv': '0.15', 'advv': '0.01', 'modv': '0.16'}
```

## Readability Scores

`$> python3 readability-scores.py`
