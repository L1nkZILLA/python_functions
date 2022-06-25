print("---- Declaracao de variaveis e operacoes matematicas ----")
# Meu primeiro script do Python
print("Hello World =D")

a = 1
print("o valor de a eh")
print(a)

b = 3
print("o valor de b eh")
print(b)

print("se eu somo a + b entao: ")
soma = a + b
print(soma)

print("se eu subtraio a - b entao: ")
subtracao = a - b 
print(subtracao)

print("se eu multiplico a * b entao: ")
multiplicacao = a * b
print(multiplicacao)

print("se eu divido a / b entao: ")
divisao = a / b
print(divisao)

print("-----------------------------------------")
print("---- Strings (Textos como variaveis) ----")

#começando a ver sobre strings

c = "Guilherme"
print(c)

c_outro_jeito = "Guilherme"
print(c_outro_jeito)

parte_final = " Henrique Alves da Costa"

final_com_tudo = c + parte_final
print (final_com_tudo)

final_com_tudo_e_com_caixa_alta = final_com_tudo.replace("e", "E")
print(final_com_tudo_e_com_caixa_alta)

print("--------------------------------------------")
print("------------------ Listas ------------------")

#Lista de números 
minha_lista = [2, 1, 6, 3, 80, 12312266]
print("conteudo da minha lista")
print(minha_lista)

print("primeiro elemento da minha lista")
primeiro_elemento = minha_lista[0]
print(primeiro_elemento)

print("segundo elemento da minha lista")
segundo_elemento = minha_lista[1]
print(segundo_elemento)

print("terceiro elemento da minha lista")
terceiro_elemento = minha_lista[2]
print(terceiro_elemento)

print("quarto elemento da minha lista")
quarto_elemento = minha_lista[3]
print(quarto_elemento)

print("quinto elemento da minha lista")
quinto_elemento = minha_lista[4]
print(quinto_elemento)

print("sexto elemento da minha lista")
sexto_elemento = minha_lista[5]
print(sexto_elemento)

#Lista de palavras
minha_lista_de_palavras = ['Guilherme', 'Henrique', 'Alves', 'da Costa']
print('conteudo da minha lista de palavras: ')
print(minha_lista_de_palavras)

terceiro_elemento_lista_de_palavras = minha_lista_de_palavras [2]
print("terceiro elemento da minha lista de palavras: ")
print(terceiro_elemento_lista_de_palavras)

print("-------------------------------------------")
print("---------------- if e else ----------------")

saldo_conta_bancaria = -1
print('Tentando sacar dinheiro')
if saldo_conta_bancaria > 0:
    print('Saque disponível')
else:
    print('Saque indiponível, Você não possui saldo.')

print('Checando balconistas')
minha_lista_de_presenca_de_balconistas = ['presente', 'presente', 'presente']
if len(minha_lista_de_presenca_de_balconistas) == 3:
    print('Estamos funcionando a todo vapor!')
else:
    print('Está faltando gente para trabalhar.')

print("------------------------------------------")
print("---------------- for loop ----------------")

for i in range (3): 
    print(i)
    print('Hello World!')

print('printando elementos da minha lista de palavras: ')
for elemento in minha_lista_de_palavras:
    elemento_modificado = "=D" + elemento + "=D"
    print (elemento)

print('Vamos saber quantas palavras na minha lista que tem mais de 3 letras: ')

total_de_palavras_com_mais_de_3_letras = 0
for palavra in minha_lista_de_palavras:
    if len(palavra) > 3:
        total_de_palavras_com_mais_de_3_letras += 1
    else:
        print('Elemento com menos de 3 letras')

print('quantidade de palavras com mais de três letras: ')
print(total_de_palavras_com_mais_de_3_letras)
    
print("-----------------------------------------")
print("---------------- Funções ----------------")

#def nome_da_função(argumento_de_entrada):

def imprimir_hello_world():
    print("Hello World!")

imprimir_hello_world()

def checar_se_tem_dinheiro(saldo_conta_bancaria):
    print('Tentando sacar dinheiro')
if saldo_conta_bancaria > 0:
    print('Saque disponível')
else:
    print('Saque indiponível, Você não possui saldo.')

checar_se_tem_dinheiro(-123123)
checar_se_tem_dinheiro(9999999)
saldo_conta_bancaria = 4345
checar_se_tem_dinheiro(saldo_conta_bancaria)

def somar_todos_valores_da_minha_lista_de_numeros(minha_lista):
    valor_total = 0
    for valor in minha_lista:
        #valor_total += valor
        valor_total = valor_total + valor
    return valor_total   

valor_total = somar_todos_valores_da_minha_lista_de_numeros(minha_lista)
print('valor total (esperamos 12312358): ')
print(valor_total)

print("------------------------------------------")
print("-- Algorítimos de ordenação bubble sort --")

def algoritmo_bubble_sort(minha_lista):
    n = len(minha_lista)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if minha_lista[j] > minha_lista[j+1] :
                minha_lista[j], minha_lista[j+1] = minha_lista[j+1], minha_lista[j]
    return minha_lista

print('Minha lista antes: ')
print(minha_lista)

print('Minha lista depois: ')
Minha_lista_depois = algoritmo_bubble_sort(minha_lista)
print(Minha_lista_depois)

print("-------------------------------------------")
print("------ Leitura e escrita de arquivos ------")

arquivo_para_ler = open('minha_movimentacao_bancaria.txt', 'r')
dados_do_arquivo = arquivo_para_ler.read()
lista_dados_do_arquivo = dados_do_arquivo.split('\n')
saldo_total = 0
for valor in lista_dados_do_arquivo:
    saldo_total += float(valor)
print('o saldo total eh (733): ')    
print(saldo_total)
arquivo_para_guardar_o_saldo = open('meu_saldo_total.txt', 'w')
arquivo_para_guardar_o_saldo.write(str(saldo_total))
arquivo_para_guardar_o_saldo.close()

print("-------------------------------------------")
print("----------------- Debugar -----------------")

import pdb; pdb.set_trace()
