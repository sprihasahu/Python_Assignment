def count_case(text):
    uppercase = 0
    lowercase = 0
    digits = 0
    spaces = 0

    for ch in text:
        if ch.isupper():
            uppercase += 1
        elif ch.islower():
            lowercase += 1
        elif ch.isdigit():
            digits += 1
        elif ch == " ":
            spaces += 1

    print("Uppercase:", uppercase)
    print("Lowercase:", lowercase)
    print("Digits:", digits)
    print("Spaces:", spaces)

count_case("Python123 ABC")