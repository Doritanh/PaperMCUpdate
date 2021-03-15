import requests
import json

version = "1.16"

r = requests.get("https://papermc.io/api/v2/projects/paper/version_group/" + version + "/builds")
rJSON = r.json()

json_formatted_str = json.dumps(rJSON, indent=4)
print(json_formatted_str)
