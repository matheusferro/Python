def primo(x):
    div = 1
    contador = 0
    while div <= x:
        if (x % div == 0):
            contador += 1
            div += 1
        else:
            div += 1
    if(contador == 2):
        return True
    else:
        return False

def maior_primo(nu):
    while primo(nu) == False:
        primo(nu)
        nu -= 1
    return(nu)


            

