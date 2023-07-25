# WebApp-CC-ColinaSol


![Logomarca CC COLINA SOL - Versão Horizontal Cores RGB 300dpi](https://user-images.githubusercontent.com/79157730/215213134-4db3f2bf-01e7-4772-abde-70f05f2c2bb8.png)

Development of the website and management platform for the Colina do Sol shopping center.

# Prerequisites:
  * Python 3.10 or higher
  * MySQL DB
# Installation:

  In the project's root directory, install a virtual environment:

    pip install pipenv

  Activate the virtual environment:

    pipenv shell

  Install the application's dependencies:

    pip install -r requirements.txt

  Add the .env file to the project's root directory:

    SECRET_KEY=<sua_chave_secreta>
    DEBUG=<True_ou_False>
    
    # Database Configuration
    DATABASE_NAME=<nome_da_base_de_dados>
    DATABASE_USER=<Utilizador_da_bd>
    DATABASE_PASSWORD=<password_da_bd>
    DATABASE_HOST=<host_da_bd>
    DATABASE_PORT=<porta_da_bd>
    
    # SMTP Configuration
    EMAIL_BACKEND=<backend_do_email>
    EMAIL_HOST=<host_do_email>
    EMAIL_PORT=<porta_do_email>
    EMAIL_USE_SSL=<True_ou_False>
    EMAIL_HOST_USER=<usuário_do_email>
    DEFAULT_FROM_EMAIL=<email_de_envio_padrao>
    EMAIL_HOST_PASSWORD=<senha_do_email>
    
    # Instagram Access Token Configuration
    INSTA_ACCESS_TOKEN=<seu_token_de_acesso>

  Migrate to the database:

    python manage.py migrate

  Run the App:

    python manage.py runserver
  
