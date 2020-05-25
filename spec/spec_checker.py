import json
from pathlib import Path

import requests
from dictdiffer import diff


def check_spec(id, spec_file):
    print(f"Detecting changes in the {id}")
    base_url = "https://develop.battle.net/api/pages/content/documentation/world-of-warcraft/"
    spec_url = f"{base_url}{spec_file}"

    response = requests.get(spec_url)
    new_content = response.json()
    if Path(spec_file).is_file():
        with open(spec_file, 'r') as old_content_file:
            old_content = json.load(old_content_file)
            differences = list(diff(old_content, new_content))
            if len(differences) > 0:
                print(f"Changes in the {id} have been detected since last release!")
                print("I need a human to look for possible deprecations.")
                print("-----------------------------------------------------")
                for difference in differences:
                    print(difference)
                print("-----------------------------------------------------")
                return True
    else:
        with open(spec_file, 'w') as content_file:
            content_file.write(json.dumps(new_content, indent=2))

    print("No API changes detected..")
    return False

if __name__ == '__main__':
    assert not check_spec('WoW Game Data API', 'game-data-apis.json')
    assert not check_spec('WoW Game Data API', 'profile-apis.json')
