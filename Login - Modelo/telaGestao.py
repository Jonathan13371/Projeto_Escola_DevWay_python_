
from gestaoAluno import GestaoAluno   
from gestaoNotas import GestaoNotas

import os 
class TelaGestao():

    def __init__(self):
            opcao = 0
            

            while opcao != 3:
                print(50 * '=')
                print('Escola DevWay'.center(50))
                print('Área Do Professor'.center(50))
                print(50 * '=')
                print('')
                print('')
                
                print('1 - Gestão do Aluno')
                print('2 - Gestão de Notas ')
                print('3 - Sair ')

                opcao = int(input(''))
                

                if (opcao ==1):
                   os.system('cls')
                   telaGA = GestaoAluno()

                
                if opcao ==2:
                  os.system('cls')
                  telaGN = GestaoNotas()
                if opcao ==3:
                  os.system('cls')  
                