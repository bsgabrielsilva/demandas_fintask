# Teste para Fintask

Projeto escrito utilizando a linguagem Python3 com o Framework Django 2.2. O intuito deste teste é de participar do processo de seleção para a vaga de Desenvolvedor(tech leader?) da Fintask. 

## Instruções para rodar este projeto

### Utilizando o Docker
1° Faça um clone deste repositório:
```
$ git clone https://github.com/bsgabrielsilva/demandas_fintask.git
```
2° Em seguida, abra seu terminal dentro da pasta demandas_fintask e rode o docker-compose(se necessário, use o sudo, por gentileza):
```
$ docker-compose up
```
3° Se tudo ocorrer bem, abra seu navegador e digite http://localhost:8000

4º Para acessar o painel administrativo(http://localhost:8000/admin), use: 
```
username: bsgabrielsilva
password: 123Mudar
``` 

### Instruções caso o docker-compose up falhe(espero que não)
1° Faça um clone deste repositório:
```
$ git clone https://github.com/bsgabrielsilva/demandas_fintask.git
```
2° Em seguida, abra seu terminal dentro da pasta demandas_fintask, crie um ambiente virtual de desenvolvimento(de sua preferência, eu gosto do virtualwrapper) e após criar, rode:
```
$ pip install -r requirements.txt
```
3º Rode em seguida a sequência de comandos:
```
$ cp .env-test .env  
$ python manage.py migrate  
$ python manage.py loaddata cidades.json  
$ python manage.py loaddata user.json  
$ python manage.py test   
$ python manage.py runserver 0.0.0.0:8000
```
4° Se tudo ocorrer bem, abra seu navegador e digite http://localhost:8000

5º Para acessar o painel administrativo(http://localhost:8000/admin), use: 
```
username: bsgabrielsilva
password: 123Mudar
``` 

### Cobertura do docker-compose

Ao executar o **docker-compose up**, serão chamados em sequência: **Dockerfile** que instalará as dependências do projeto e concederá permissões para execução como programa ao script **docker-entrypoint.sh**, esse por sua vez, adicionará o arquivo .env ao projeto, e criará uma base de dados **.sqlite3** para migração das tabelas, bem como carregará os dados pré-definidos em fixtures do projeto. Todos os arquivos citados, estão presentes na raiz do projeto. 

### Cobertura de testes
A cobertura de testes está atrelada à API, e possuí cobertura a listagem de cidades e cadastro, edição, listagem, informações, finalização e remoção de demandas. Por conveniência, a execução dos testes, está presente no arquivo **docker-entrypoint.sh**, na linha 18, como uma das etapas na execução do sistema com o **docker-compose up**.

Caso seja necessário executar manualmente, recomendo executar no container, ou executar fora dele, em todos os casos, funcionará(depois de criar um banco, migrar as tabelas, carregas os dados pré-definidos em fixtures). 

### Cobertura no Postman e das API's
A cobertura no postman, através de collection também é possível, e está presente na pasta **/docs**. Um ponto a se considerar, é que a collection está parcialmente automatizada. O cadastro de usuários e login, fazem parte do processo de criação de usuário e obtenção do token para acessar os endpoints da api. Durante a obtenção do token, ao obter status code igual à 200, ele vai setar automaticamente a variável da collection **demandas_token** o prefixo do token e o token gerado pela api.

O processo citado acima, se refere aos endpoints:

- **/api/registro/ [POST]** => Registrar um usuário
- **/api/login/ [POST]** => Obter o token do usuário, com usuário e senha;

Feito isso, os demais endpoints possuem também automatização para setar os valores dos cabeçalhos e dos parâmetros que compõem o restante dos endpoints. E todos os demais, precisam do token do usuário no cabeçalho de autorização; 

A autenticação e o token gerados para o usuário, são usando a biblioteca **authtoken** do **djangorestframework**, seguindo o padrão de cabeçalho: 

- **Authorization**: Token token_do_usuario

Os demais endpoints são:

- **/api/cidades/ [GET]** => Trazer todas as cidades, com opção de pesquisa **?cidade=** para uma cidade em específico, utilizando o filtro do django ORM **icontains** para realizar a busca 
- **/api/demandas/ [POST][GET] [PUT][DELETE]** => Cadastro, Edição, Listagem(de todas ou por Id) e remoção de demandas. É importante enfatizar que todo o processo, corresponde a filtragem de demandas pelo usuário que a criou, então, não se tornando possível listar, alterar ou remover as demandas de outro usuário, a não ser, o do próprio criador da demanda. 
- **/api/finalizar_demanda/{id} [PUT]** => Finalizar a demanda. Somente o usuário que a criou, pode finalizá-la. O endpoint, só aceitará o status **Finalizada**. Caso a demanda já esteja finalizada, ele retornará **Demanda já finalizada!**. 

Os body's de cada endpoint, está disponível na collection do postman na pasta **/docs** do projeto.

## Considerações

Acredito que o projeto está dentro do escopo do desafio. Adicionei algumas informações para melhor detalhar os requisitos, como a inserção de novos campos para endereço previsto na Demanda. Algumas inserções  Nos serializers da api, eu utilizei as heranças do POO do python, para simplificar e deixar mais enxuto a criação de serializers para os modelViewsets e outras coisas mais que podemos discutir depois, pois as questões de organizações de projetos de software, é uma praia que gosto de aprender com as visões das pessoas com experiência nessa área.

Aproveitando, a forma em que o projeto foi organizado, é a maneira como trabalhamos atualmente aqui. Em que dividimos a responsabilidade do módulos, em pacotes do próprio python, é uma abstração própria, que segue o princípio de projetos orientado a objetos, no que tange a projeto. Isso facilita demais na manutenção de algumas funções e classes. 

Enfim, espero ser aprovado e vamos que vamos! 
