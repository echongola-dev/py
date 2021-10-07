#        Ordem de precedencia nos Operadores Aretimetricos

#  1. ()
#  2. **
#  3. *, /, //, %
#  4. +, -

# nome = input('Qual e o seu nome? ')
# print('Prazer em te conhecer, {:=^20}!'.format(nome))

n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2

print('A Soma e {}, \n o produto e {}, e a divisao e {:.3f}'.format(s, m, d), end = ' <> ')
print('Divisao inteira {} e potencia {}'.format(di, e))