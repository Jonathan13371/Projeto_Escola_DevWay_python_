from aluno import Aluno
from alunoDAO import AlunoDAO
import os 
class CadastrarNotas():
    def __init__(self):
        
        self.__usu = Aluno()
        self.__usuDAO = AlunoDAO()
        

        opcao = 'S'
        while opcao != 'N':
                print(50 * '=')
                print('Escola DevWay'.center(50))
                print('Área Do Professor - Cadastrar Notas'.center(50))
                print(50 * '=')
                print('')
                
                
                
                self.__usu.nomeAluno = input('Digite o nome do aluno que deseja cadastrar a nota: ')
                self.__usuDAO.usu = self.__usu

                listaPes = self.__usuDAO.pesquisarAluno()
                for(idAluno,nomeAluno,loginAluno,senhaAluno) in listaPes:
                    print("==========================================")
                    print('ID do Aluno: ' + str(idAluno))
                    print("Nome  do Aluno: " + nomeAluno)
                    

                    print("==========================================")
                else:
                     listaPes.fetchone()
                     qtdItens = listaPes.rowcount.numerator
                if qtdItens == 0:
                    os.system('cls')
                    print("==========================================")
                    print("      Aluno Não encontrado !!! ")
                    print("==========================================")
                    opcao = input("Deseja Tentar Novamente [S/N]? ").upper()

                else:               
                    
                    self.__usuDAO.use.disciplina = ''
                    while not self.__usuDAO.use.disciplina.isalpha():
                        self.__usuDAO.use.disciplina = input('Nome da disciplina: ')
                        
                        if not self.__usuDAO.use.disciplina.isalpha():
                            print('Voce está tentando digitar numeros para o nome da disciplina ou voce não estar digitando nada!')
                            print('Por favor Digite apenas letras!')
             
                    
                    
                        
                    try:
                        self.__usuDAO.use.media = float(input('Media: '))
                    except ValueError:
                        print('Erro: você precisa inserir um número para a média')
                        self.__usuDAO.use.media = None

                    if self.__usuDAO.use.media == None:
                        while self.__usuDAO.use.media == None:
                            try:
                                self.__usuDAO.use.media = float(input('Media: '))
                            except ValueError:
                                print('Erro: você precisa inserir um número para a média')
                                self.__usuDAO.use.media = None
                
                
                    try:
                        self.__usuDAO.use.faltas = int(input('Quantidade de Faltas: '))          
                    except ValueError:
                            print('Erro voce precisa cadastrar quantidade de faltas')                               
                            self.__usuDAO.use.faltas = None
                        
                    if self.__usuDAO.use.faltas == None:
                            while self.__usuDAO.use.faltas == None:     
                             try:
                              self.__usuDAO.use.faltas =  int (input('Quantidade de Faltas: ')) 
                             except ValueError:
                                print('Voce precisa cadastrar a quantidade de faltas:')
                                self.__usuDAO.use.faltas = None

                                                  
                    try:
                        self.__usuDAO.usu.idAluno = int(input(f'Qual o ID do Aluno {self.__usuDAO.usu.nomeAluno}: '))
                    except ValueError:
                        print(f'Digite um valor numerico para o ID do {self.__usuDAO.usu.nomeAluno} ! ')    
                        self.__usuDAO.usu.idAluno = None   
                        
                    if self.__usuDAO.usu.idAluno ==None:
                        while self.__usuDAO.usu.idAluno ==None:
                         print('Voce Precisa informar o ID do Aluno:')
                         print('')
                         try:
                             self.__usuDAO.usu.idAluno = int(input(f'Qual o ID do Aluno {self.__usuDAO.usu.nomeAluno}: '))  
                                
                         except ValueError:
                            print(f'Digite um valor numerico para o ID do {self.__usuDAO.usu.nomeAluno} ! ') 
                            self.__usuDAO.usu.idAluno = None    
                
                    self.__usuDAO.usu = self.__usu 
                    verificar = self.__usuDAO.verificarID(self.__usuDAO.usu.idAluno) 
                    if verificar ==True:       
                        self.__usuDAO.cadastrarNotas() 

                        os.system('cls')
                        print("==========================================")
                        print("      Notas Cadastrada com sucesso !!! ")
                        print("==========================================")
                                    
                                
                        opcao = input("Deseja cadastrar nota de outro Aluno [S/N]? ").upper()
                        os.system('cls')
                    else:
                        print('Erro: esse id não coresponte a esse aluno')
                        opcao = input("Deseja tentar novamente [S/N]? ").upper()
                        os.system('cls')
                    
                        
        self.__usuDAO.fecharConexao()            