import os

import pytest
from dotenv import load_dotenv
from playwright.sync_api import sync_playwright

from api.balance_api import BalanceApi
from api.payments_api import PaymentsApi

load_dotenv()


@pytest.fixture(scope="session")
def api_settings():
    settings = {
        "base_url": os.getenv("BASE_URL"),
        "token": os.getenv("TOKEN"),
        "agent_id": os.getenv("AGENT_ID"),
        "point_id": os.getenv("POINT_ID"),
    }
    if not all(settings.values()):
        pytest.skip("Set BASE_URL, TOKEN, AGENT_ID and POINT_ID in .env")
    return settings


@pytest.fixture(scope="session")
def api_context(api_settings):
    with sync_playwright() as p:
        context = p.request.new_context(
            base_url=api_settings["base_url"],
            extra_http_headers={
                "Accept": "application/json",
                "Authorization": f"Bearer {api_settings['token']}",
            },
        )

        yield context

        context.dispose()


@pytest.fixture
def balance_api(api_context, api_settings):
    return BalanceApi(
        api_context,
        api_settings["agent_id"],
        api_settings["point_id"],
    )


@pytest.fixture
def payments_api(api_context, api_settings):
    return PaymentsApi(
        api_context,
        api_settings["agent_id"],
        api_settings["point_id"],
    )
