#1)Solicite ao usuário que digite o seu nome:
#2) Solicite ao usuário que digite o valor do seu salário
#Converta a entrada para um número de ponto flutuante
#3)Solicite ao usuário que digite o valor do bônus recebido
#Converta a entrada para um número de ponto flutuante
#4) Calcule o valor do bônus final
#5) Imprima a mensagem personalizada incluindo o nome do usuário, salário e bônus
# Bônus: Quantos bugs e riscos vc consegue identificar nesse programa?


#POSSIBILIDADES DE ERROS:
#usuário colocar inteiro/float no lugar de string no campo nome

nome= input('Digite o seu nome: ')


if nome.isdigit():
    print('Vc digitou seu nome errado!')
    exit()
elif len(nome) == 0:
    print('Vc não digitou nada!')
    exit() 
elif nome.isspace():
    print('Vc digitou apenas espaço')
             

salario = float(input('Digite o seu salário: '))

bonus= float(input('Digite o seu bônus: '))

s_b= [salario, bonus]

print(sum(s_b))


nome= '25'
nome2= '25.7'
print('este é da var-> nome contendo um inteiro ', nome.isdigit())
print('este é da var-> nome2 contendo um float ', nome2.isdigit())