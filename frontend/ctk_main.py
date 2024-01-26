import customtkinter
import datetime
from tkinter import *
from User import *
import time
import requests
import asyncio
from requests import *
from asyncio import *

data = {
    "is_user": False,
    "is_test_user": False,
    "user_is_register":False,
    "user_data": None,
    "dias_restantes_de_prueba":0,
    "dias_restantes_de_premiun":0,
    "first-time-message": "Bienvenido que desea hacer",
    "test-user-message": "Le restan 15 dias de uso.",
    "label-title": "System-Tk-Validator",
    "btn-test": "Probar aplicacion",
    "btn-buy": "Comprar aplicacion",
    "url":"http://localhost:8000/", # Cambiar la url local de las consultas, por la real de despliegue
}

usr = Usuario()
myuuid = usr.get_user()
miid = myuuid["uid"]
mydicttest = {"uid": miid,"start_date_for_test":datetime.datetime.now(),"tests_days_selected":True}
mydictpremiun = {"uid": miid,"start_date_for_premiun_use":datetime.datetime.now(),"premiun_days_selected":True }
mi_info = []

async def fetch_status(url:str)-> dict:
    response :Response = await asyncio.to_thread(requests.get,url,None)
    return {"status": response.status_code, "url":url,'response':response}


async def main():
    get_data: Task[dict] = asyncio.create_task(fetch_status("http://localhost:8000/userprofile/userprofile"))
    get_data: dict = await get_data
    if len(get_data['response'].json()) > 0:
        global mi_info,data
        mi_info.append(get_data['response'].json())
        mi_info = [elm for elm in mi_info[0] if elm['uid'] == str(miid)][0]
        data['is_test_user'] = await user_has_tests_days(mi_info)
        data['is_user'] = await user_has_premiun_days(mi_info)
        data['dias_restantes_de_prueba'] = await dias_restantes(mi_info,'start_date_for_test')
        data['dias_restantes_de_premiun'] = await dias_restantes(mi_info,'start_date_for_premiun_use')

asyncio.run(main=main())


def register_test_user():
    global mi_info
    if len(mi_info) == 0:
        newdata = requests.post(data["url"] + "userprofile/userprofile/",data=mydicttest)
        mi_info = newdata.json()
        label_time_to_complete.configure(text=data['test-user-message']) 
        btn_test.pack_forget()

def register_premiun_user():
    global mi_info
    if len(mi_info) == 0:
        newdata = requests.post(data["url"] + "userprofile/userprofile/",data=mydictpremiun)
        mi_info = newdata.json()
    else:
        newdata = requests.put(data["url"] + "userprofile/userprofile/" + str(mi_info['id']), data=mydictpremiun)
        mi_info = newdata.json()
    if btn_test:
        btn_test.pack_forget()
    label_time_to_complete.configure(text="Tiene 30 dias como usuario oficial.") 

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")
root = customtkinter.CTk()
root.geometry("500x350")

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = customtkinter.CTkLabel(
    master=frame, text=data["label-title"], font=("Roboto", 24)
)
label.pack(pady=20, padx=10)
label_time_to_complete = customtkinter.CTkLabel(
    master=frame, text=data["first-time-message"] 
    if not data['is_test_user'] or not data['is_user'] else 
    "Le restan {} dias de prueba".format(data['dias_restantes_de_prueba']) 
    if data['is_test_user'] and not data['is_user'] else 
    "Le restan {} dias de uso".format(data['dias_restantes_de_premiun']) if data['is_user'] else 
    "", font=("Roboto", 12)
)
label_time_to_complete.pack(pady=12, padx=10)
if not data["is_test_user"]:
    btn_test = customtkinter.CTkButton(
        master=frame, text=data["btn-test"], command=register_test_user
    )
    btn_test.pack(pady=12, padx=10)
button1 = customtkinter.CTkButton(
    master=frame, text=data["btn-buy"], 
    command=register_premiun_user
)

button1.pack(pady=12, padx=10)
label.pack(pady=12, padx=10)

root.mainloop()
