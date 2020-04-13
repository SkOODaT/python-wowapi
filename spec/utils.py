import os

import requests


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def get_spec_resource(spec_file):
    base_url = "https://develop.battle.net/api/pages/content/documentation/world-of-warcraft/"
    url = f"{base_url}{spec_file}"

    response = requests.get(url)
    if response.ok:
        return response.text
    raise Exception('{0} returned wrong response: {1}'.format(url, response))


def save_spec_file(name, spec_file):
    print("saving spec for {0} to '{1}'".format(name, spec_file))
    data = get_spec_resource(spec_file)
    location = os.path.join(BASE_DIR, 'spec', spec_file)
    if not os.path.exists(os.path.dirname(location)):
        os.makedirs(os.path.dirname(location))
    with open(location, 'w') as f:
        f.write(data)


if __name__ == '__main__':
    save_spec_file('WoW Game Data API', 'game-data-apis.json')
