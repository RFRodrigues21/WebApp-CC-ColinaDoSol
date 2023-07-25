# WebApp-CC-ColinaSol


![Logomarca CC COLINA SOL - Versão Horizontal Cores RGB 300dpi](https://user-images.githubusercontent.com/79157730/215213134-4db3f2bf-01e7-4772-abde-70f05f2c2bb8.png)

Desenvolvimento do Website e plataforma de gestão do centro comercial Colina do Sol

# Pré requisitos:
  * Python 3.10 ou superior
  * Motor de Base de Dados MySQL
# Instalação:
  Clonar o repositório para a pasta local desejada:
  
    Git Clone https://github.com/CC-ColinaSol/WebApp-CC-ColinaSol.git

  Na directoria root do projeto instalar um ambiente virtual:

    pip install pipenv

  Ativar o ambiente virtual:

    pipenv shell

  Instalar as dependências da aplicação:

    pip install -r requirements.txt

  Adicionar o ficheiro .env na diretoria root do projeto:

    SECRET_KEY=<sua_chave_secreta>
    DEBUG=<True_ou_False>
    
    # Configuração do Banco de Dados
    DATABASE_NAME=<nome_da_base_de_dados>
    DATABASE_USER=<Utilizador_da_bd>
    DATABASE_PASSWORD=<password_da_bd>
    DATABASE_HOST=<host_da_bd>
    DATABASE_PORT=<porta_da_bd>
    
    # Configuração do SMTP
    EMAIL_BACKEND=<backend_do_email>
    EMAIL_HOST=<host_do_email>
    EMAIL_PORT=<porta_do_email>
    EMAIL_USE_SSL=<True_ou_False>
    EMAIL_HOST_USER=<usuário_do_email>
    DEFAULT_FROM_EMAIL=<email_de_envio_padrao>
    EMAIL_HOST_PASSWORD=<senha_do_email>
    
    # Configuração do Token de Acesso do Instagram
    INSTA_ACCESS_TOKEN=<seu_token_de_acesso>

  Migrar para a base de dados:

    python manage.py migrate

  Correr a App:

    python manage.py runserver
  
