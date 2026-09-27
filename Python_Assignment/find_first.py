def first_character(text):
    if text == "":
        print("String is empty")
        return

    for ch in text:
        print(ch)
        break

first_character("Python")  