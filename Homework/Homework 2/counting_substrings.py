def countSubstrings(string, pattern):
    count = string.count(pattern)
    if count > 0:
        return count
    else:
        return 0

def countSubstrings2(string, pattern):
    count = 0

    i = 0
    while i < len(string):
        contains = True

        for j in range(len(pattern)):
            if pattern[j] == string[i]:

                if i == len(string) - 1 and j == len(pattern) - 1:
                    break
                elif i == len(string) - 1 and j != len(pattern) - 1:
                    contains = False
                    break

                i += 1
            else:
                contains = False

                if i == len(string) - 1:
                    break

                i += 1
                break

        if contains:
            count += 1
    
    return count
        

print(countSubstrings2("This is this and that is this", "this"))