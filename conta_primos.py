def n_primos(n1):
    if(n1 >= 2):
        total = 0 
        while n1 >= 2:
            n = 1
            primo = 0
            while n <= n1:
                if(n1 % n == 0):
                    primo += 1
                    n += 1
                else:
                    n += 1
            if(primo == 2):
                total += 1
                n1 -= 1
            else:
                n1 -= 1
        return(total)
    else:
        print('digite um numero maior ou igual a 2')
