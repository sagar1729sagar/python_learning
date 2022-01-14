import requests
import json


def api_call():
    URL = "https://translate.google.com/translate_a/single?client=at&dt=t&dt=ld&dt=qca&dt=rm&dt=bd&dj=1&ie=UTF-8&oe=UTF-8&inputm=2&otf=2&iid=1dd3b944-fa62-4b55-b330-74909a99969e"
    # sl = de & tl = en & q = Hurra.
    data = {
        'sl': 'de',
        'tl': 'en',
        'q': 'Hurra.'
    }
    response = requests.post(URL, data=json.dumps(data))
    print(response)

api_call()
