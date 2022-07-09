def slopeStyleScore(scores):
    min = 1000000
    max = -1000000
    sum = 0

    for element in scores:
        if element < min:
            min = element
        
        if element > max:
            max = element
    
    scores.remove(max)
    scores.remove(min)

    for element in scores:
        sum += element

    average = sum / len(scores)
    return round(average, 2)

print(slopeStyleScore([94, 95, 95, 95, 90]))