def is_anagram(fst_word, snd_word):

    first = fst_word.lower()
    second = snd_word.lower()

    if len(first) == len(second):

        for i in range(len(first)):
            if first.count(first[i]) == second.count(second[i]):
                continue
            else:
                return False

        return True
    else:
        return False

def is_anagram2(fst_word, snd_word):
    return sorted(fst_word.lower()) == sorted(snd_word.lower())

print(is_anagram("TOP_CODER", "COTO_PRODE"))
print(is_anagram2("TOP_CODER", "COTO_PRODE"))
    