import peewee as pw
import time

myDB = pw.MySQLDatabase("pupperdb", host="45.33.72.127", port=3306, user="todo", passwd="password")

class MySQLModel(pw.Model):
    """A base model that will use our MySQL database"""
    class Meta:
        database = myDB

class Pupper(MySQLModel):
    name = pw.CharField()
    bork = pw.CharField()
    tail_speed = pw.CharField()

# when you're ready to start querying, remember to connect
connected = False
tries = 0
while connected == False and tries < 5:
    try:
        myDB.connect()
        connected = True
    except pw.OperationalError as error:
        print("Could not connect to the db. Trying again in 10 seconds... {}".format(error))
        tries += 1
        time.sleep(10)

if not myDB.table_exists(Pupper):
    with myDB:
        print("Creating Pupper table")
        myDB.create_tables([Pupper])