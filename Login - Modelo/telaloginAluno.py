import os 
from aluno import Aluno
from alunoDAO import AlunoDAO
from telaPrincipalAluno import TelaPrincipalAluno

class TelaLoginAluno():

    def __init__(self) :
            
            self.__usu =Aluno() 

            self.__usuDAO = AlunoDAO()
            opcao = 'S'
            while (opcao!= 'N'):   
                print(50*'=')
                print('Escola DevWay'.center(50))
                print('Área Do Aluno'.center(50))
                print(50*'=')

                self.__usu.loginAluno = input('Login:')
                self.__usu.senhaAluno = input('Senha:')
                os.system('cls')


                
                self.__usuDAO.usu = self.__usu

            
                if ( self.__usuDAO.logarAluno() == True):
                    os.system('cls')
                    respAluno = self.__usuDAO.usu
                    telaa=TelaPrincipalAluno(respAluno)
                
                else:
                    
                    print(50*"=")
                    print("Aluno não cadastrado".center(50))
                    print(50*"=")

                    opcao = input('Deseja tentar Novamente [S/N]:').upper()
                    os.system('cls')
           
               
                
                
            
            