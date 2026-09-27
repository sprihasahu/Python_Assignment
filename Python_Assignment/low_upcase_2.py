def convert_uppercase(text):
    result = ""

    for ch in text:
        if "a" <= ch <= "z":
            result += chr(ord(ch) - 32)
        else:
            result += ch

    return result

print(convert_uppercase("Hello Python 123"))
