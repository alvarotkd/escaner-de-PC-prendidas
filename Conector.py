from re import I
import mysql.connector
cur=''
def conexion():
    conexion= mysql.connector.connect(host="127.0.0.1", username="root", password="Spiderred32", database="instituto")
    cur=conexion.cursor()
    return cur

def recorrido(cur):
    fila=''
    fila=cur.fetchall()
    for r in fila:
        print(fila[r])
        return r
    
def consulta (a):
    ip=''
    comp="SELECT Nombre FROM instituto.computadoras WHERE IP= %s;"
    cur.execute(comp,(a,))
    ip=recorrido()
    return ip