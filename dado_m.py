from random import randint

def menu():

    list = ['Rodar dado']
    print('================================')
    print('================================')
    
    for v in range(len(list)):
        print(F'{v + 1}: {list[v]}')
    
    print('================================')
    print('================================')



def dado_um(v):
    try:
        da = randint(1, v)
        print(da)
    except:
        print('comando invalido')


def dado_varios(v, c):
    list = []
    try:
        for v in range(0, v):
            list.append(randint(1, c))
        print(list)
    except:
        print('comando invalido')
        


        


def linha():
    print('=================================')