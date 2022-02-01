import requests


def saves_and_retrieves_simple_data_t(app_url):
    calculate_input = {
        'user_id': 1,
        'data': {
            'x_data_type': 'sleep',
            'y_data_type': 'eat',
            'x': [
                {'date': '2022-02-01', 'value': 1.0},
            ],
            'y': [
                {'date': '2022-02-01', 'value': 1.0},
            ],
        },
    }
    correlation_input = {'x_data_type': 'sleep', 'y_data_type': 'eat'}
    correlation_output = {
        'user_id': 1,
        'x_data_type': 'sleep',
        'y_data_type': 'eat',
        'correlation': {
            'value': 1.0,
            'p_value': 1.0,
        },
    }
    r = requests.post(app_url + '/calculate', json=calculate_input)

    r = requests.get(app_url + '/correlation', params=correlation_input)

    assert r.status_code == 200
    assert r.json() == correlation_output
