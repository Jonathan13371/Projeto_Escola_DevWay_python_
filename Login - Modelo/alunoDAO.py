from aluno import Aluno
from notasAluno import NotasAluno

import mysql.connector 


class AlunoDAO():
    __usu = Aluno()
    __use = NotasAluno()
   
   
    
    @property 
    def usu(self):
        return self.__usu

    @usu.setter
    def usu(self, usu):
        self.__usu = usu
    
    @property 
    def use(self):
        return self.__use
  
    @use.setter
    def use(self, use):
        self.__use = use
    
   
    
   
    def __init__(self):
            
        self.__conexao =mysql.connector.connect( 
        host='127.0.0.1',
        database='escola',
        user='root',
        password='Apocalypse3@'

        )
        self.__cursor = self.__conexao.cursor()
        
    def fecharConexao(self):
        self.__cursor.close()
        self.__conexao.close()        
    
    def logarAluno(self):
        sql = 'select * from alunos where  loginAluno=%s and senhaAluno=%s'
        sqlDados = (self.__usu.loginAluno,self.__usu.senhaAluno)
        self.__cursor.execute(sql, sqlDados)
        resp= self.__cursor.fetchone()
        
        if( resp == None):
            return False
        else:
            #armazenar no OBJ modelo a resposta
            self.__usu.idAluno = resp[0]
            self.__usu.nomeAluno = resp[1]
            self.__usu.loginAluno= resp[2]
            self.__usu.senhaAluno= resp[3]
          
            return True
    
    def alunoPrincipal(self):
        sql = 'select  nomeAluno,disciplina,media,qtdFaltas from alunos,notas where alunos.idAluno=notas.idAlunoFk and alunos.idAluno=' + str(self.__usu.idAluno)
        
        self.__cursor.execute(sql)
        return self.__cursor 
        
       

    def pesquisarNome(self):
        sql='select * from alunos where nomeAluno='+str(self.__usu.nomeAluno)
        self.__cursor.execute(sql)     
        respBD = self.__cursor.fetchone()
        self.__usu.idAluno = respBD[0]
        self.__usu.nomeAluno = respBD[1]
        self.__usu.loginAluno= respBD[2]
        self.__usu.senhaAluno = respBD[3]   


    def pesquisarID(self):
        sql='select * from alunos where idAluno='+str(self.__usu.idAluno)
        self.__cursor.execute(sql)     
        respBD = self.__cursor.fetchone()
        self.__usu.idAluno = respBD[0]
        self.__usu.nomeAluno = respBD[1]
        self.__usu.loginAluno= respBD[2]
        self.__usu.senhaAluno = respBD[3]        


    def cadastrarAluno(self):
        sql = 'insert into alunos values ( 0, %s , %s,%s )'   
        sqlDados =(self.__usu.nomeAluno,self.__usu.loginAluno,self.__usu.senhaAluno) 
        self.__cursor.execute(sql, sqlDados)
        self.__conexao.commit()

    
    

    def pesquisarAluno(self):
        sql='select * from alunos where nomeAluno="'+ self.__usu.nomeAluno+'"'
        self.__cursor.execute(sql)
        return self.__cursor    

    def pesquisarAlunoNotasID(self):
        sql='select * from notas where idAlunoFk='+str(self.__use.idAluno)
        self.__cursor.execute(sql)
        return self.__cursor         
    
    def pesquisarNotasID(self):
        sql='select * from notas where idNota='+str(self.__use.idNota)
        self.__cursor.execute(sql)
        respBD = self.__cursor.fetchone()
        self.__use.idNota = respBD[0]
        self.__use.disciplina = respBD[1]
        self.__use.media= respBD[2]
        self.__use.faltas = respBD[3] 
        self.__use.idAluno = respBD[4]      


    def AlterarAluno(self):
        sql ='update alunos set nomeAluno=%s, loginAluno=%s, senhaAluno=%s where idAluno=%s ' # primeiro eu digo a tabela que quero atualizar depois 
        # como quis atributos quero alterar e no final eu coloco o id da coluna que desejo fazer alteração
        sqlDados = (self.__usu.nomeAluno, self.__usu.loginAluno,self.__usu.senhaAluno, self.__usu.idAluno)
        self.__cursor.execute(sql,sqlDados)
        self.__conexao.commit()  

    def AlterarNotas(self):
        sql ='update notas set disciplina=%s, media=%s, qtdFaltas=%s where idNota=%s ' # primeiro eu digo a tabela que quero atualizar depois 
        # como quis atributos quero alterar e no final eu coloco o id da coluna que desejo fazer alteração
        sqlDados = (self.__use.disciplina, self.__use.media,self.__use.faltas, self.__use.idNota)
        self.__cursor.execute(sql,sqlDados)
        self.__conexao.commit()        
   


    def excluirAlunoID(self):
        sql = 'delete from alunos where idAluno=' + str (self.__usu.idAluno )
        self.__cursor.execute(sql)
        self.__conexao.commit()

    def excluirNota(self):
        sql = 'delete from notas where idNota=' + str (self.__use.idNota )
        self.__cursor.execute(sql)
        self.__conexao.commit()    


    def cadastrarNotas(self):
        sql = 'insert into notas values ( 0, %s , %s,%s, %s)'   
        sqlDados =(self.__use.disciplina,self.__use.media,self.__use.faltas, self.__usu.idAluno) 
        self.__cursor.execute(sql, sqlDados)
        self.__conexao.commit()    
    
    def verificar(self,idNota):
       sql=' select * from notas where idNota=%s and idAlunoFk=%s'
       sqlDados =(idNota,self.__use.idAluno)
       self.__cursor.execute(sql,sqlDados)
       result= self.__cursor.fetchone() 
       return result is not None

    def verificarIDAluno(self,idAluno):
        sql ='select * from notas where idAlunoFk=%s' 
        sqlDados=(idAluno,)
        self.__cursor.execute(sql, sqlDados)
        result= self.__cursor.fetchone() 
        return result is not None

    def verificarID(self,idAluno):
        sql = 'select * from alunos where idAluno=%s'
        sqlDados = (idAluno,)
        self.__cursor.execute(sql, sqlDados)
        result = self.__cursor.fetchone()
        return result is not None 
