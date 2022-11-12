from bs4 import BeautifulSoup
import requests 
import os 

# DEL_START  ="<!--CTFLEARN-->"
# DEL_END    ="<!--/CTFLEARN-->"

# n = 0
# readmefile=open('README.md','r')
# lines = readmefile.readlines()
# readmefile.close()

# start =-1
# end = -1
# for line in lines:
#     if DEL_START in line:
#         start = n
#     if DEL_END in line:
#         end = n
#     n+=1
# if start == -1 or end == -1:
#     print("Error: Delimiter not found")
#     exit(1)

# partOne = lines[:start+1]
# conttemp = lines[start+1:end]
# partTwo = lines[end:]

url="https://ctflearn.com/user/Varius93"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Get the name of user
name = soup.find("h5", {"class": "text-left font-weight-bold font-primary my-auto d-inline"}).text.strip()

# Get the number of rank
rank = soup.find("span", {"class": "font-primary mt-2"}).text.strip()

rank = rank.split("nd")[0]

# Get the number of points
points = soup.find("div", {"class": "stats mt-3"}).text.strip()

points = points.split("points")[0]

data = ["```text\n"]

data.append("🧑‍💻 Name: "+name+"\n")
data.append("📈 Number Points: "+points+"\n")
data.append("🥇 Ranking: "+rank+"\n")
data.append("✅ Number of Challenges Finish: 125\n")
data.append("```\n")

print(data)

# if conttemp == data:
#     print("No change in README.md")
#     exit(0)

# result = partOne + data + partTwo
# readmefile=open('README.md','w')
# readmefile.writelines(result)
# readmefile.close()

# os.system('git config --local user.email "github-actions[bot]@users.noreply.github.com"')
# os.system('git config --local user.name "github-actions[bot]"')
# os.system('git add .')
# os.system('git commit -m "CTFLearn Stats Update"')
# os.system('git push')