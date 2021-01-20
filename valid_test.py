import pytest
import cerberus
from data.general import MY_TOKEN as TOKEN, full_req, main_shema_json


@pytest.mark.parametrize("test_input", ["lat': '40,5', 'lon': '64,5}",
                                        "lat': '39,891', 'lon': '51,6}",
                                        "lat': '56.237654', 'lon': '58.004785}",
                                        "lat': '37,61', 'lon': '55,755}"
                                        ])
def test_1_status_empty_req(req_ya_api_weather, test_input):
    r = req_ya_api_weather.get(test_input, TOKEN)
    r_status = r.status_code
    assert r_status == 200


def test_2_full_req(req_ya_api_weather):
    r = req_ya_api_weather.get(full_req, TOKEN)
    r_status = r.status_code
    assert r_status == 200


def test_3_location(req_ya_api_weather):
    r = req_ya_api_weather.get(full_req, TOKEN)
    geo = r.json()
    assert geo["geo_object"]['locality']['name'] == 'Тосненский район'


@pytest.mark.parametrize("test_input, expected_result",
                         [('ru_Ru', 'Тосненский район' ), ('ru_UA', 'Тосненский район'), ('uk_UA', 'Тосненский район'),
                          ('be_BY', 'Тосненский район'), ('kk_KZ', 'Тосненский район'), ('tr_TR', 'Tosnenskiy rayon'),
                          ('en_US', 'Tosnenskiy District')])
def test_4_test_lang(req_ya_api_weather, test_input, expected_result):
    full_req['lang'] = test_input
    r = req_ya_api_weather.get(full_req, TOKEN)
    geo_lang = r.json()
    assert geo_lang["geo_object"]['locality']['name'] == expected_result


@pytest.mark.parametrize("count_day", range(1, 8))
def test_5_count_day(req_ya_api_weather, count_day):
    full_req['limit'] = count_day
    r = req_ya_api_weather.get(full_req, TOKEN)
    count_date = str(r.json())
    assert count_date.count('date_ts') == count_day


@pytest.mark.parametrize("input_count_day", range(1, 8))
def test_6_count_block_hours(req_ya_api_weather, input_count_day):
    count_block_hours = input_count_day
    full_req['limit'] = input_count_day
    r = req_ya_api_weather.get(full_req, TOKEN)
    count_date = str(r.json())
    assert count_date.count('hours') == count_block_hours and count_date.count('hours') != []


# def test_7_valid_main_shema(req_ya_api_weather):
#     r = req_ya_api_weather.get(full_req, TOKEN)
#     response = r.json()
#     v = cerberus.Validator()
#     assert v.validate(response, main_shema_json())

#TODO: добавить тесты на 204 ошибку(значение не найдено)





