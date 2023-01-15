from dotenv import load_dotenv
import os
load_dotenv()

DATABASE_URL = os.getenv('DATABASE_URL')

DEBUG=True

USERNAME='root'
PASSWORD='chaves123'
SERVER='localhost'
DB='contas_flutter'

# SQLALCHEMY_DATABASE_URI=f'mysql://{USERNAME}:{PASSWORD}@{SERVER}/{DB}'

SQLALCHEMY_DATABASE_URI='postgresql://postgres:0gPte5pMwDMFwbJmCzH5@containers-us-west-127.railway.app:6836/railway'

SQLALCHEMY_TRACK_MODIFICATIONS=True

SECRET_KEY='chave_secreta1'