import csv
from urllib.request import urlopen
from urllib.request import Request
import json
import os

rep_list_address = "./rep_list.csv"
reader = csv.reader(open(rep_list_address))
rep_list = [row for row in reader]

headers = {'User-Agent':'Mozilla/5.0',
               'Authorization': 'token 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',
               'Content-Type':'application/json',
               'Accept':'application/json'
               }
print(os.path.exists("./data/commit/freeCodeCamp freeCodeCamp.json"))

for row in rep_list:
    repo = row[0]
    save_address = ".\\data\\commit\\%s.json"%(repo.replace("/", " "))
    if os.path.exists(save_address):
        print(repo, "exists.")
        continue
    url = "https://api.github.com/repos/%s/commits" % (repo)
    req = Request(url, headers=headers)
    openurl = urlopen(req)
    response = openurl.read()

    result_decode = response.decode()
    result_json = json.loads(result_decode)
    remaining_time = openurl.headers["X-RateLimit-Remaining"]
    print("load:",repo)
    print("remaining time:", remaining_time)

    with open(save_address, "w", encoding='utf-8') as f:
        # json.dump(dict_var, f)  # 写为一行
        json.dump(result_json, f, indent=2, sort_keys=True, ensure_ascii=False)  # 写为多行
        print("save...\n")