---

# Crud com Python com framework Flask e SQL Server

---

### Nesse programa iremos fazer um Crud com Python ( Flask ) e o banco de dados sql server. Funcionando no Windows e Linux ( apt ).

### Antes de tudo teremos que baixar o python e o sql server. Abaixo terá os links.

### Python

[Download Python](https://www.python.org/downloads/)

### SQL Server

[Downloads do SQL Server | Microsoft](https://www.microsoft.com/pt-br/sql-server/sql-server-downloads)

---

### Sobre a questão da versão testada, está funcionando no python ( 3.9.5 ) e o SQL Server 19.

---

### Após as instalações faça um clone do repositório e abra os arquivos no seu editor de texto, abaixo tem um link do vscode.

### Visual Studio

[Download Visual Studio Code - Mac, Linux, Windows](https://code.visualstudio.com/download)

---

### No final teremos algo como assim.

imagem - tela.png

### A seguir é necessario instalar algumas bibliotecas para o python, para fazer isso usaremos o "pip" onde o mesmo é instalado automaticamente no Windows, sendo assim apenas temos que instalar o "Flask" pelo terminal. Abaixo veremos como instalamos para Linux no terminal, qualquer dúvida segue a documentação do pip abaixo.

[Installation - pip documentation v21.2.2](https://pip.pypa.io/en/stable/installation/)

---

Windows ( Microsoft ODBC Driver 17 )

[Microsoft® ODBC Driver 17 for SQL Server® - Windows, Linux e macOS](https://www.microsoft.com/pt-BR/download/details.aspx?id=56567)

```powershell
pip install flask
pip install requests
```

Linux

```
sudo apt install python3-pip
sudo apt install python3-pyodbc
pip3 install flask
pip3 install requests
```

---

### Configure o seu banco de dados com as suas informações: server, database, username e password de sua preferência. Qualquer dúvida documentação do SQL Server abaixo.

imagem - conexao.png

### Documentação do SQL Server

[Documentação do Microsoft SQL - SQL Server](https://docs.microsoft.com/pt-br/sql/?view=sql-server-ver15)

---

### Pronto, com as bibliotecas instaladas e banco configurado podemos agora executar o código.

---

### Essa é a tela inicial quando o programa executa, clique com o ctrl esquerdo + clique esquerdo do mouse ou digite na url no seu navegador http://127.0.0.1:500/

imagem - executando.png

---

### Depois de iniciar, veremos uma tela onde podemos cadastrar um aluno

imagem - cadastro.png

---

### Após cadastrar seremos redirecionados para uma tela de login, onde podemos fazer nosso login com o aluno novo.

imagem - login.png

---

### Por padrão já existe alunos cadastrado para o teste, tendo também um usuário Adiministrador para olharmos todos os alunos cadastrados

imagem - admin.png

---

### Agora com o nosso aluno logado, temos as seguites opções: Editar ou Deletar esse aluno.

imagem - editar-delete.png

---

### Editando Aluno

imagem - editar.png

---

### Deletando Aluno

imagem - delete.png

# Assim terminando. Agradeço! [❤](https://www.notion.so/PostgresqlWithPython-b08d46e640404827928210116a2e3fd7)
