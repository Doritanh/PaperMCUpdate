import requests
import json

version = "1.16"
name = "paper"

# r = requests.get("https://papermc.io/api/v2/projects")

r = requests.get("https://papermc.io/api/v2/projects/" + name + "/version_group/" + version + "/builds")
rJSON = r.json()

lastBuild = rJSON['builds'][-1]

buildVersion = str(lastBuild['version'])
buildNumber = str(lastBuild['build'])
buildDownload = str(lastBuild['downloads']['application']['name'])

downloadURL = "https://papermc.io/api/v2/projects/paper/versions/" + buildVersion + "/builds/" + buildNumber + "/downloads/" + buildDownload

r = requests.get(downloadURL)

with open(buildDownload, 'wb') as f:
    f.write(r.content)
