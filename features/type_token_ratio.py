# obtainable by dividing the total number of unique words by the total number of words
def type_token_ratio(text):
    all_words = text.replace(",", "").replace(".", "").replace(";", "").split(" ")
    all_words = [word for word in all_words if word != ""]
    
    unique_words = set()
    for word in all_words:
        unique_words.add(word)
    
    return len(unique_words)/len(all_words)

print(type_token_ratio("hi , ,        hi this is a sentence"))