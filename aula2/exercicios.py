#TypeError, Type Check, Type Conversion, try-except e if

#print( 5 / 4)
#print( 5 // 4)
#print( 5 % 4)


#data_user= input('digite uma data neste formato: dd/mm/aaaa')
#
#dt_sep = data_user.split('/')
#
#for nun in dt_sep:
    #print(nun)


'''                                                 EXERCICIOS                          '''  

##Inteiros (int)

#Escreva um programa que soma dois números inteiros inseridos pelo usuário.

'''n1= int(input('Digite um numero: '))
n2= int(input('Digite outro numero: '))
res= n1+n2
print(f'O resultado do numero {n1} somado ao numero {n2} é igual a {res} ')'''

#Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.

'''d1= int(input('Digite um numero que queira dividir: '))
div2= int(input('Digite outro numero que sera o divisor: '))
res= d1%div2
print(f'O resultado do numero {d1} sdividido pelo numero {div2} é igual a {res} ')'''

#Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.

'''n1= int(input('Digite um numero: '))
n2= int(input('Digite outro numero: '))
res= n1*n2
print(f'O resultado do numero {n1} multiplicado numero {n2} é igual a {res} ')'''


#Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.

'''n1= int(input('Digite um numero: '))
n2= int(input('Digite outro numero: '))

res1= n1/n2 #divisão normal
res2= n1//n2 #divisão de inteiro
res3= n1%n2 # divisão resto

print(f'O resultado do numero {n1} dividido por {n2} é igual a {res1} sendo divisão normal, aqui trazendo somente o resultado inteiro {res2} e aqui caso tenha resto {res3} ')'''

#Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.

'''n1= int(input('Digite um numero que vc deseja saber seu valor elevado ao quadrado: '))
res= n1**2 
print(f'O resultado do numero {n1} elevado ao quadrado é {res}')'''

##Números de Ponto Flutuante (float)

#Escreva um programa que receba dois números flutuantes e realize sua adição.

'''n1= float(input('Digite um numero decimal: '))
n2= float(input('Digite outro numero decimal: '))
res= n1 + n2 

print(f'O resultado do numero {n1} somado ao {n2} é igual ao {res}')
print(f'O resultado do numero {n1} somado ao {n2} é igual ao {res:.2} com duas casas decimais')'''

#Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.

## Solicita ao usuário para digitar os números separados por espaços
'''OPÇÃO1
entrada = input("Digite os números flutuantes separados por espaços: ")

# Converte a entrada em uma lista de números flutuantes
numeros = [float(num) for num in entrada.split()]

# Calcula a média
media = sum(numeros) / len(numeros)

print("A média é:", media)
#print(f'O resultado do numero {n1} somado ao {n2} é igual ao {res}')'''

'''n1= float(input('Digite um numero decimal: '))
n2= float(input('Digite outro numero decimal: '))

div= (n1 + n2) / 2

print(f'A média de {n1} e  {n2} é {div}')'''

#Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).

'''n1= float(input('Digite um numero decimal: '))
p= float(input('Digite a base exponencial: '))

res= n1**p
print(res)'''

#Faça um programa que converta a temperatura de Celsius para Fahrenheit.
'''C= float(input('Digite a temperatura em Celsius'))

f = (C * 9/5) + 32

print(f' Este grau {C} em Celsius, representa {f} graus Fahrenheit')'''

#Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.
'''import math

r= float(input('Digite o  valor do raio do circulo: '))

a= math.pi * r

print(f'Este é o valor da área do circulo {a:.3} ')'''

#Strings (str)
#Escreva um programa que receba uma string do usuário e a converta para maiúsculas.

'''var= input('Digite uma palavra: ')

print(var.upper())'''

#Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.

'''var= input('Digite uma palavra: ')

print(var.lower())'''

#Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem #espaços em branco no início e no final.

'''var= input('Digite uma uma frase: ')

var= '   o gato de botas   !!'
var2= 'o gato de botas!'
print(var.strip())
print(var2.strip())'''

#Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o #dia, o mês e o ano separadamente.
  
#dt= input('Digite uma data sguindo este formato dd/mm/aaaa: ')
#
#dia, mes, ano= dt.split('/')
#
#print(f'este é o dia digitado: {dia}')
#print(f'este é o mes digitado: {mes}')
#print(f'este é o ano digitado: {ano}')

#possibilidade a corrigir
'''for d in dt:
    print(d.split('/'))'''

#Escreva um programa que concatene duas strings fornecidas pelo usuário.

'''p1= input('Digite metade de uma palavra: ')
p2= input('Digite a outra parte da palavra: ')

print(p1 + p2)
'''

#Booleanos (bool)
#Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da #operação AND entre elas.

'''valor1= True
valor2= False

res_and= valor1 and valor2

print(res_and)'''

#Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.

'''valor1= True
valor2= False

res_and= valor1 or valor2

print(res_and)'''

#Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
#MINHA SOLUÇÃO:
'''ent=int(input('insira um valor sendo 1 verdadeiro e 0 falso'))

if ent ==1:
    True
else:
    False
n_ent= print(not(ent))''' 

#SOLUÇÃO PROFESSOR:

# Exemplo de entrada
'''resultado_not = not valor1
print("Resultado do NOT lógico:", resultado_not)'''

#Faça um programa que compare se dois números fornecidos pelo usuário são iguais.

 ##ESTA SOLUÇÃO ENGLOBA O PRÓXIMO EXERCICIO

#MINHA SOLUÇÃO:
'''v1= float(input('digite um número: '))
v2= float(input('digite outro número: '))

if v1 == v2:
    print('Os números são iguais!')
else:
    print('Os números são diferentes!')'''    

#SOLUÇÃO PROFESSOR
'''num1 = 5
num2 = 5
resultado_igualdade = (num1 == num2)
print("Resultado da igualdade:", resultado_igualdade)'''

#Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.
#SOLUÇÃO PROFESSOR
'''resultado_diferenca = (num1 != num2)
print("Resultado da diferença:", resultado_diferenca)'''


#x= [0, 1, 2]
#y= x
#x +=[3, 4]
#print(x)
#print(y)
#print( x is y)