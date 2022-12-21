from dado_m import menu, dado_um, linha
import os

while True:
    menu()
    op = int(input('>> '))
    os.system('cls')
    if op == 1:
        linha()
        qua = int(input('Quantos dados deseja rodar? '))
        if qua == 1:
            da = int(input('dado de quanto? '))
            dado_um(da)
            linha()
            input('Enter pra voltar ')
        


    os.system('cls')
