def count_consonants(text):
    total = 0

    for ch in text:
        if ch.isalpha() and ch.lower() not in "aeiou":
            total += 1

    return total

print(count_consonants("Hello World"))  