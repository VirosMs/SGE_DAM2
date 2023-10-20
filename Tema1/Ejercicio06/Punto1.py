def argsNumericos(*p):
    if len(p) == 1:
        if isinstance(p[0], (int, float)):
            return pow(p[0], 2)
        else:
            return "No es un número: " + p[0]
    elif len(p) == 2:
        return  p[0] * p[1]
    else:
        return sum(p)


print(argsNumericos("buenos dias"))