def test_create_payment_success(payments_api):
    response, payment_id = payments_api.create_payment()

    assert response.status == 200, response.text()

    payment = response.json()

    assert payment["paymentId"] == payment_id
    assert payment["status"]["value"] == "READY"
    assert payment["amount"]["value"] == "1.00"
    assert payment["amount"]["currency"] == "RUB"