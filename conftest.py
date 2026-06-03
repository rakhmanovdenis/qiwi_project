import os

import pytest
from dotenv import load_dotenv
from playwright.sync_api import sync_playwright

from api.balance_api import BalanceApi
from api.payments_api import PaymentsApi


load_dotenv()


@pytest.fixture(scope="session")
def api_context():
    base_url = os.getenv(
        "BASE_URL",
        "https://api-test.qiwi.com/partner/payout"
    )
    token = os.getenv("TOKEN", "YOUR_TOKEN")

    with sync_playwright() as p:
        context = p.request.new_context(
            base_url=base_url,
            extra_http_headers={
                "Accept": "application/json",
                "Authorization": f"Bearer {token}",
            },
        )

        yield context

        context.dispose()


@pytest.fixture
def balance_api(api_context):
    return BalanceApi(api_context)


@pytest.fixture
def payments_api(api_context):
    return PaymentsApi(api_context)