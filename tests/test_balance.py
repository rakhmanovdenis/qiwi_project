from decimal import Decimal


def test_balance_positive(balance_api):

    response = balance_api.get_balance()

    assert response.status == 200

    body = response.json()

    assert Decimal(body["balance"]["value"]) > 0
