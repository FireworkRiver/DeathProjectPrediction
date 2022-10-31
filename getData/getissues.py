from urllib.request import urlopen
from urllib.request import Request
import json
import os
import re
import csv
from datetime import datetime, timedelta
import time

headers = {'User-Agent':'Mozilla/5.0',
               'Authorization': 'token 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',
               'Content-Type':'application/json',
               'Accept':'application/json'
               }

def getissues(repo,page,repo_dir,time):
    url = "https://api.github.com/repos/%s/issues?state=all&since=%s&sort=updated&direction=asc&direction=asc&per_page=100&page=%d" % (repo, time,page)
    req = Request(url, headers=headers)
    openurl = urlopen(req)
    response = openurl.read()

    result_decode = response.decode()
    result_json = json.loads(result_decode)

    with open(repo_dir+"/page%d.json" % (page), "w", encoding='utf-8') as f:
        json.dump(result_json, f, indent=2, sort_keys=True, ensure_ascii=False)  # 写为多行

    remaining_time = int(openurl.headers["X-RateLimit-Remaining"])
    print("remaining time:", remaining_time)

    link = openurl.headers["Link"]
    if link == None:
        last_page_num = 1
    else:
        last_page = re.findall(r'page=(\d+)>; rel="last"', link)
        if len(last_page)>0:
            last_page_num = int(last_page[0])
        else:
            last_page_num = 0
    print("last page:", last_page_num)
    print("current page",page)

    return remaining_time,last_page_num

root = 'E:/Death project/data/issues'
rep_list_address = "./rep_commit.csv"
reader = csv.reader(open(rep_list_address))
rep_list = [row for row in reader]
flag = True
twoyear = timedelta(days=730)

not_finish = True
while(not_finish):
    try:
        for row in rep_list:
            repo = row[0]
            last_commit_time = row[1]
            begin_date = datetime.strptime(last_commit_time, '%Y-%m-%dT%H:%M:%SZ') - twoyear
            begin_time = begin_date.strftime('%Y-%m-%dT%H:%M:%SZ')
            repo_dir = root + "/" + repo.replace("/", " ")
            if flag == False:
                break

            if not os.path.exists(repo_dir):
                os.makedirs(repo_dir)
                print("create dir:", repo)
                remaining_time, last_page_num = getissues(repo, 1, repo_dir, begin_time)
                with open(repo_dir + "/pageNum.txt", "w") as fo:
                    fo.write(str(last_page_num))
                for i in range(2, last_page_num + 1):
                    remaining_time, _ = getissues(repo, i, repo_dir, begin_time)
                    if remaining_time < 100 or remaining_time < last_page_num:
                        flag = False
                print("read finish\n")
            else:
                if os.path.exists(repo_dir + "/pageNum.txt"):
                    fo = open(repo_dir + "/pageNum.txt", "r")
                    last_page_num = int(fo.read())
                    if os.path.exists(repo_dir + "/page%d.json" % (last_page_num)):
                        print(repo, "read finish.")
                        continue
                    print("last page:", last_page_num)
                else:
                    remaining_time, last_page_num = getissues(repo, 1, repo_dir, begin_time)
                    with open(repo_dir + "/pageNum.txt", "w") as fo:
                        fo.write(str(last_page_num))
                    print("read", repo)
                for i in range(1, last_page_num + 1):
                    if os.path.exists(repo_dir + "/page%d.json" % (i)):
                        continue
                    else:
                        remaining_time, _ = getissues(repo, i, repo_dir, begin_time)
                        if remaining_time < 50:
                            flag = False
                print("read finish\n")
        not_finish = False
    except:
        print("Error.")
        time.sleep(10)

