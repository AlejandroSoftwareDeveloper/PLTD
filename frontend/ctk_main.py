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
    "user_is_register": False,
    "user_data": None,
    "dias_restantes_de_prueba": 0,
    "dias_restantes_de_premiun": 0,
    "first-time-message": "Bienvenido que desea hacer",
    "test-user-message": "Se ha registrado para 15 dias de uso en la version de prueba.",
    "premiun-user-message": "Se ha registrado para 60 dias de uso en la version premiun de la aplicacion.",
    "label-title": "System-Tk-Validator",
    "btn-test": "Probar aplicacion",
    "btn-buy": "Comprar aplicacion",
    "url": "http://localhost:8000/",  # Cambiar la url local de las consultas, por la real de despliegue
}

usr = Usuario()
user = usr.get_user()
miid = user["uid"]
conexion = False
all_data = None


async def fetch_status(url: str) -> dict:
    # Anterior parametro de retorno
    # return {"status": response.status_code, "url":url, 'response': response}
    response: Response = await asyncio.to_thread(requests.get, url, None)
    return response


async def main():
    try:
        global all_data, conexion, initial_response
        server_data: Task[dict] = asyncio.create_task(
            fetch_status("http://localhost:8000/userprofile/userprofile")
        )
        server_data: dict = await server_data
        conexion = True
        all_data = server_data
    except:
        print("No se pudo realizar la conexion.")


asyncio.run(main=main())
usr.get_my_user_from_data(all_data.json())


def register_test_user():
    if not usr.has_any_licence():
        user = usr.get_user()
        user["start_date_for_test"] = datetime.datetime.now()
        user["tests_days_selected"] = True
        newdata = requests.post(data["url"] + "userprofile/userprofile/", data=user)
        usr.actualizar_datos_de_usuario(newdata.json())
        label_time_to_complete.configure(text=data["test-user-message"])


def register_premiun_user():
    user = usr.get_user()
    current_date = datetime.datetime.now()
    if not usr.has_any_licence():
        user["test_days_selected"] = True
        user["start_date_for_premiun_use"] = current_date
        user["premiun_days_selected"] = True
        newdata = requests.post(data["url"] + "userprofile/userprofile/", data=user)
        usr.actualizar_datos_de_usuario(newdata.json())
    else:
        user["test_days_selected"] = True
        user["start_date_for_premiun_use"] = current_date
        user["premiun_days_selected"] = True
        newdata = requests.put(
            data["url"] + "userprofile/userprofile/" + str(user["id"]), data=user
        )
        usr.actualizar_datos_de_usuario(newdata.json())
    if user["premiun_days_selected"]:
        label_time_to_complete.configure(text=data["premiun-user-message"])


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

if not conexion:  # Comprueba que hay conexion
    label = customtkinter.CTkLabel(
        master=frame,
        text="No es posible conectarse al servicio.\n revise su conexion a internet o contacte con el \n administrador del servicio.",
        font=("Roboto", 12),
    )
    label.pack(pady=30, padx=10)

elif usr.user_has_tests_days() and not usr.user_has_premiun_days():
    label_time_to_complete = customtkinter.CTkLabel(
        master=frame,
        text="Usted le restan {} días de uso del sistema \n en su versión de prueba.".format(
            usr.cuantos_dias_le_quedan()
        ),
        font=("Roboto", 12),
    )
    label_time_to_complete.pack(pady=12, padx=10)
    button1 = customtkinter.CTkButton(
        master=frame, text="Comprar aplicacion", command=register_premiun_user
    )
    button1.pack(pady=12, padx=10)
    label.pack(pady=12, padx=10)

elif usr.user_has_premiun_days():
    label_time_to_complete = customtkinter.CTkLabel(
        master=frame,
        text="Usted le restan {} días de uso del sistema \n en su versión premiun.".format(
            usr.cuantos_dias_le_quedan("premiun")
        ),
        font=("Roboto", 12),
    )
    label_time_to_complete.pack(pady=12, padx=10)
    button1 = customtkinter.CTkButton(
        master=frame, text="Comprar aplicacion", command=register_premiun_user
    )
    button1.pack(pady=12, padx=10)

# Todas las variantes antes de elif se escriben antes del siguiente el else
else:
    label_time_to_complete = customtkinter.CTkLabel(
        master=frame, text=data["first-time-message"], font=("Roboto", 12)
    )
    label_time_to_complete.pack(pady=12, padx=10)
    btn_test = customtkinter.CTkButton(
        master=frame, text="Probar aplicacion", command=register_test_user
    )
    btn_test.pack(pady=12, padx=10)
    button1 = customtkinter.CTkButton(
        master=frame, text="Comprar aplicacion", command=register_premiun_user
    )
    button1.pack(pady=12, padx=10)

root.mainloop()
