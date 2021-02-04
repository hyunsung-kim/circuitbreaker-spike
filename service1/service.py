import requests

from circuitbreaker import db_breaker


@db_breaker
def external_error_api():
    res = requests.get('http://localhost:8001/error')
    print(f'[external_error_api] status:{res.status_code}')
    if res.status_code != r'2d{2}':
        raise Exception('Error api call')


@db_breaker
def external_success_api():
    res = requests.get('http://localhost:8001/success')
    print(f'[external_success_api] status:{res.status_code}')
