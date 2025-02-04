
#try:
    #numero_1= int(input('Inserir um número inteiro'))
    #numero_2= int(input('Inserir um número inteiro'))
    #resultado= numero_1 // numero_2
    #print(resultado)
#except:
    #print('Vc esta digitado um numero que não é divisivel por outro!!')    



#PARA CADA TIPO DE ERRO EU TENHO CONSIGO TER UM TIPO DE SAÍDA(OUTPUT)
    #NESTE CASO SIMULANDO UM OUTPUT PARA NÚMERO INVÁLIDO E OUTRO PARA CASO APERTE ERRADO 
    #   ALGUMA TECLA NESTE CASO O CTRL + C

#try:
    #numero_1= int(input('Inserir um número inteiro'))
    #numero_2= int(input('Inserir um número inteiro'))
    #resultado= numero_1 // numero_2
    #print(resultado)
#except ZeroDivisionError:
    #print('Vc esta digitado um numero que não é divisivel por outro!!')
#except KeyboardInterrupt:
    #print('Acho que vc não quis inserir um numero!!')



#TypeError

#nome= input('digite seu nome:')
#
#try:
    #resultado= len(nome.strip())
    #print(resultado)
#except TypeError as e:
    #print(e) # imprime a mensagem de erro.    


# o typeError é um erro detipagem, igual o exemplo abaixo onde quero usar o método len()
#   em em um objeto do tipo int(inteiro), sendo que deviria usar no tipo str(string) 

#numero= 3
#
#try:
    #resultado=len(numero)
#except TimeoutError as e:
    #print(e)  
#else:
    #print('ocorreu tudo bem!!')
#finally:
    #print('O imprtante é participar')           




nuemero= int(input('insira um numero:'))

if isinstance(nuemero, int):
    print('a variável é inteiro')
else:
    print('a variável não é um inteiro!!')
