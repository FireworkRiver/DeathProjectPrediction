import json
import csv
import os
from datetime import datetime, timedelta
from tqdm import tqdm

rep_list_address = "./rep_commit.csv"
reader = csv.reader(open(rep_list_address))
rep_list = [row for row in reader]

root = 'E:/Death project/data/issues'
checked = True
if checked:
    for row in tqdm(rep_list):
        repo = row[0]
        repo_dir = root + "/" + repo.replace("/", " ")
        fo = open(repo_dir + "/pageNum.txt", "r")
        last_page_num = int(fo.read())
        for i in range(1, last_page_num + 1):
            if os.path.exists(repo_dir + "/page%d.json" % (i)):
                continue
            else:
                print(repo, "is not completed.")
                break
    print("check finish.")

repo_issue = []
for row in rep_list:
    repo = row[0]
    print("read",repo,"%d/%d"%(rep_list.index(row)+1,len(rep_list)))
    last_commit_time = row[1]
    last_commit_date = datetime.strptime(last_commit_time, '%Y-%m-%dT%H:%M:%SZ')
    repo_dir = root + "/" + repo.replace("/", " ")
    fo = open(repo_dir + "/pageNum.txt", "r")
    last_page_num = int(fo.read())
    issues_list = [[0 for j in range(4)] for i in range(25)]
    for i in range(1, last_page_num + 1):
        with open(repo_dir + "/page%d.json" % (i), encoding="utf-8") as f:
            data = json.load(f)
        for issue in data:
            try:
                pull_request = issue['pull_request']
            except:
                pull_request = None
            createtime = issue['created_at']
            createdate = datetime.strptime(createtime, '%Y-%m-%dT%H:%M:%SZ')
            time = last_commit_date - createdate
            if time.days>=0:
                months = int(time.days/30)
                if months<24:
                    if pull_request == None:
                        issues_list[months][0] += 1
                        issues_list[24][0] += 1
                    else:
                        issues_list[months][2] += 1
                        issues_list[24][2] += 1
            closetime = issue['closed_at']
            if not closetime == None:
                closedate = datetime.strptime(closetime, '%Y-%m-%dT%H:%M:%SZ')
                time = last_commit_date - closedate
                if time.days >= 0:
                    months = int(time.days / 30)
                    if months < 24:
                        if pull_request == None:
                            issues_list[months][1] += 1
                            issues_list[24][1] += 1
                        else:
                            issues_list[months][3] += 1
                            issues_list[24][3] += 1
    repo_issue.append(sum(issues_list,[]))

with open('repo_issues.csv', 'w',newline='') as f:
    print("writing..")
    writer = csv.writer(f)
    for i in repo_issue:
        writer.writerow(i)
