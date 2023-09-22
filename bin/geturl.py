import re


with open("repos.json") as file:
    text = file.read()
    urls = re.findall("https://github.com/[-\w.]+/[-\w.]+", text)

with open('repos.txt', 'w', encoding='utf-8') as f:
    for i in urls:
        f.write(i+"\n")
