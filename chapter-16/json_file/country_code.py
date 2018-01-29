from pygal.maps.world import COUNTRIES


def get_country_code(country):
    for code,name in COUNTRIES.items():
        if country==name:
            return code
    return None
