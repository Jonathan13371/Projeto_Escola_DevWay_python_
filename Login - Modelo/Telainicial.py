import os
from TelaLoginProf import TelaLoginProf
from telaloginAluno import TelaLoginAluno


class TelaInicial():
    

    def __init__(self):
        opcao = 0
        while (opcao!= 3):
            
            print(50*'=')
            print('Escola DevWay'.center(50))
            print(50*'=')

            print('1 - Àrea do Professor ')
            print('2 - Àrea do Aluno ')
            print('3 - Sair ')

            opcao= int(input('')) 
            os.system('cls')
                    
            
            if (opcao == 1):
               telaProf = TelaLoginProf()

            if (opcao == 2):
               telaAluno = TelaLoginAluno()    

            if (opcao == 3):
                print(50*'=')
                print('Escola DevWay'.center(50))
                print(' Volte Sempre !!'.center(50))
                print(50*'=')


