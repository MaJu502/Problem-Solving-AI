def getStart(x):
    for countRS, row in enumerate(x):
        for countCS, element in enumerate(row):
            if element == 2:
                return (countRS, countCS)

def getEnd(x):
    retorno = []
    for countRS, row in enumerate(x):
        for countCS, element in enumerate(row):
            if element == 3:
                retorno.append((countRS, countCS))
    return retorno