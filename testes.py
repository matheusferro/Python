import math
def primo(x):
    i = False
    while i == False:
        div = 1
        contador = 0
        while div <= x:
            if (x % div == 0):
                contador += 1
                div += 1
            else:
                div += 1
        if(contador == 2):
            i = True
        else:
            x -= 1
    return(x)


def e_hipotenusa(n):
    n_primo = primo(n)
    while n_primo != 2:
        if(n % n_primo == 0 and n_primo % 4 == 1):
            return(1)
        else:
            n_primo = primo(n_primo-1)
    return(0)

def soma_hipotenusas(n):
    if(n >= 0):
        hip = 0
        while n > 1:
            if(e_hipotenusa(n) == 1):
                hip += n
            n -= 1
        return(hip)
    else:
        return(print('erro'))
