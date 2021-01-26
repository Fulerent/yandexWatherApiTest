import pytest
import json
import cerberus

from data.general import MY_TOKEN as TOKEN,full_req, empty_req_no_lat, empty_req_no_lon, exceeds_par

#Приходит 200 код, вместо 403
def test_1_empty_req_no_lat(req_ya_api_weather):
    r = req_ya_api_weather.get(empty_req_no_lat, TOKEN)
    r_j = r.json()
    r_status = r.status_code
    assert r_status == 403

#Приходит 200 код, вместо 403
def test_2_empty_req_no_lon(req_ya_api_weather):
    r = req_ya_api_weather.get(empty_req_no_lon, TOKEN)
    r_status = r.status_code
    assert r_status == 403


def test_3_exceeds_par(req_ya_api_weather):
    r = req_ya_api_weather.get(exceeds_par, TOKEN)
    r_status = r.status_code
    assert r_status == 404


@pytest.mark.parametrize("test_input", [["lat", "11, 11"],
                                        ["lon", "153,000001"],
                                        ["lang", "123"],
                                        ["limit", "all"],
                                        ["hours", "24"],
                                        ["extra", "full"]])

def test_4_shema_error_invalid_date(req_ya_api_weather, test_input):
    req = full_req
    print(f"req === {req}")
    req[test_input[0]] = test_input[1]
    r = req_ya_api_weather.get(req, TOKEN)
    r_j = r.json()
    r_status = r.status_code
    print(r_status)
    print(r_j['error'])
