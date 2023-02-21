import re

#Quantidade de cartas de um naipe
cartasc = 0
cartase = 0
cartasu = 0
cartasp = 0

# Se tem erro em um conjunto de um naipe
ec = False
ee = False
eu = False
ep = False

#Adiciona no contador do naipe da carta
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
        
#Ve se um naipe esta completo
def completou(l_cartas):
    if l_cartas==13:
        print(0)
conjunto=input()
conjunto = re.findall('...', conjunto)
cartasQForam = []

#Printa se tem erro de um naipe
def tem_erro(erroNaipe):
    if erroNaipe:
        print("erro")
        return erroNaipe
        
#Arruma a variavel erro de um naipe
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
        
#Mostra o número de cartas que faltam
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