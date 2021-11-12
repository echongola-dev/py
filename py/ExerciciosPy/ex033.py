a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))

# verificando quem e menor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c 

# para verificar que o maior
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c

print('O menor numero verificado foi {}.'.format(menor))
print('O maior numero verificado foi {}.'.format(maior))