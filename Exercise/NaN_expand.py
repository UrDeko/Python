def nan_expand(num):
    if num == 0:
        return "\"\""
    else:
        result = "\""

        for i in range(num):
            result += "Not a "

        return result + "NaN\""

def nan_expand2(num):
    if num == 0:
        return "\"\""
    return '"' + "Not a " * num + "NaN" + '"'

print(nan_expand2(0))