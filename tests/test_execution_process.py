from flask import Flask
from ..execution_process import routes


def test_post_webhook_payload_1_must_returns_200():
    app = Flask(__name__)
    routes(app)
    client = app.test_client()

    data = {
        "evt": "ExecutionFinishedWithError",
        "execution": "20201015.111226-ij0uxv",
        "owner": 56,
        "bot": "pje-trt-copia-integral"
    }
    url = '/notification'

    response = client.post(url, json=data)

    assert response.status_code == 200


def test_post_webhook_payload_2_must_returns_200():
    app = Flask(__name__)
    routes(app)
    client = app.test_client()

    data = {
        "evt": "ReportGenerated",
        "execution": "20201015.111226-ij0uxv",
        "owner": 56,
        "bot": "pje-trt-copia-integral"
    }
    url = '/notification'

    response = client.post(url, json=data)

    assert response.status_code == 200


def test_post_webhook_payload_1_must_returns_400():
    app = Flask(__name__)
    routes(app)
    client = app.test_client()

    data = {
        "execution": "20201015.111226-ij0uxv",
        "owner": 56,
        "bot": "pje-trt-copia-integral"
    }
    url = '/notification'

    response = client.post(url, json=data)

    assert response.status_code == 400


def test_post_webhook_payload_2_must_returns_400():
    app = Flask(__name__)
    routes(app)
    client = app.test_client()

    data = {
        "execution": "20201015.111226-ij0uxv",
        "owner": 56,
        "bot": "pje-trt-copia-integral"
    }
    url = '/notification'

    response = client.post(url, json=data)

    assert response.status_code == 400
