#ESTUDO DE POO - CLASSES E OBJETOS
class foguete:
    '''CONTROLE DE FOGUETES'''
    def __init__(self, nome, nacao, posicao, status):
        self.nome = nome
        self.nacao = nacao
        self.posicao = posicao
        self.status = status

    def abastecer(self):
        self.status = 'Abastecido'
        print('Foguete \033[1;31m{}\033[m Abastecido com sucesso\n'.format(self.nome))

    def decolar(self):
        self.posicao = 'Espaço'
        print('Contagem regressiva 3.. 2.. 1.. Ignição >> Foguete \033[1;31m{}\033[m em Orbita\n'.format(self.nome))

    def pousar(self):
        print('Calculando janela de reentrada para \033[1;30m{}\033[m, Bem vindo de volta \033[1;31m{}\033[m\n'.format(self.nacao, self.nome))
        self.posicao = 'Terra'
        self.status = 'sem combustível'

def cabecalho():
    print('=-'*15)
    print('{:^30}'.format('CONTROLE DE FOGUETES'))
    print('=-'*15)

def satushangar():
    print('Status do Hangar')
    print([foguete1.nome, foguete1.nacao, foguete1.posicao, foguete1.status])
    print([foguete2.nome, foguete2.nacao, foguete2.posicao, foguete2.status])
    print([foguete3.nome, foguete3.nacao, foguete3.posicao, foguete3.status])
    print()

#CRIANDO OS OBJETOS E ATRIBUINDO SUAS CARACTERÍSTICAS
foguete1 = foguete('Antares', 'EUA', 'Terra', 'sem combustível')
foguete2 = foguete('Sputinik', 'URSS', 'Terra', 'sem combustível')
foguete3 = foguete('VLS1', 'BRASIL', 'Terra', 'sem combustível')


#CHAMANDO AS FUNÇÕES PARA TESTAR OS OBJETOS
cabecalho()
satushangar()
foguete1.abastecer()
foguete2.abastecer()
foguete3.abastecer()
satushangar()
foguete1.decolar()
foguete2.decolar()
satushangar()
foguete2.pousar()
satushangar()
