from itertools import count


def roman_numerals(s):
    roman_symbols = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    result = 0
    for key in roman_symbols:
        if s.count(key):
            result += s.count(key) * roman_symbols[key]

    if s.count("IV") == 1 or s.count("IX") == 1:
        result -= 2
    if s.count("XL") == 1 or s.count("XC") == 1:
        result -= 20
    if s.count("CD") == 1 or s.count("CM") == 1:
        result -= 200

    return result

print(roman_numerals("MCDXLVIII"))