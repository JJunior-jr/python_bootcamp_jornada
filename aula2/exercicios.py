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

n1= float(input('Digite um numero decimal: '))
n2= float(input('Digite outro numero decimal: '))

div= (n1,n2)


print(div)


#print(f'O resultado do numero {n1} somado ao {n2} é igual ao {res}')


#Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
#Faça um programa que converta a temperatura de Celsius para Fahrenheit.
#Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.
#Strings (str)
#Escreva um programa que receba uma string do usuário e a converta para maiúsculas.
#Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
#Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem #espaços em branco no início e no final.
#Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o #dia, o mês e o ano separadamente.
#Escreva um programa que concatene duas strings fornecidas pelo usuário.
#Booleanos (bool)
#Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da #operação AND entre elas.
#Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
#Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
#Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
#Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.



#x= [0, 1, 2]
#y= x
#x +=[3, 4]
#print(x)
#print(y)
#print( x is y)