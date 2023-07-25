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

    SECRET_KEY=<your_secret_key>
    DEBUG=<True_or_False>
    
    # Database Configuration
    DATABASE_NAME=<database_name>
    DATABASE_USER=<database_user>
    DATABASE_PASSWORD=<database_password>
    DATABASE_HOST=<database_host>
    DATABASE_PORT=<database_port>
    
    # SMTP Configuration
    EMAIL_BACKEND=<email_backend>
    EMAIL_HOST=<email_host>
    EMAIL_PORT=<email_port>
    EMAIL_USE_SSL=<True_or_False>
    EMAIL_HOST_USER=<email_user>
    DEFAULT_FROM_EMAIL=<default_sender_email>
    EMAIL_HOST_PASSWORD=<email_password>
    
    # Instagram Access Token Configuration
    INSTA_ACCESS_TOKEN=<your_instagram_access_token>

  Migrate to the database:

    python manage.py migrate

  Run the App:

    python manage.py runserver

# First Steps
  Step1 : Create a superuser
  
    python manage.py createsuperuser

  Step2: Create first user
  
   Login in with the superuser clicking in "ccColinaDoSol" on the footer of the page and create your first administrator.
  
