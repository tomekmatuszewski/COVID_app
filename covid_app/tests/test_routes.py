import pytest

from covid_app.routes import app


@pytest.fixture(name="client")
def create_client():
    with app.test_client() as client:
        yield client


def test_get_all_countries_summary(client):
    response = client.get("/covid/summary")
    assert response.status_code == 200


@pytest.mark.parametrize(
    "country, exp_result",
    (
        ("italy", 200),
        ("grenada", 200),
        ("poland", 200),
        ("%%%%", 500),
    ),
)
def test_country_day_one_cases(client, country, exp_result):
    response = client.get(f"/covid/{country}")
    assert response.status_code == exp_result


@pytest.mark.parametrize(
    "country,start_date,end_date,exp_result",
    (
        ("spain", "2020-09-09", "2020-10-11", 200),
        ("poland", "2020-03-09", "2020-10-11", 200),
        ("%%%%", "2020-10-09", "2020-10-11", 500),
        ("canada", "2020-10-09", "ppp", 500),
    ),
)
def test_country_start_end_date_cases(
    client, country, start_date, end_date, exp_result
):
    response = client.get(f"/covid/{country}/{start_date}/{end_date}")
    assert response.status_code == exp_result
