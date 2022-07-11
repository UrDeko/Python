def is_palindrome(number):
    string_number = str(number)

    for i in range(len(string_number) // 2):
        if string_number[i] == string_number[len(string_number) - 1 - i]:
            continue
        else:
            return False
    
    return True

print(is_palindrome(123))