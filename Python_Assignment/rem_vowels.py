def remove_vowels(text):
    result = ""

    for ch in text:
        if ch.lower() not in "aeiou":
            result += ch

    return result

print(remove_vowels("Python Programming"))
