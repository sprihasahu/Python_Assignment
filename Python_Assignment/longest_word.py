def find_longest_word(text):
    longest = ""
    current_word = ""

    for ch in text:
        if ch.isspace():
            if len(current_word) > len(longest):
                longest = current_word
            current_word = ""
        else:
            current_word += ch

    # Check the final word when there is no trailing space.
    if len(current_word) > len(longest):
        longest = current_word

    return longest

print(find_longest_word("Python programming is interesting"))
