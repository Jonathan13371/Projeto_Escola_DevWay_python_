from professores import Professores
from profDAO import ProfDAO
from telaGestao  import TelaGestao
import os 
class TelaLoginProf():
    

    def __init__(self):
        
            self.__usu =Professores() 

            self.__usuDAO = ProfDAO()
            opcao='S'
            
            
            while opcao!='N':
               
                print(50*'=')
                print('Escola DevWay'.center(50))
                print('Área do Professor'.center(50))
                print(50*'=')
                
                self.__usu.loginProf = input("    Login: ")
                self.__usu.senhaProf = input("    Senha: ")
                
                
                self.__usuDAO.usu = self.__usu

                
                if ( self.__usuDAO.logarProf() == True):
                    os.system('cls')
                    print("             Bem vindo Professor " + self.__usuDAO.usu.nomeProf + " !!!!!!")
                    

                    telaG=TelaGestao()
                else:
                    os.system('cls')
                    print("================================================")
                    print("          Usuário não cadastrado")
                    print("================================================")
                    opcao = input('Deseja tentar Novamente [S/N]:').upper()
                    os.system('cls')
                    
               
            self.__usuDAO.fecharConexao     
