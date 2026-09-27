def count_words(text):
    words = 0
    inside_word = False

    for ch in text:
        if ch.isspace():
            inside_word = False
        elif not inside_word:
            words += 1
            inside_word = True

    return words

print(count_words("Python is easy to learn"))  
print(count_words("  Hello   world  "))        