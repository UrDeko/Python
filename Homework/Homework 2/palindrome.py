def isPalindrome(number):
    stringNumber = str(number)

    for i in range(len(stringNumber) // 2):
        if stringNumber[i] == stringNumber[len(stringNumber) - 1 - i]:
            continue
        else:
            return False
    
    return True

print(isPalindrome(123))