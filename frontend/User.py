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
            "total_days_of_test": self.diaspru,
            "total_days_of_payment": self.diaspag,
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
            "total_days_of_test": self.diaspru,
            "total_days_of_payment": self.diaspag,
            "has_temporal_licence_due": self.terminopru,
            "has_payment_license_due": self.terminopag,
        }


def registrar_usuario():
    return Usuario()
