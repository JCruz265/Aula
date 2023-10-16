#App para validar um triângulo
#Apresentação
print('\n\t\t\t -- Identidade de um triângulo --')
#Entrada de Dados do triangulo
a = float(input('Digite o tamanho do lado -A- : '))
b = float(input('Digite o tamanho do lado -B- : '))
c = float(input('Digite o tamanho do lado -C- : '))
#Processamento dos dados
if (a > b + c) or (c > a + b) or (b > a + c):
    #Saida
    print('Não é um triângulo')
else:
    print('É um triângulo')