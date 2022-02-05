# Shelter 
<h1 align="center">
    <a href="https://pt-br.reactjs.org/">🔗 Python</a>
</h1>
<p align="center">🚀 Um sistema em DJANGO</p>

<h4 align="center"> 
	🚧 Em construção...  🚧
</h4>

### Features

- [X] Importar o conteúdo de um arquivo .CSV
- [X] Exibir as informações como tabelas e/ou gráficos, de forma a facilitar o trabalho de análise e priorização das vulnerabilidades a serem corrigidas, devem existir visões por ativo e por ambiente.
- [ ] Gerar uma métrica de risco para o host.
- [ ] Gerar uma média de risco do ambiente.
- [ ] O usuário irá marcar quando uma vulnerabilidade foi corrigida.

**Caracteristicas da API:**
- [x] As APIs devem possuir paginação de 50 elementos.
- [X] Realizar filtragens e ordenações.
- [ ] Não devem permitir modificação dos dados dos hosts e vulnerabilidades, apenas para mudança de seus status (corrigida e não corrigida)

### Requirements
asgiref==3.5.0<br>
Django==4.0.1<br>
djangorestframework==3.13.1<br>
greenlet==1.1.2<br>
numpy==1.22.1<br>
pandas==1.4.0<br>
python-dateutil==2.8.2<br>
pytz==2021.3<br>
six==1.16.0<br>
SQLAlchemy==1.4.31<br>
sqlparse==0.4.2<br>
tzdata==2021.5<br>

### Clone este repositório
$ git clone https://github.com/abrantes32/api_flask_aws.git

### Execute a aplicação em modo de desenvolvimento e acesse a pasta onde se localiza o projeto
$ python -m venv venv<br>
$ call venv\scripts\activate<br>
$ pip install requirements.txt<br>
$ flask run

### Veja o resultado da rota /songs no postman ou o que preferir:
$ localhost:5000/songs?artist_id=349487

# O servidor inciará na porta:5000 - acesse <http://localhost:5000> 


