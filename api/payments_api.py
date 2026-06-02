import uuid

from api.base_api import BaseApi


class PaymentsApi(BaseApi):

    def create_payment(
            self,
            amount="200.00",
            currency="RUB",
            account="79123456789"
    ):

        payment_id = str(uuid.uuid4())

        payload = {
            "amount": {
                "value": amount,
                "currency": currency
            },
            "recipientDetails": {
                "providerCode": "qiwi-wallet",
                "fields": {
                    "account": account
                }
            },
            "customer": {
                "account": "#12345",
                "email": "usermail@mail.mail",
                "phone": account
            },
            "source": {
                "paymentType": "NO_EXTRA_CHARGE",
                "paymentToolType": "BANK_ACCOUNT",
                "paymentTerminalType": "INTERNET_BANKING"
            }
        }

        response = self.request.put(
            f"{self.base_path}/payments/{payment_id}",
            data=payload,
            headers={
                "Content-Type": "application/json"
            }
        )

        return response, payment_id

    def execute_payment(self, payment_id):

        return self.request.post(
            f"{self.base_path}/payments/{payment_id}/execute"
        )

    def get_payment(self, payment_id):

        return self.request.get(
            f"{self.base_path}/payments/{payment_id}"
        )
