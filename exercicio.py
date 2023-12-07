#Preencha as células de código para preencher os valores de (A), (B) e (C) na tabela de ticket
#médio abaixo:
#Dia Valor Total Vendas Qtd Total Vendas Ticket Medio
#19/01 (A) 3 320.52
#20/01 834.47 (B) 119.21
#23/01 15378.12 5 (C)


a = '961,56'
print(f'O valor total de vendas foi de {a}')
b = '7'
print(f'A quantidade total de vendas foi de {b}')
c = '3.075,624'
print(f'O ticket medio foi de {c}')


#Aplique três métodos distintos na string abaixo, você pode conferir alguns métodos neste link:


cancao = 'Roda mundo, roda gigante, roda moinho, roda pião.'

cancaomaiscula = cancao.upper()
print(f'E assim que fica a frase em maiuscula : {cancaomaiscula}')
cancaominuscula = cancao.lower()
print(f'E assim que fica a frase em minusculo : {cancaominuscula}')
cancaodividido = cancao.split()
print(f'E assim que fica a frase divida em um array : {cancaodividido}')

#Extraia da string abaixo o valor da taxa selic na variável selic e o valor do ano na variavel 
#ano . Imprima os valores na tela.


noticia = 'Selic vai a 2,75% e supera expectativas; ' + \
'é a primeira alta em 6 anos.'

selic = noticia[12:17]
print(f'O valor da selic foi de {selic}')
ano = noticia[62:63]
print(f'O ano equivalente sera de {ano}')


#Utilize a tabela da verdade para responder: qual o valor da variável x?
#a = False
#b = True
#x = not a & b

print('O valor de X e True. Pois o inverso de A e True e o valor de B sendo True passa a condição & como verdadeira.')
