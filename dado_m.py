from random import randint
import os

def menu():

    list = ['Rolagem de dados', 
            'Regras do D&D',
            'Classes do D&D'
            ]
    print('================================')
    print('================================')
    
    for v in range(len(list)):
        print(F'{v + 1}:\033[1;36m {list[v]}\033[m')
    
    print('================================')
    print('================================')



def dado_um(v):
    try:
        da = randint(1, v)
        print(f'd{v} {da}')
    except:
        print('comando invalido')


def dado_varios(v, c):
    list = []
    try:
        for v in range(0, v):
            list.append(randint(1, c))
        cont = 0
        for v in list:
            cont = cont + v

        print(f' d{c}x{len(list)} {list} = {cont}')
        
    except:
        print('comando invalido')
        


def linha():
    print('=================================')



def regras():
    list = ['Rolagens de dados', 
    'Ataque', 
    'Testes genericos',
    'Mecânicas básicas',
    'Vantagem e desvantsgem',
    'Inspiração',
    'Testes passivos',
    'Ações livres',
    'Reações',
    'Sair'
    ]
    while True:
        try:
            for v in range(len(list)):
                print(f'{v + 1}: \033[1;36m{list[v]}\033[m')
            op = int(input('>> '))
            os.system('cls')
        except:
            print('comando invalido')
            input('>> ')
            break
        

        if op == 10:
            break

        elif op == 1:
            print('>>>>>>\033[1;36mRolagens basicas\033[m]>>>>>>')
            print('''\033[1;34mA rolagem de dados, assim como em qualquer outro RPG, 
é uma parte fundamental das regras d&d 5e.
Antes de saber como usar os dados,
é necessário que você os tenha.
Dados de RPG são conhecidos por não serem convencionais,
pois possuem contam com diversas faces.
Para iniciar sua jornada você precisa entender 
a dinâmica de duas rolagens básicas: 
O jogo possui basicamente três rolagens de dado 
para as seguintes situações de jogo:
ATACAR: d20 + modificador de atributo + proficiência 
com arma ou magia + modificadores situacionais. 
Se o total for igual ou maior que a Classe de Armadura (CA), o ataque acerta. 
TESTES: d20 + modificador de atributo + modificadores circunstanciais. 
TESTES DE RESISTÊNCIA: d20 + modificador de atributo + modificador 
de proficiência (se aplicável).\033[m ''')
            input('>> ')
            os.system('cls')

        
        elif op == 2:
            print('>>>>>\033[1;36mATAQUE\033[m>>>>>>>>')
            print('''\033[1;34mD20 (Dado de vinte faces) + modificador de atributo + 
proficiência com arma ou magia + modificadores situacionais. 
Todos estes itens estão descritos em sua ficha de personagem.
Se o total for igual ou maior que o CA (Classe de armadura) 
do seu inimigo, o ataque acerta.\033[m''')
            input('>> ')
            os.system('cls')

        
        elif op == 3:
            print('>>>>\033[1;36mTestes genéricos\033[m')
            print('''\033[1;34mD20 + modificador de atributo + modificadores  de circunstâncias.

Estes testes são utilizados para as mais variadas ocasiões e 
aqui vale o bom senso. Um teste para abrir uma porta trancada, 
por exemplo, se utiliza o modificador de atributo “força”. 
Se o seu personagem estiver machucado, por exemplo, 
o mestre pode impor uma desvantagem, por exemplo\033[m''')
            input('>> ')
            os.system('cls')
        

        elif op == 4:
            print('>>>>>\033[1;36mMecânicas básicas\033[m')
            print('''\033[1;34mA mecânica básicas de todos os RPGs 
é a de criar e interpretar um personagem,
fazendo com que ele evolua durante a partida.
Essa mecânica é associada como extensão de jogadores 
com diferentes habilidades.
Nas regras d&d 5e as mecânicas básicas presentes são:\033[m''')
            input('>> ')
            os.system('cls')

        
        elif op == 5:
            print('>>>>>\033[1;36mVantagem e desvantagem*\033[m')
            print('''\033[1;34mPara calcular a vantagem é necessário rolar 2d20 
(dois dados de 20 faces) e ficar com o maior resultado. 
Já a desvantagem se torna o pior resultado obtido.
Se você está tentando intimidar um inimigo enquanto está amarrado, 
seu teste será com desvantagem, pois seu adversário 
possui uma vantagem sobre você. Outro exemplo é se 
você está procurando uma trilha em uma mata fechada e
 possui um companheiro lhe auxiliando nesta função. 
 Como você está obtendo ajuda, ambos rolam o teste com vantagem.\033[m''')
            input('>> ')
            os.system('cls')

        
        elif op == 6:
            print('>>>>>\033[1;36mInspiração\033[m')
            print('''\033[1;34mInspiração é quando o jogador consegue interpretar 
seu personagem como definido pelos seus ideais, 
vínculos, habilidades e etc. Ao fazer isso corretamente, 
 o mestre pode optar por dar pontos de inspiração a um jogador, 
o que garante vantagem em uma única rolagem, não sendo cumulativa.
Também é permitido que os jogadores doem inspiração uns aos outros, 
se assim o mestre preferir.\033[m''')
            input('>> ')
            os.system('cls')

        
        elif op == 7:
            print('>>>>>>>\033[1;36mTestes passivos\033[m')
            print('''\033[1;34mSegundo as regras d&d 5e, 
teste passivo é um tipo de teste em que não é envolvido 
a rolagem de dados. Podendo representar o resultado 
 médio de uma tarefa contínua, como a procura de portas secretas.
O cálculo feito é 10 + modificadores + vantagem (+5) ou desvantagem (-5).
É comum que os personagens que tenham uma percepção maior compreendam antes 
do que os seus companheiros o que está acontecendo na cena.
Por exemplo: digamos que o Ranger do grupo tem uma percepção de 17\033[m''')
            input('>> ')
            os.system('cls')
        

        elif op == 8:
            print('>>>>>\033[1;36mAções livres\033[m')
            print('''\033[1;34mSacar sua arma, pegar uma poção da mochila e etc. 
Execuções  desse tipo não precisam de uma ação\033[m''')
            input('>> ')
            os.system('cls')

        
        elif op == 9:
            
            print('>>>>\033[1;36mReações\033[m')
            print('''\033[1;34mÉ permitido apenas uma reação por rodada. 
Para ter outra reação, é necessário esperar o início do seu próximo
turno.Essas são algumas das principais regras d&d 5e. 
Por se tratar de um conteúdo muito extenso, 
o RPG Next criou um podcast exclusivo para comentar 
as regras do jogo. Conheça a nossa categoria
de podcasts sobre as regras d&d 5e. 
Acesse Regras d&d 5e e confira!\033[m''')
            input('>> ')
            os.system('cls')

def classes():
    ...
