def star_pattern(n):
    for row in range(1, n + 1):
        for column in range(row):
            print("*", end="")
        print()

star_pattern(5)