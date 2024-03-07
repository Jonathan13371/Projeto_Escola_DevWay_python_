create database escola;
use escola;

create table alunos 
(
	idAluno int auto_increment not null,
    nomeAluno varchar(50),
    loginAluno varchar(30),
    senhaAluno varchar(30),
	primary key(idAluno)

);


create table notas
(
	idNota int auto_increment not null,
    disciplina varchar(50),
    media decimal(10,2),
    qtdFaltas int,
    idAlunoFk int ,
    primary key(idNota),
    foreign key(idAlunoFk) references alunos(idAluno)
);


create table professores

(
	idProf int auto_increment not null,
    nomeProf varchar(50),
    loginProf varchar(30),
    senhaProf varchar(30),
    
    primary key(idProf)
    insert into  professores values(null ,'jose','adm','123');

    insert into  alunos values(null ,'andre','andre','123')
);