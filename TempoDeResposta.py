# O exercício resolvido nesse código é o desse link: https://olimpiada.ic.unicamp.br/pratique/ps/2021/f1/tempo/

"""
Ao analisar o problema, vi que precisaria conferir todos os amigos que tinham mensagens, mostrar o número deles e verificar
se tem resposta para todas as mensagens, se tiver, deve ser mostrado o tempo de resposta, caso contrário, deve ser exibido -1.
Para isso, é necessário abrir conversas e fechar para saber se houve resposta e armazenar o tempo de resposta se houver, resolvi
fazer uma classe Amigo que registra em seus atributos, o número do amigo, se a conversa está aberta e a contagem do tempo
de resposta, além de um método para mostrar a saída(o tempo de resposta ou então -1 se estiver em aberto).
Para resolver agora foi só ir criando as classes de amigo de acordo com as mensagens e, ao acabar, chamar os métodos de mostrar
a saída para cada amigo.

"""

#Recebendo o número de registros
n=int(input())

#Lista para armazenar os amigos
amigos=[]

#Classe para os Amigos
class Amigo:
    #Construtor + atributos
    def __init__(self,numero,estadoConversa): 
        self.numero = numero
        self.estadoConversa = estadoConversa
        self.contador=0
        
    #Método que mostra a saída
    def mostra_saida(self): 
        if self.estadoConversa == "Aberta":
            return -1
        else:
            return self.contador            

#Função para verificar se o amigo n ja mandou mensagem antes
def contem_n(lista,n):
    retorno = False
    for x in lista:
        if x.numero == n:
            retorno = True
    return retorno

#Função para trocar se a conversa está aberta ou fechada
def inverte_estadoConversa(lista,n):
    for x in lista:
        if x.numero == n:
            if x.estadoConversa == "Aberta":
                x.estadoConversa = "Fechada"
            else:
                x.estadoConversa = "Aberta"

#Função para adicionar tempo às conversas abertas
def adicionaTempo(lista,valor):
    for x in lista:
        if x.estadoConversa == "Aberta":
            x.contador += valor
            
ultimo="nda"
c="f"
w=0
#Percorrendo as entradas, adicionando amigos à lista e incrementando os contadores de tempo de amigos com conversas abertas
while w<n:
    ultimo=c
    c, x = input().split()
    x=int(x)
    if c!= "T":
        if ultimo!= "T":
            adicionaTempo(amigos,1)
        if contem_n(amigos,x):
            inverte_estadoConversa(amigos,x)
        else:
            amigos.append(Amigo(x,"Aberta"))
    else:
        adicionaTempo(amigos,x)
    #Ordenando a lista de amigos de acordo com o atributo numero
    amigos.sort(key = lambda x:x.numero)
    w+=1
    
for amigo in amigos:
    print(f"{amigo.numero} ",end='')
    print(amigo.mostra_saida())