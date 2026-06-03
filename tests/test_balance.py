from decimal import Decimal


def test_get_balance_success(balance_api):
    response = balance_api.get_balance()

    assert response.status == 200, response.text()

    balance_info = response.json()

    assert "balance" in balance_info
    assert "available" in balance_info

    balance = balance_info["balance"]
    available = balance_info["available"]

    assert balance["currency"] == "RUB"
    assert available["currency"] == "RUB"

    assert Decimal(balance["value"]) > Decimal("0")
    assert Decimal(available["value"]) > Decimal("0")