def es_bisiesto(ano):
    if not ano % 4 and (ano % 100 or  not ano % 400):
        return "Es bisiesto" 
    else:
        return "No es bisiesto"


print(es_bisiesto(1804))