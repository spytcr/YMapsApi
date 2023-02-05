import requests


def geocode(code):
    params = {
        'apikey': '40d1649f-0493-4b70-98ba-98533de7710b',
        'geocode': code,
        'results': 1,
        'lang': 'ru_RU',
        'format': 'json'
    }
    response = requests.get('http://geocode-maps.yandex.ru/1.x/', params)
    if response:
        json = response.json()
        feature = json["response"]["GeoObjectCollection"]["featureMember"]
        if feature:
            return feature[0]["GeoObject"]


def get_address(point):
    if point is not None:
        code = geocode(f'{point[0]},{point[1]}')
        if code is not None:
            meta = code['metaDataProperty']['GeocoderMetaData']['Address']
            return meta['formatted'], meta['postal_code'] if 'postal_code' in meta else ''


def get_point(address):
    code = geocode(address)
    if code is not None:
        pos = code['Point']['pos'].split()
        return float(pos[0]), float(pos[1])


def get_organization(point):
    params = {
        'apikey': 'dda3ddba-c9ea-4ead-9010-f43fbc15c6e3',
        'text': 'Организация',
        'll': f'{point[0]},{point[1]}',
        'spn': '0.005,0.005',
        'type': 'biz',
        'results': 1,
        'lang': 'ru_RU',
        'format': 'json'
    }
    response = requests.get('https://search-maps.yandex.ru/v1/', params)
    if response is not None:
        json = response.json()
        if 'features' in json and json['features']:
            organization = json['features'][0]
            return (tuple(organization['geometry']['coordinates']),
                    (organization['properties']['CompanyMetaData']['name'], ''))


def get_map(mode, coord, zoom, point):
    params = {
        'l': mode,
        'll': f'{coord[0]},{coord[1]}',
        'z': zoom,
        'size': '650,450',
        'lang': 'ru_RU'
    }

    if point is not None:
        params['pt'] = f'{point[0]},{point[1]},flag'
    response = requests.get('http://static-maps.yandex.ru/1.x/', params)
    return response.content
