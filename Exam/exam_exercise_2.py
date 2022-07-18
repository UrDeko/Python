def marbles_count(marbles):
    result = {}
    for i in range(len(marbles)):
        if result.get(marbles[i][0]):
            result[marbles[i][0]] += marbles[i][1]
        else:
            result[marbles[i][0]] = marbles[i][1] 

    return result

print(marbles_count([("red", 3), ("blue", 2), ("yellow", 10), ("red", 7), ("green", 8), ("blue", 5), ("yellow", 9)]
))