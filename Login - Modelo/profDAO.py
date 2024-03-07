from professores import Professores

import mysql.connector  

class ProfDAO():
    __usu = Professores()
    
    @property 
    def usu(self):
            return self.__usu

    @usu.setter
    def usu(self, usu):
            self.__usu = usu
    
   
    
    
    def __init__(self):
            
            self.__conexao =mysql.connector.connect( 
            host='127.0.0.1',
            database='escola',
            user='root',
            password='***********'

            )
            self.__cursor = self.__conexao.cursor()
        
        
    
    def fecharConexao(self):
        self.__cursor.close()
        self.__conexao.close()
    
    def logarProf(self):
        sql = 'select * from professores where  loginProf=%s and senhaProf=%s'
        sqlDados = (self.__usu.loginProf,self.__usu.senhaProf)
        self.__cursor.execute(sql, sqlDados)
        resp = self.__cursor.fetchone()


        
       
        if( resp == None):
            return False
        else:
            #armazenar no OBJ modelo a resposta
            self.__usu.idProf = resp[0]
            self.__usu.nomeProf = resp[1]
            self.__usu.loginProf = resp[2]
            self.__usu.senhaProf =resp[3]
            return True

    
     
