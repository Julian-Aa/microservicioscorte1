from dotenv import load_dotenv
from peewee import *

import os

load_dotenv()

database = MySQLDatabase(
    os.getenv("MYSQL_DATABASE"),
    user=os.getenv("MYSQL_USER"),
    password=os.getenv("MYSQL_PASSWORD"),
    host=os.getenv("MYSQL_HOST"),
    port=int(os.getenv("MYSQL_PORT")),
)

class FrutaModel(Model):
    id = AutoField(primary_key=True)
    nombre = CharField(max_length=50)
    color = CharField(max_length=50)
    peso = FloatField()
    origen = CharField(max_length=50)
    precio = FloatField()

    class Meta:
        database = database  
        table_name = "frutas"

try:
    database.connect()
    print("Conexión a la base de datos exitosa.")
except Exception as e:
    print(f"Error conectando a la base de datos: {e}")
finally:
    database.close()
