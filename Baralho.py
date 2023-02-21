# O exercício resolvido nesse código é o desse link: https://olimpiada.ic.unicamp.br/pratique/ps/2021/f1/baralho/

"""
Pensei em possíveis ideias de código e resolvi fazer a solução por funções, as quais são chamadas para verificar, atualizar e mostrar a quantidade de cartas de cada naipe
do baralho de acordo com a sequência fornecida
"""

import re

#Variáveis que armazenam a quantidade de cartas de cada naipe
cartasc = 0
cartase = 0
cartasu = 0
cartasp = 0

# Variáveis que representam se tem erro (cartas duplicadas) em um conjunto de um naipe
ec = False
ee = False
eu = False
ep = False

#Função que adiciona no contador do naipe da carta
def adiciona_naipe_q_foi(carta):
    global cartasc
    global cartase
    global cartasu
    global cartasp
    if carta[2] == "C":
        cartasc+=1
    if carta[2] == "E":
        cartase+=1
    if carta[2] == "U":
        cartasu+=1
    if carta[2] == "P":
        cartasp+=1
        
#Função para ver se um naipe esta completo
def completou(l_cartas):
    if l_cartas==13:
        print(0)

#Recebe os caracteres que descrevem o baralho
conjunto=input()
conjunto = re.findall('...', conjunto)
cartasQForam = []

#Função que printa se tem erro em um naipe
def tem_erro(erroNaipe):
    if erroNaipe:
        print("erro")
        return erroNaipe
        
#Função que coloca que o naipe da carta fornecida tem erro
def arruma_erro(carta):
    global ec
    global ee
    global eu
    global ep
    if carta[2] == "C":
        ec=True
    if carta[2] == "E":
        ee=True
    if carta[2] == "U":
        eu=True
    if carta[2] == "P":
        ep=True
        
#Função para mostrar o número de cartas que faltam para o naipe estar completo
def n_que_falta(carta):
    if carta<13:
        print(13-carta)
for carta in conjunto:
    if carta in cartasQForam:
        arruma_erro(carta)
        pass
    else:
        cartasQForam.append(carta)
        adiciona_naipe_q_foi(carta)
     
#Chamando as funcoes para retornar as saidas
completou(cartasc)
if tem_erro(ec):
    pass
else:
    n_que_falta(cartasc)
completou(cartase)
if tem_erro(ee):
    pass
else:
    n_que_falta(cartase)
completou(cartasu)
if tem_erro(eu):
    pass
else:
    n_que_falta(cartasu)
completou(cartasp)
if tem_erro(ep):
    pass
else:
    n_que_falta(cartasp)
