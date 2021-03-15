import requests
import json
import argparse

parser = argparse.ArgumentParser(description='Simple downloader script for PaperMC.')
parser.add_argument(
    "-p", "--project", help="Select the project to download latest (paper, waterfall).", default="paper")
parser.add_argument(
    "-v", "--version", help="Select the project version (1.16, 1.15...).", default="1.16")
args = parser.parse_args()

baseURL = "https://papermc.io/api/v2/projects/"

version = "1.16"
project = args.project

# r = requests.get("https://papermc.io/api/v2/projects")

r = requests.get(baseURL + project + "/version_group/" + version + "/builds")
rJSON = r.json()

lastBuild = rJSON['builds'][-1]

buildVersion = str(lastBuild['version'])
buildNumber = str(lastBuild['build'])
buildDownload = str(lastBuild['downloads']['application']['name'])

downloadURL = baseURL + project + "/versions/" + buildVersion + \
    "/builds/" + buildNumber + "/downloads/" + buildDownload

r = requests.get(downloadURL)

with open(buildDownload, 'wb') as f:
    f.write(r.content)
