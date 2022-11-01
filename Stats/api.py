import os
import requests

DEL_START  ="<!--ROOTME-->"
DEL_END    ="<!--/ROOTME-->"

n = 0
readmefile=open('README.md','r')
lines = readmefile.readlines()
readmefile.close()

start =-1
end = -1
for line in lines:
    if DEL_START in line:
        start = n
    if DEL_END in line:
        end = n
    n+=1
if start == -1 or end == -1:
    print("Error: Delimiter not found")
    exit(1)

partOne = lines[:start+1]
conttemp = lines[start+1:end]
partTwo = lines[end:]

# Get the API_KEY
API_KEY = os.environ.get('API_KEY')

# Set cookies
cookies = {"api_key": API_KEY}

# Get the API
resp = requests.get("https://api.www.root-me.org/auteurs/719910", cookies=cookies)

# Check if the status code is 200
if resp.status_code != 200:
    raise Exception("GET /auteurs/ {}".format(resp.status_code))

# Get the data
data = resp.json()

info = ["```text\n","\n"]

info.append("🧑‍💻 Name:\n")
info.append(data["nom"])
info.append("\n")

info.append("📈 Number Points:\n")
info.append(data["score"])
info.append("\n")

info.append("🥇 Ranking:\n")
info.append(str(data["position"]))
info.append("\n")

info.append("✅ Number of Challenges Finish:\n")
info.append(str(len(data["validations"])))

info.append("```\n")

if conttemp == info:
    print("No change in README.md")
    exit(0)

result = partOne + info + partTwo
readmefile=open('README.md','w')
readmefile.writelines(result)
readmefile.close()

os.system('git config --local user.email "github-actions[bot]@users.noreply.github.com"')
os.system('git config --local user.name "github-actions[bot]"')
os.system('git add .')
os.system('git commit -m "RootMe Stats Update"')
os.system('git push')