import re
import json
import requests.auth
import requests
import sys

class BearerAuth(requests.auth.AuthBase):
    def __init__(self, token):
        self.token = token
    def __call__(self, r):
        r.headers["authorization"] = "Bearer " + self.token
        return r

# fill in username and token to get 5000 instead of 60 requests per hour
if len(sys.argv) > 1:
    auth = BearerAuth(sys.argv[1])
else:
    username = ""
    github_token = ""
    auth = (username, github_token)

gitlab_session = requests.Session()
gitlab_session.auth = auth

libraries = open("libraries.csv", "rt", encoding="utf-8")
lines = libraries.readlines()
json_result_string ='''
{
  "organisations" : [
'''
for line in lines:
    json_result_string += "    {\n"
    parts = line.split(",")
    country = parts[0]
    city = parts[1]
    name = parts[2]
    link = parts[3]
    json_result_string += "      \"name\": \"" + name + "\",\n"
    json_result_string += "      \"country\": \"" + country + "\",\n"
    json_result_string += "      \"city\": \"" + city + "\",\n"
    json_result_string += "      \"url\": \"" + link.replace("\n","") + "\",\n"
    json_result_string += "      \"repositories\": "
    github_orga = re.findall("/([^/^$]+)$", link)[0].replace("\n","")
    print(country + "   " + city + "   " + github_orga)

    api_url = "https://api.github.com/orgs/" + github_orga + "/repos?per_page=100&page=1"

    res = gitlab_session.get(url=api_url)
    repo_data = res.json()
    while 'next' in res.links.keys():
        res=gitlab_session.get(res.links['next']['url'])
        repo_data.extend(res.json())

    json_result_string += json.dumps(repo_data, indent=4, ensure_ascii=0) + "\n"
    json_result_string += "    },\n"

json_result_string = json_result_string[:-2]
json_result_string += '''
  ]
}
'''

with open("all-libs.json", "w", encoding="utf-8") as json_file:
    json_file.write(json_result_string)
