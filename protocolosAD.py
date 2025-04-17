ospf=110
eigrp=90
bgp=20

protocolo= input("Ingrese que protocolo desea saber: OSPF,EIGRP,BGP. ").upper();

if protocolo=="OSPF":print("La distancia administrativa de OSPF es: " ,ospf);
elif protocolo=="EIGRP":print("La distancia Administrativa de EIGRP es :", eigrp);
elif protocolo=="BGP":print("La distancia Administrativa de BGP es 20: ", bgp);
else: print("Protocolo no existente");

