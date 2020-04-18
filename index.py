#AUTOR; Eduardo Rico Sotomayor. GitHub: Eduardo-rico. www.ricosotomayor.com

def Simpson(f, a, b, n):
    if n % 2 != 0:
        return 'El numero de intervalos tiene que ser par'
    h = float((b-a))/n
    suma1 = 0
    for i in range(1, int(n/2)+1):
        suma1 = suma1 + f(a + (2*i -1)*h)
    suma2 = 0
    for j in range(1, int(n/2)):
        suma2 = suma2 + f(a+ (2*j)*h)
    resultado = (h/3.0)*(f(a) + 4*suma1 + 2*suma2 + f(b))
    return resultado

def partida(x):
    if (x>= 0 and x<= 0.5):
        return x
    if(0.5 < x and x <= 1):
        return 1-x

def Trapecio(f, a, b, n):
    h = float(b-a)/n
    suma = 0.5*(f(a) + f(b))
    for i in range(1, n):
        suma = suma + f(a + (i*h))
    resultado = suma * h
    return resultado

def ln(x):
    return 1/x

def log(x):
    return 1/x * 0.4329

print('\n')
print('El resultado del inciso 1) para referirnos al Ln(2) \n del ejercicio 2 es {} Trapecio'.format(Trapecio(ln, 1, 2, 20)) )
print('\n')
print('El resultado del inciso 1) para referirnos al Ln(2) \n del ejercicio 2 es {} Simpson'.format(Simpson(ln, 1, 2, 20)) )
print('\n')
print('El resultado del inciso 1) para referirnos al Log(2) \n del ejercicio 2 es {} Trapecio'.format(Trapecio(log, 1, 2, 20)) )
print('\n')
print('El resultado del inciso 1) para referirnos al Log(2) \n del ejercicio 2 es {} Simpson'.format(Simpson(log, 1, 2, 20)) )
print('\n\n')
print('\n\n')
print('El resultado del inciso 1) para referirnos al Ln(2) \n del ejercicio 3 es {} Trapecio'.format(Trapecio(ln, 1, 2, 20)) )
print('\n')
print('El resultado del inciso 1) para referirnos al Ln(2) \n del ejercicio 3 es {} Simpson'.format(Simpson(ln, 1, 2, 20)) )
print('\n')
print('El resultado del inciso 1) para referirnos al Log(2) \n del ejercicio 3 es {} Trapecio'.format(Trapecio(log, 1, 2, 6)) )
print('\n')
print('El resultado del inciso 1) para referirnos al Log(2) \n del ejercicio 3 es {} Simpson'.format(Simpson(log, 1, 2, 6)) )
print('\n\n')
print('\n\n')
print('El resultado del inciso a) del ejercicio 2 es {}'.format(Trapecio(partida, 0, 1, 2)) )
print('El resultado del inciso b) del ejercicio 2 es {}'.format((Trapecio(partida, 0, 0.5, 2))+(Trapecio(partida, 0.5, 1, 2))) )
print('El resultado del inciso c) del ejercicio 2 es {}'.format(Simpson(partida, 0, 1, 2)) )



