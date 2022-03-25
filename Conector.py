from re import I
import mysql.connector
conexion= mysql.connector.connect(host="127.0.0.1", username="root", password="Spiderred32", database="instituto")
cur=conexion.cursor()


def recorrido():
    fila=''
    fila=cur.fetchall()
    for r in fila:
        print(fila[r])
        return r
    
def consulta (a):
    ip=''
    comp="SELECT Nombre FROM instituto.computadoras WHERE IP= %s;"
    cur.execute(comp,str(a),)
    ip=recorrido()
    return ip