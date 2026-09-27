def count_vowels(text):
    total = 0

    for ch in text:
        if ch.lower() in "aeiou":
            total += 1

    return total

print(count_vowels("education")) 