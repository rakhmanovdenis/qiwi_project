def test_execute_payment_success(payments_api):
    create_response, payment_id = payments_api.create_payment()

    assert create_response.status == 200, create_response.text()

    created_payment = create_response.json()
    assert created_payment["status"]["value"] == "READY"

    execute_response = payments_api.execute_payment(payment_id)

    assert execute_response.status == 200, execute_response.text()

    payment = execute_response.json()
    assert payment["paymentId"] == payment_id
    assert payment["status"]["value"] in {"IN_PROGRESS", "COMPLETED"}