import datetime
import hug

def tiempo_de_prueba():
    today_time = datetime.datetime.now()
    next_15_days = datetime.timedelta(days=15)
    return [today_time, today_time + next_15_days]
    
def tiempo_de_pruebas_vencio(lista):
    fechaI = [int(elm1) for elm1 in lista[1].split('T')[0].split("-")]
    fechaF = [int(elm2) for elm2 in lista[2].split('T')[0].split("-")]
    d0 = datetime.datetime(fechaI[0],fechaI[1],fechaI[2])
    d1 = datetime.datetime(fechaF[0],fechaF[1],fechaF[2])
    return (d1 - d0).days <= 0
    
    
lista = [['705a0f2d130d', '2024-01-24T00:42:18.636082', '2024-02-08T00:42:18.636082']]

@hug.get()
def validar(uuid: hug.types.text):
    for elm in lista:
        if elm[0] == uuid:
            return tiempo_de_pruebas_vencio(elm)
    today,xdaylater = tiempo_de_prueba()
    lista.append((uuid,today,xdaylater))
    return lista

