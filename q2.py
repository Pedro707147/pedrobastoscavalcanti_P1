def numeropi():

    diferensa = 5*10**(-9)
    pi1 = 1
    pi2 = 1

    while(diferensa <= (5*10**(-8))):
        cont1 = 3
        cont1 += 4
        pi1 = 4*(1 - (1/3) - (1/cont1))
        cont2 = 5
        cont2 += 4
        pi2 = 4*(1 + (1/5) + (1/cont2))
        diferensa = pi1 + pi2
        return diferensa
        return pi1
        return pi2
    print('Pi e igual a : ', pi2)
