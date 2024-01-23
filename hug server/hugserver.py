import datetime
import hug
from db_management import Connection

def tiempo_de_prueba():
    today_time = datetime.datetime.now()
    next_15_days = datetime.timedelta(days=15)
    return [today_time, today_time + next_15_days]
    
#Esta es la funcion que le devuelve la response a la request de main app
@hug.get()
def validar(num: hug.types.text):
    connetion = Connection('register_user.sqlite')
    connetion.openconn()
    all = connetion.get_all_data("RegisterUser")
    if all == None:
        time = tiempo_de_prueba()
        connetion.insert([(num,time[0],time[1])])
    all = connetion.get_all_data("RegisterUser")
    connetion.close()
    return all

