def what_is_my_sign(day, month):
    signs = [ [20, 4, "Aries"],
              [21, 5, "Taurus"],
              [21, 6, "Gemini"],
              [22, 7, "Cancer"],
              [22, 8, "Leo"],
              [23, 9, "Virgo"],
              [23, 10, "Libra"],
              [22, 11, "Scorpio"],
              [21, 12, "Sagittarius"],
              [20, 1, "Capricorn"],
              [19, 2, "Aquarius"],
              [20, 3, "Pisces"] ]
    
    for i in range(len(signs)):
        if month == signs[i][1]:
            if day < signs[i][0]:
                return signs[i][2]
            else:
                if signs[i] == signs[len(signs) - 1]:
                    i == 0
                return signs[i + 1][2]

print(what_is_my_sign(29, 1))