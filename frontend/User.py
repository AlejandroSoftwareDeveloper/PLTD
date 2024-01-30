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
        self.id = 0
        self.uid = str(uuid.uuid1()).split("-")[-1]
        self.start_date_for_test = fipru  # ya
        self.start_date_for_premiun_use = fipag  # ya
        self.days_of_test = diaspru
        self.days_of_use_as_premiun = diaspag
        self.tests_days_selected = terminopru
        self.premiun_days_selected = terminopag
        self.all_responses = None

    def get_my_user_from_data(self, response_json):
        self.all_responses = response_json
        if len(self.all_responses) != 0:
            user = self.exist_mi_user(self.all_responses)
            if user[0]:
                self.update_user_data(self.all_responses[user[1]])

    def get_user(self):
        return {
            "id": self.id,
            "uid": self.uid,
            "start_date_for_test": self.start_date_for_test,
            "start_date_for_premiun_use": self.start_date_for_premiun_use,
            "days_of_test": self.days_of_test,
            "days_of_use_as_premiun": self.days_of_use_as_premiun,
            "test_days_selected": self.tests_days_selected,
            "premiun_days_selected": self.premiun_days_selected,
        }

    def update_user_data(self, data):
        self.id = data["id"]
        self.uid = data["uid"]
        self.days_of_test = data["days_of_test"]
        self.days_of_use_as_premiun = data["days_of_use_as_premiun"]
        self.start_date_for_test = data["start_date_for_test"]
        self.start_date_for_premiun_use = data["start_date_for_premiun_use"]
        self.tests_days_selected = data["tests_days_selected"]
        self.premiun_days_selected = data["premiun_days_selected"]

    def has_any_licence(self):
        return self.tests_days_selected or self.premiun_days_selected

    def tiempo_restante(self, cond="test") -> int:
        year, month, days = (
            self.start_date_for_premiun_use
            if cond == "premiun"
            else self.start_date_for_test
        ).split("-")
        test_time = datetime.datetime(int(year), int(month), int(days))
        today = datetime.datetime.now()
        return int((today - test_time).days)

    def exist_mi_user(self, data):
        for pos, elm in enumerate(data):
            if elm["uid"] == str(self.uid):
                return [True, pos]
        return [False, -1]

    def cuantos_dias_le_quedan(self, cond="test"):
        if self.start_date_for_premiun_use == None or self.start_date_for_test == None:
            return 0
        dias = self.days_of_test if cond == "test" else self.days_of_use_as_premiun
        return dias - self.tiempo_restante(cond)

    def actualizar_datos_de_usuario(self, response_json):
        all_responses = [response_json]
        if len(all_responses) != 0:
            data = self.exist_mi_user(all_responses)
            if data[0]:
                self.update_user_data(all_responses[data[1]])

    def user_has_tests_days(self) -> bool:
        if self.start_date_for_test == None:
            return False
        return self.tiempo_restante() <= self.days_of_test and self.tests_days_selected

    def user_has_premiun_days(self) -> bool:
        if self.start_date_for_premiun_use == None:
            return False
        return (
            self.tiempo_restante("premiun") <= self.days_of_use_as_premiun
            and self.premiun_days_selected
        )
