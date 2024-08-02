def pattern_right_angle_triangle(n: int):
    print("Pattern: Right-Angle Triangle")
    for i in range(1, n + 1):
        print("*" * i)
    print()

def pattern_square_grid(n: int):
    print("Pattern: Square Grid of Asterisks")
    for i in range(n):
        for j in range(n):
            print("*", end=" ")
        print()
    print()

def pattern_right_angle_triangle_numbers(n: int):
    print("Pattern: Right-Angle Triangle of Numbers")
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()
    print()

def pattern_number_triangle(n: int):
    print("Pattern: Number Triangle")
    for i in range(1, n + 1):
        print((str(i) + " ") * i)
    print()

def pattern_inverted_right_angle_triangle_asterisks(n: int):
    print("Pattern: Inverted Right-Angle Triangle of Asterisks")
    for i in range(n, 0, -1):
        print("* " * i)
    print()

def pattern_inverted_right_angle_triangle_numbers(n: int):
    print("Pattern: Inverted Right-Angle Triangle of Numbers")
    for i in range(n, 0, -1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()
    print()

def pattern_pyramid_asterisks(n: int):
    print("Pattern: Pyramid of Asterisks")
    for i in range(n):
        print(" " * (n - i - 1) + "*" * (2 * i + 1) + " " * (n - i - 1))
    print()

def pattern_diamond_asterisks(n: int):
    print("Pattern: Diamond of Asterisks")
    for i in range(n):
        print(" " * (n - i - 1) + "*" * (2 * i + 1) + " " * (n - i - 1))
    for i in range(n - 1, -1, -1):
        print(" " * (n - i - 1) + "*" * (2 * i + 1) + " " * (n - i - 1))
    print()

def pattern_diamond_asterisks_single_line(n: int):
    print("Pattern: Diamond of Asterisks with a Single Line in the Middle")
    for i in range(1, n + 1):
        print("*" * i)
    for i in range(n - 1, 0, -1):
        print("*" * i)
    print()

def pattern_alternating_binary(n: int):
    print("Pattern: Alternating Binary Pattern")
    start = 1
    for i in range(n):
        if i % 2 == 0:
            start = 1
        else:
            start = 0
        for j in range(i + 1):
            print(start, end=" ")
            start = 1 - start
        print()
    print()

def pattern_number_pyramid(n: int):
    print("Pattern: Number Pyramid")
    space = 2 * n - 2
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(str(j) + " ", end="")
        for _ in range(space):
            print(" ", end="")
        for k in range(i, 0, -1):
            print(str(k) + " ", end="")
        print()
        space -= 2
    print()

def pattern_incremental_number_triangle(n: int):
    print("Pattern: Incremental Number Triangle")
    num = 1
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(num, end=" ")
            num += 1
        print()
    print()

def pattern_alphabet_triangle(n: int):
    print("Pattern: Alphabet Triangle")
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            char = chr(64 + j)
            print(char, end=" ")
        print()
    print()

def pattern_inverted_alphabet_triangle(n: int):
    print("Pattern: Inverted Alphabet Triangle")
    for i in range(n, 0, -1):
        for j in range(1, i + 1):
            char = chr(64 + j)
            print(char, end=" ")
        print()
    print()

def pattern_repeating_alphabet_triangle(n: int):
    print("Pattern: Repeating Alphabet Triangle")
    for i in range(1, n + 1):
        char = chr(64 + i)
        print((char + " ") * i)
    print()

def pattern_alpha_hill(n: int):
    print("Pattern: Alpha-Hill")
    result = []
    for i in range(1, n + 1):
        spaces = ' ' * (n - i)
        left_half = [chr(ord('A') + j) for j in range(i)]
        full_row = left_half + left_half[-2::-1]
        row = ' '.join(full_row)
        result.append(spaces + row)
    result = '\n'.join(result)
    print(result)

