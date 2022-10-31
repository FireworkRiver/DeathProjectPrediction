import json
import csv
import os
from datetime import datetime, timedelta
today = datetime(2022,8,18)
oneyear = timedelta(days=365)

rep_list_address = "./rep_list.csv"
reader = csv.reader(open(rep_list_address))
rep_list = [row for row in reader]

dict_rep={}
dead_num = 0

for row in rep_list:
    repo = row[0]
    save_address = ".\\data\\commit\\%s.json" % (repo.replace("/", " "))
    if os.path.exists(save_address):
        with open(save_address, encoding="utf-8") as f:
            data = json.load(f)
        commit_time = data[0]["commit"]["author"]["date"]
        commit_date = datetime.strptime(commit_time, '%Y-%m-%dT%H:%M:%S%fZ')
        print(repo,"commit time:",commit_time)
        if commit_date<today-oneyear:
            flag = "dead"
            dead_num+=1
        else:
            flag = "alive"
        dict_rep[repo] = [commit_time,flag]
    else:
        print(repo,"Not exists")

print("dead repo:",dead_num)
with open('rep_commit.csv', 'w',newline='') as f:
    print("writing..")
    writer = csv.writer(f)
    for k, v in dict_rep.items():
        writer.writerow([k]+ v)