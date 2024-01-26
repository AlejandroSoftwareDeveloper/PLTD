import uuid
import datetime

class Usuario:
    def __init__(
        self,
        fipru=None,
        fipag=None,
        diaspru=15,
        diaspag=60,
        terminopru=False,
        terminopag=False,
    ):
        self.uid = str(uuid.uuid1()).split("-")[-1]
        self.fipru = fipru
        self.fipag = fipag
        self.diaspru = diaspru
        self.diaspag = diaspag
        self.terminopru = terminopru
        self.terminopag = terminopag

    def get_user(self):
        return {
            "uid": self.uid,
            "initial_date_of_test": str(self.fipru)
            if self.fipru is not None
            else self.fipru,
            "initial_date_of_premiun": str(self.fipag)
            if self.fipag is not None
            else self.fipag,
            "days_of_test": self.diaspru,
            "days_of_use_as_premiun": self.diaspag,
            "has_temporal_licence_due": self.terminopru,
            "has_payment_license_due": self.terminopag,
        }

    def registrar_dias_de_prueba(self):
        return {
            "uid": self.uid,
            "initial_date_of_test": datetime.datetime.now(),
            "initial_date_of_premiun": str(self.fipag)
            if self.fipag is not None
            else self.fipag,
            "days_of_test": self.diaspru,
            "days_of_use_as_premiun": self.diaspag,
            "has_temporal_licence_due": self.terminopru,
            "has_payment_license_due": self.terminopag,
        }


def registrar_usuario():
    return Usuario()
 
async def tiempo_restante(data,string):
    year,month, days = data[string].split("-")
    test_time = datetime.datetime(int(year),int(month),int(days)) 
    today =  datetime.datetime.now()
    return [test_time,today]

async def user_has_tests_days(data:dict):
    test_time,today = await tiempo_restante(data,'start_date_for_test')
    return int((today - test_time).days) <= data['days_of_test'] and data['tests_days_selected'] 
    
async def user_has_premiun_days(data:dict):
    test_time,today = await tiempo_restante(data,'start_date_for_premiun_use')
    return int((today - test_time).days) <= data['days_of_use_as_premiun'] and data['premiun_days_selected']

async def dias_restantes(data,string):
    test_time,today = await tiempo_restante(data,string)
    return int((today - test_time).days)

    # print((today - test_time) >= data['days_of_test'] )
    # time_delta = datetime.timedelta(days=data['days_of_test'])
    # print(time_delta)
#  now = datetime.datetime.now()
    
#     #Dias para la fecha final
#     days = datetime.timedelta(days=15)
#     fecha_final = now + days
    
#     #Calculo para dias retantes
#     dias_restantes = int(str(fecha_final - now).split(" ")[0])
#     return (uid,now,True)