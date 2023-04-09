import mysql.connector as mysql #biblioteca 
from core.configs import settings #settings seria as configurações do banco de dados que se localiza em "config.py"

connection = mysql.connect(
    host=settings.DB_HOST, 
    user=settings.DB_USER,
    password=settings.DB_PASS,
    database=settings.DB_NAME
)
