from dotenv import load_dotenv
from peewee import *

import os

load_dotenv()

database = MySQLDatabase(
    os.getenv("MYSQL_DATABASE"),
    user=os.getenv("MYSQL_USER"),
    passwd=os.getenv("MYSQL_PASSWORD"),
    host=os.getenv("MYSQL_HOST"),
    port=int(os.getenv("MYSQL_PORT")),
)


class UserModel(Model):
    id = AutoField(primary_key=True)
    username = CharField(max_length=50)
    email = CharField(max_length=50)
    password = CharField(max_length=50)

    class Meta:
        database = database
        table_name = "users"

class CLienteModel(Model):
    id = AutoField(primary_key=True)
    name = CharField(max_length=50)
    address = CharField(max_length=50)
    phone = CharField(max_length=50)

    class Meta:
        database = database
        table_name = "clientes"

class FacturaModel(Model):
    id = AutoField(primary_key=True) 
    date = CharField(max_length=50)  
    client_id = IntegerField()   
    total = FloatField()        

    class Meta:
        database = database  
        table_name = "facturas"  

class ProductoModel(Model):
    id = AutoField(primary_key=True) 
    name = CharField(max_length=100)  
    price = FloatField()     
    stock = IntegerField()         

    class Meta:
        database = database         
        table_name = "productos"


class TransaccionModel(Model):
    id = AutoField(primary_key=True)  
    client_id = IntegerField()         
    product_id = IntegerField()         
    quantity = IntegerField()        
    total = FloatField()            

    class Meta:
        database = database        
        table_name = "transacciones" 

class VeterinarioModel(Model):
    id = AutoField(primary_key=True)     
    name = CharField(max_length=100)       
    specialty = CharField(max_length=100)  
    years_experience = IntegerField()     

    class Meta:
        database = database               
        table_name = "veterinarios"