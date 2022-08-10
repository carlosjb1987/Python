
def primo (numero):
    for n in range(2, numero):
        if numero % n == 0:
            return "No es un numero primo"
        else:
            return "Es un número primo"


print(primo(14))