from api.base_api import BaseApi


class BalanceApi(BaseApi):

    def get_balance(self):

        return self.request.get(f"{self.base_path}/balance")
