def count_words(arr):
    words = {}

    for element in arr:
        if words.get(element):
            words[element] += 1
        else:
            words[element] = 1

    return words

print(count_words(["python", "python", "python", "ruby"]))