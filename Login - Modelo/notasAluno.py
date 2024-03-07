class NotasAluno():
    __idNota = int
    __disciplina = str
    __media = float
    __faltas= int 
    __idAluno = int



    @property
    def disciplina(self):
        return self.__disciplina

    @disciplina.setter
    def disciplina(self, disciplina):
        self.__disciplina = disciplina


    @property
    def media(self):
        return self.__media

    @media.setter
    def media(self, media):
        self.__media = media 

    @property
    def faltas(self):
        return self.__faltas

    @faltas.setter
    def faltas(self, faltas):
        self.__faltas = faltas    

    @property
    def idAluno(self):
        return self.__idAluno

    @idAluno.setter
    def idAluno(self, idAluno):
        self.__idAluno = idAluno    

    @property
    def idNota(self):
        return self.__idNota

    @idNota.setter
    def idNota(self, idNota):
       self.__idNota = idNota         