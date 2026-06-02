def test_execute_payment_success(payments_api):

    create_response, payment_id = (
        payments_api.create_payment()
    )

    assert create_response.ok

    execute_response = (
        payments_api.execute_payment(payment_id)
    )

    assert execute_response.status == 200

    body = execute_response.json()

    assert body["paymentId"] == payment_id
    assert body["status"]["value"] in ["IN_PROGRESS", "COMPLETED"]
