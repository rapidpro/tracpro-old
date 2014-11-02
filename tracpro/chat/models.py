import requests
from django.conf import settings

def lookup_chat_messages(org):
    api_token = org.get_config('chat_api_token')

    try:
        url = '%s/api/v1/messages.json' % settings.API_ENDPOINT
        params = dict(flow=2046)
        params['direction'] = 'I'

        response = requests.get(url,
                                params=params,
                                headers={'Content-type': 'application/json',
                                         'Accept': 'application/json',
                                         'Authorization': 'Token %s' % api_token})

        result = response.json()
        return result['results']

    except Exception as e:
        raise e
