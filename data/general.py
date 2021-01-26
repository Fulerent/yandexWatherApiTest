MY_TOKEN = {'X-Yandex-API-Key': '82eca524-de16-4fa3-9432-b8d986e2ba07'}

full_req = {'lat': '59.56',
            'lon': '30.95',
            'lang': 'ru_RU',
            'limit': '7',
            'hours': 'false',
            'extra': 'false',
            } # lat = долгота max = 180, lon = широта max = 90


def main_shema_json():
    shema = {
        "now": {"type": "number"},
        "now_dt": {"type": "string"},
        "info": {"type": "object"},
        "fact": {"type": "object"},
        "forecasts": {"type": "object"}
    }
    return shema


empty_req_no_lat = {
            'lon': '30.95',
            'lang': 'ru_RU',
            'limit': '7',
            'hours': 'false',
            'extra': 'false',
            }

empty_req_no_lon = {
            'lat': '59.56',
            'lang': 'ru_RU',
            'limit': '7',
            'hours': 'false',
            'extra': 'false',
            }

exceeds_par = {'lat': '200432423423.5345345320',
               'lon': '1105345345340.534534534556'}


