import pytest
import cerberus

from data.general import MY_TOKEN as TOKEN,empty_req_no_lat, empty_req_no_lon, exceeds_par


def test_1_empty_req_no_lat(req_ya_api_weather):
    r = req_ya_api_weather.get(TOKEN, empty_req_no_lat)
    r_status = r.status_code
    assert r_status == 403


def test_2_empty_req_no_lon(req_ya_api_weather):
    r = req_ya_api_weather.get(TOKEN, empty_req_no_lon)
    r_status = r.status_code
    assert r_status == 403


def test_3_exceeds_par(req_ya_api_weather):
    r = req_ya_api_weather.get(TOKEN, exceeds_par)
    r_status = r.status_code
    assert r_status == 403
