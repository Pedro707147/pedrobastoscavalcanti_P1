ef raizes(a, b, c):

    delta = b*b -(4*a*c)
    if (delta < 0):

        delta *= (-1)
        p_real = -b/2*a
        p_im = sqrt(delta)
        print('Raiz1: ', p_real, '+', p_im)
        print('Raiz2: ', p_real, '-', p_im)
        valor = 1

    elif (delta > 0):

        Raiz1 = (-b + (sqrt(delta)))/2*a
        Raiz2 = (-b - (sqrt(delta)))/2*a
        print('Raiz1: ', Raiz1, 'Raiz2: ', Raiz2)
        valor = 0

    else:
        Raiz = -b/2*a
        print('A raiz é: ', Raiz)
        valor = 0
    return valor


def main():

    a= int(input('Insira um valor diferente de zero.'))
    b = int(input('Insira um valor.'))
    c = int(input('insira um valor.'))

    raizes(a, b, c)
    resultado = raizes(a, b, c)
    print(resultado)

main()
