from bs4 import BeautifulSoup
import requests 
import os 

DEL_START  ="<!--42CTF-->"
DEL_END    ="<!--/42CTF-->"

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

url="https://www.42ctf.org/en/scoreboard/?page=3"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Get the name of user
name = soup.find_all("a", {"class": "profile_link"})

name = name[3].text.strip()

# Get the number of rank
rank = soup.find_all("th", {"scope": "row"})

rank = rank[3].text.strip()

rank = rank.split(" ")[1]

# Get the number of points
points = soup.find_all("td")

points = points[11].text.strip()

points = points.split("<td>")[0]

data = ["```text\n"]

data.append("🧑‍💻 Name: "+name+"\n")
data.append("📈 Number Points: "+str(points)+"\n")
data.append("🥇 Ranking: "+rank+"\n")
data.append("✅ Number of Challenges Finish: 21\n")
data.append("```\n")

if conttemp == data:
    print("No change in README.md")
    exit(0)

result = partOne + data + partTwo

os.system('git pull')

readmefile=open('README.md','w')
readmefile.writelines(result)
readmefile.close()

os.system('git config --local user.email "github-actions[bot]@users.noreply.github.com"')
os.system('git config --local user.name "github-actions[bot]"')
os.system('git add .')
os.system('git commit -m "42CTF Stats Update"')
os.system('git push')