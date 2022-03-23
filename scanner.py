from ast import If
from pydoc import cli
from tabnanny import verbose
import scapy.all as scapy
import bottele
import Conector





    
target_ip = '192.168.12.0/24'

arp = scapy.ARP(pdst = target_ip)

ether = scapy.Ether(dst = "ff:ff:ff:ff:ff:ff" )

paquete = ether/arp

respuesta = scapy.srp(paquete, timeout = 2, verbose=0) [0]

clientes= []

for enviado,recivido in respuesta:
    clientes+= [[recivido.psrc,recivido.hwsrc]]

totalIp=len(clientes)
b=0
a=''
prendidas = []
comp=""
ip=''
for i in range (totalIp):
    Conector.conexion()
    a=clientes[i][0]
    Conector.consulta(a)
    if ip != None:
      bottele.telegram_bot_sendtext("pc prendida:"+ str(ip)) 
      b=1   
        

if b==0:
  bottele.telegram_bot_sendtext("INSTITUTO APAGADO")



    # if clientes[i][1] == 'd0:67:e5:e7:1b:8d':
    #     prendidas+= [clientes[i][0]]
    #     b=1
    #print("IP: {} MAC: {}". format(clientes[i][0], clientes[i][1]))
    

# totalCon=len(prendidas)
# if b==1:
#     for j in range (totalCon): 
#         bottele.telegram_bot_sendtext("pc prendida " + prendidas[j] )
# else:
#     bottele.telegram_bot_sendtext("tamy no conectada")
    


