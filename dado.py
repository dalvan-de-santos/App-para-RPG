from dado_m import menu, dado_um, linha, dado_varios, regras
import os

while True:
    try: 
        menu()
        op = int(input('>> '))
        os.system('cls')

        #rolagens
        if op == 1:
            linha()
            qua = int(input('Quantos dados deseja rodar? '))
            if qua == 1:
                da = int(input('dado de quanto? '))
                dado_um(da)
                linha()
                input('Enter pra voltar ')
        
        

        
            elif qua > 1:
                da = int(input('dado de quanto? '))
                dado_varios(qua, da)
                linha()
                input('Enter pra voltar ')
         
        #regras   
        elif op == 2:
            regras()
            os.system('cls')

        



        os.system('cls')
    except:
        print('comando invalido')
        input('>> ')
        os.system('cls')
