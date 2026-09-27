def character_frequency(text, ch):
    frequency = 0

    for character in text:
        if character == ch:
            frequency += 1

    return frequency

print(character_frequency("programming", "g")) 