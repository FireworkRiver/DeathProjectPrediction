import json

page_num = 110
root = ".\\data\\repositories\\"
dict_rep={}

for i in range(1,1+page_num):
    print("read page%d"%i)
    file = root +"page%d.json"%(i)
    with open(file, encoding="utf-8") as f:
        data = json.load(f)

    for rep in data["items"]:
        name = rep["full_name"]
        language = rep["language"]
        if language == None:
            continue
        stars = rep["stargazers_count"]
        dict_rep[name] = [stars, language]

import csv

labels = ["name","stars","language"]
with open('rep_list.csv', 'w',newline='') as f:
    print("writing..")
    writer = csv.writer(f)
    for k, v in dict_rep.items():
        writer.writerow([k]+ v)