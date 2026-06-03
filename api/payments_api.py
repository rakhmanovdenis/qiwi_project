import uuid

from api.base_api import BaseApi


class PaymentsApi(BaseApi):

    def get_payments(self):
        return self.request.get(
            f"{self.base_path}/payments"
        )

    def create_payment(
        self,
        amount="1.00",
        currency="RUB",
        account="79123456789"
    ):
        payment_id = str(uuid.uuid4())

        response = self.request.put(
            f"{self.base_path}/payments/{payment_id}",
            json=self._payment_payload(
                amount,
                currency,
                account
            )
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

    @staticmethod
    def _payment_payload(amount, currency, account):
        return {
            "amount": {
                "value": amount,
                "currency": currency
            },
            "recipientDetails": {
                "providerCode": "qiwi-wallet",
                "fields": {
                    "account": account
                }
            }
        }