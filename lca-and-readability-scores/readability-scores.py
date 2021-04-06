import textstat

test_data = (
    "Playing games has always been thought to be important to "
    "the development of well-balanced and creative children; "
    "however, what part, if any, they should play in the lives "
    "of adults has never been researched that deeply. I believe "
    "that playing games is every bit as important for adults "
    "as for children. Not only is taking time out to play games "
    "with our children and other adults valuable to building "
    "interpersonal relationships but is also a wonderful way "
    "to release built up tension."
)

print(textstat.flesch_reading_ease(test_data))
print(textstat.smog_index(test_data))
print(textstat.flesch_kincaid_grade(test_data))
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