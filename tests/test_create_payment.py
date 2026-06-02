def test_create_payment_success(payments_api):

    response, payment_id = payments_api.create_payment()

    assert response.status == 200

    body = response.json()

    assert body["paymentId"] == payment_id
    assert body["status"]["value"] == "READY"
