
# >>>>>>>>>>>>>>>>>>>>>>DESAFIO<<<<<<<<<<<<<<<<
# 1) Solicita ao usuário que digite seu nome
# 2) Solicita ao usuário que digite o valor do seu salário
# Converte a entrada para um número de ponto flutuante
# 3) Solicita ao usuário que digite o valor do bônus recebido
# Converte a entrada para um número de ponto flutuante
# 4) Calcule o valor do bônus final
# 5) Imprima cálculo do KPI para o usuário
# 6) Imprime a mensagem personalizada incluindo o nome do usuário, salário e bônus
# Bônus: Quantos bugs e riscos você consegue identificar nesse programa?





CONSTANTE_BONUS= 1000

nome = input('Digite o seu nome aqui: ')

salario = float(input('Coloquei aqui o valor do seu salário(caso seja 3k>>3.000,00 | 2546k>>2.546,00): '))

bonus = float(input('coloque aqui o percentual do seu bonus'))

mont_final = salario+(salario * bonus)


print(f'Olá {nome} !, espero que esteja bem, seu saário de: {salario} ,  com a aliquita de {bonus},deu um montante de: {mont_final}')