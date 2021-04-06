import textstat

def get_flesch_reading_ease(text):
    return textstat.flesch_reading_ease(text)

def get_smog_index(text):
    return textstat.smog_index(text)

def get_flesch_kincaid_grade(text):
    return textstat.flesch_kincaid_grade(text)

# Etc.
# textstat.coleman_liau_index(test_data)
# textstat.automated_readability_index(test_data)
# textstat.dale_chall_readability_score(test_data)
# textstat.difficult_words(test_data)
# textstat.linsear_write_formula(test_data)
# textstat.gunning_fog(test_data)
# textstat.text_standard(test_data)
# textstat.fernandez_huerta(test_data)
# textstat.szigriszt_pazos(test_data)
# textstat.gutierrez_polini(test_data)
# textstat.crawford(test_data)