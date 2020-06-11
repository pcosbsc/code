
bad_words = ['natural']
with open('/Users/Pep/code/CMIP5_copy.txt') as oldfile, open('/Users/Pep/code/CMIP5.txt', 'w') as newfile:
    for line in oldfile:
        if not any(bad_word in line for bad_word in bad_words):
            newfile.write(line)
