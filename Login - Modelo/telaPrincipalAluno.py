import os 
from aluno import Aluno
from alunoDAO import AlunoDAO

class TelaPrincipalAluno():
    def __init__(self,respAluno):
       # respAluno aluno e a resposta do logar aluno, onde eu tenho idAluno,nomeAluno,loginAluno,senhaAluno. 

        self.__usu = Aluno()
        self.__usuDAO = AlunoDAO()

        opcao = 0  
        
       
       
        
        

        while opcao != 3:
            print(50 * '=')
            print('Escola DevWay'.center(50))
            print('Área Do Aluno'.center(50))
            print(50 * '=')
            print('')
            print('')
            
            self.__usuDAO.usu = respAluno
            
            
          
            exibir = self.__usuDAO.alunoPrincipal()
            print('   Disciplina       Média       Faltas ')
            for(nomeAluno,disciplina,media,faltas) in exibir:  
             
              
             print(f'    {disciplina}           {media}              {faltas}')   
               
            else:     
              
              exibir.fetchone()
              qtdItens = exibir.rowcount.numerator
              if qtdItens == 0:
                       
                os.system('cls')       
                print(50*"=")
                print("      O  ALUNO AINDA NAO POSSUI NOTAS DISPONIVEIS!!! ".center(50))
                print(50*"=")
                
                    
            print('3 - Voltar') 
            opcao = int(input(''))
            os.system('cls')
        
             
