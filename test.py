import pyodbc # Conexao para o Python ( Connection to Python )

#***************************************************************************#

#                                 SLQ Sever                                 #


# Faz a conexão do Python e SQL Server. ( Does the Python and SQL Server connection )
def conexao(self):
    self.server = 'dan-pc' 
    self.database = 'Alunos'
    self.username = 'SA'
    self.password = ''
    self.cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+self.server+';DATABASE='+self.database+';UID='+self.username+';PWD='+self.password)      
    self.cursor = self.cnxn.cursor()
    self.cursor.execute(self.exeSQL)
    
#***************************************************************************#
# Classe Aluno faz a conexao com as colunas no SQL Server. ( Student Class Connects to Columns in SQL Server )
class Aluno():
    def __init__(self, nomeC, dataN, idade, inserir_genero, email, obje):
        self.nome_completo = nomeC
        self.data_de_nascimento = dataN
        self.idade = idade
        self.inserir_genero = inserir_genero
        self.email = email
        self.objetivo_da_graduacao = obje
        
#***************************************************************************#
# Seleciona todas as colunas. ( Select all columns )
    def selecao(self):
        self.exeSQL = "select nome_completo, data_de_nascimento, idade, inserir_genero, email, objetivo_da_graduacao from t_alunos where email = '{}'".format(self.email)
        conexao(self)
        result = self.cursor.fetchall()
        for row in result:
            print(row.nome_completo, ' | ', row.data_de_nascimento, ' | ', row.idade, ' | ', row.inserir_genero, ' | ', row.email, ' | ', row.objetivo_da_graduacao)
        self.cursor.commit()
        self.cursor.close()
        
#***************************************************************************#
# Seleciona apenas o nome e o email na tabela t_alunos no SQL Server. ( Selects only the name and email in the table t_alunos in SQL Server )
    def selecaoEmail(self):
        self.exeSQL = "select nome_completo, email from t_alunos"
        conexao(self)
        result = self.cursor.fetchall() 
        for row in result:
            print(row.nome_completo, ' | ', row.email)
        self.cursor.commit()
        self.cursor.close() 
#***************************************************************************#
# inserindo dados informados. ( entering informed data )
    def InserirAluno(self):
        self.exeSQL = "INSERT INTO t_alunos (nome_completo, data_de_nascimento, idade, inserir_genero, email, objetivo_da_graduacao) VALUES ('{}','{}','{}','{}','{}','{}')".format(self.nome_completo, self.data_de_nascimento, self.idade, self.inserir_genero, self.email, self.objetivo_da_graduacao)
        conexao(self)
        self.cursor.commit()
        self.cursor.close()
        
#***************************************************************************#
# Alterando dados ou "UPDATE" ( Changing data )
    def AlterarInformacao(self):
        self.exeSQL = "update t_alunos set "
        if (self.nome_completo != ''):
            self.exeSQL += "nome_completo = '{}', ".format(self.nome_completo)
        if (self.data_de_nascimento != ''):
            self.exeSQL += "data_de_nascimento = '{}', ".format(self.data_de_nascimento)
        if (self.idade != ''):
            self.exeSQL += "idade = '{}', ".format(self.idade)
        if (self.inserir_genero != ''):
            self.exeSQL += "inserir_genero = '{}', ".format(self.inserir_genero)
        if (self.email != ''):
            self.exeSQL += "email = '{}', ".format(self.email)
        if (self.objetivo_da_graduacao != ''):
            self.exeSQL += "objetivo_da_graduacao = '{}', ".format(self.objetivo_da_graduacao)
        self.exeSQL = self.exeSQL[:-2]
        self.exeSQL += " WHERE email = '{}'".format(self.email)
        conexao(self)
        self.cursor.commit()
        self.cursor.close()
        
#***************************************************************************#
# Deletando os dados do aluno escolhido. ( Deleting the data of the chosen student )
    def DeletarInformacao(self): 
        self.exeSQL = "delete from t_alunos where email = '{}';".format(self.email)
        conexao(self)
        self.cursor.commit()
        self.cursor.close()

#***************************************************************************#

#                                 Python                                    #

# Adiciona o Titulo. ( Title )
def titulo():
    centro = 'Faisp - Faculdade interativa'
    print('===' * 35)
    print(centro.rjust(60))
    print('===' * 35)
    
#***************************************************************************#
# Adiciona a linha ( Row )
def linha():
    print('---' * 35)

#***************************************************************************#
# Variaveis ( Variables )
def tela(opcao):
    email = input("Digite seu email: ")
    nomeC = str(input('Informe o seu Nome Completo: ')).strip().capitalize()
    dataN = input('Informe a sua Data de Naciomento: ')
    idade = int(input('Informe a sua Idade: '))
    inserir_genero = int(input('informe o seu Sexo [Digite "1" para Masculino/ Digite "2" para Feminino]: '))
    obje = str(input('Qual e o seu Objetivo nessa Graduação: ')).strip()
    aluno = Aluno(nomeC, dataN, idade, inserir_genero, email, obje)
    if opcao == '1':
        aluno.InserirAluno()
        print('Usuario Cadastrado com sucesso')
        resposta = str(input('Quer cadastrar mais [s/n]: ')).strip().upper()[0]
        if resposta == 'S':
            tela(opcao)
    else:
       aluno.AlterarInformacao()
       print('Usuario Alterado com sucesso')
       linha()

opcao = 0
op = 0
titulo()
while opcao != 5:
    print('''[ 1 ] incluir um Aluno(a).
[ 2 ] Editar Aluno.
[ 3 ] Excluir Aluno.
[ 4 ] Listar E-mail Cadastrados.
[ 5 ] Finaliza o Programa.''')
    linha()
    opcao = input('Qual e a opção: ')
    linha()
    while opcao not in '1' '2' '3' '4' '5':
        opcao = input('Qual e a opção: ')
        linha()
# Opção "1"
    if opcao == '1':
        tela(opcao)

        titulo()
        
        
# Opção "2"
    if opcao == '2':
        tela(opcao)

        
# Opção "3"
    if opcao == '3':
        aluno = Aluno("","","","","","")
        aluno.selecaoEmail()
        email = input('Informe o email para deletar: ')
        aluno = Aluno("","","","",email,"")
        if (input('Tem certeza que deseja excluir esse usuário? Essa ação não poderá ser desfeita (s/n): ') == 's'):
            aluno.DeletarInformacao()
            print('Usuario excluido com sucesso')
        linha()
        
# Opção "4"
    if opcao == '4':
        deletar = input('Informe o seu E-mail: ')
        aluno = Aluno("","","","",deletar,"")
        aluno.selecao()
        linha()
        
# Opção "5"
    if opcao == '5':
        print('Fim do Programa! Obrigado!!')

