import re
from typing import Dict
from configparser import ConfigParser
from definitions import CONFIG_PATH


def snake(s: str):
    """
    Is it ironic that this function is written in camel case, yet it
    converts to snake case? hmm..
    """
    underscorer1 = re.compile(r'(.)([A-Z][a-z]+)')
    underscorer2 = re.compile('([a-z0-9])([A-Z])')

    subbed = underscorer1.sub(r'\1_\2', s)
    return underscorer2.sub(r'\1_\2', subbed).lower()


def camel(s: str):
    return s.title().replace('_', '')


def make_url(host, method: str, parameters: dict):
    url = host + method
    count = 0
    query_str = ''
    for key, value in parameters.items():
        if count == 0:
            query_str = '?{0}={1}'.format(key, value)
        else:
            query_str += '&{0}={1}'.format(key, value)
        count += 1

    return url + query_str


def get_query_str_dict(url: str) -> Dict[str, str]:
    parameters = url.split('?')[1]
    parameters = parameters.split('&')

    rs_dict = {}
    for param in parameters:
        [key, value] = param.split('=')
        rs_dict[key] = value

    return rs_dict


def config_ini(name: str) -> ConfigParser:
    config_parser = ConfigParser()
    config_parser.read(CONFIG_PATH + '/{filename}.ini'.format(filename=name))
    return config_parser
