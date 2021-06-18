# docker-simple-example-
anotações pertinentes 

#######################################################
					Docker
					
Comandos do docker

-P ou -p = mapear a porta usando o parâmetro 
--name = definir um nome para o container com o parâmetro 
-d = rodar o container no modo detached com o parâmetro
run -it = conecta o terminal que estamos utilizando com o do container.
it = entra no terminal do container
ps = listar todos os containers Ativos
ps -a = listar todos os containers
rm ID_CONTAINER = remove o container com id em questão.
container prune = remove todos os containers que estão parados.
rm -f = remove e força o stop
rmi = remove a imagem passada como parâmetro.
rmi $(docker images -q -f "dangling=true") = limpa imagens antigas do disco
network create --driver bridge minha-rede = criar rede local
run -it --name meu-container-de-ubuntu --network minha-rede ubuntu = conectando meu-container-de-ubuntu a minha rede
run -it --name segundo-ubuntu --network minha-rede ubuntu = conectando segundo-ubuntu a minha rede
hostname -i = mostra o ip atribuído ao container pelo docker (funciona apenas dentro do container).
network create --driver bridge NOME_DA_REDE = cria uma rede especificando o driver desejado.
run -it --name NOME_CONTAINER --network NOME_DA_REDE NOME_IMAGEM - cria um container especificando seu nome e qual rede deverá ser usada.

######################################################
				DockerFile
				
FROM python:3 = Referencia uma imagem existente
MAINTAINER William Barrilli = nome do criador
COPY . = Como queremos copiar tudo o que está dentro da pasta
RUN npm install = queremos que a própria imagem instale as dependências para nós, rodando o comando npm install
RUN mkdir /opt/exemplo = queremos que a própria imagem crie os arquivos ao iniciar
ENTRYPOINT npm start = quando a mesma inicia, e o comando que utilizamos na aula anterior foi o npm start, Também podemos passar o comando como se fosse em um array, por exemplo ["npm", "start"]
EXPOSE 5000 colocarmos a porta em que a aplicação executará, a porta em que ela ficará exposta.
WORKDIR /opt/exemplo = através do WORKDIR, assim que copiarmos o projeto, dizemos em qual diretório iremos trabalhar
CMD ["-g", "daemon off;"] = comandos extras
----------------------Build-------------------------
docker build -f NOME_ARQUIVO -t NOME_IMAGEM . = Buildar a imagem do diretorio atual
docker build -f Dockerfile - cria uma imagem a partir de um Dockerfile.
docker build -f CAMINHO_DOCKERFILE/Dockerfile -t NOME_USUARIO/NOME_IMAGEM - constrói e nomeia uma imagem não-oficial informando o caminho para o Dockerfile.
docker login - inicia o processo de login no Docker Hub.
docker push NOME_USUARIO/NOME_IMAGEM - envia a imagem criada para o Docker Hub.
docker pull NOME_USUARIO/NOME_IMAGEM - baixa a imagem desejada do Docker Hub.

----------------------Compose-------------------------

version: '3' = Versão usada do compose
services: = serviços
    nginx: = Nome do serrviço 
        build: = comando para buildar
            dockerfile: ./Dockerfile = local do docker file para buildar
            context: . = onde executar
        image: pythao_compose = nome da imagem
        container_name: python = nome container
        ports: = porta da do container
            - "5000:5000" = porta local:por container (o "-" servepra indicar mais de um item)
        networks:  = network para ligação dos containers
            - newtork-do-papi = nome da rede 

    postgres:
        image: postgres
        networks: 
            - newtork-do-papi 
        ports: 
            - "5432:5432"

networks: = criação da rede
    newtork-do-papi: = nome da rede
        driver: bridge = driver da rede

docker-compose ps = podemos ter uma visualização simples dos serviços que estão rodando
docker-compose build = Realiza o build dos serviços relacionados ao arquivo docker-compose.yml, assim como verifica a sua sintaxe.
docker-compose up -d  = sem logs
docker-compose up = Sobe todos os containers relacionados ao docker-compose, desde que o build já tenha sido executado.
docker-compose down = Para todos os serviços em execução que estejam relacionados ao arquivo docker-compose.yml.