def count_vowels_consonants(text):
    vowels = 0
    consonants = 0

    for ch in text:
        if ch.isalpha():
            if ch.lower() in "aeiou":
                vowels += 1
            else:
                consonants += 1

    return vowels, consonants

vowels, consonants = count_vowels_consonants("Python Programming")

print("Vowels:", vowels)          
print("Consonants:", consonants)  