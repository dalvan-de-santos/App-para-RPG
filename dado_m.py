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
    da = randint(1, v)
    print(da)


def linha():
    print('=================================')