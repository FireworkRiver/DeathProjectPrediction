from urllib.request import urlopen
from urllib.request import Request
import datetime
import json

headers = {'User-Agent':'Mozilla/5.0',
               'Authorization': 'token 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',
               'Content-Type':'application/json',
               'Accept':'application/json'
               }
page_num=101
max_stars = 3376

for i in range(1,1+10):
    print("read page %d" % (i+page_num-1))
    url ="https://api.github.com/search/repositories?q=stars:1000..%d&sort=stars&per_page=100&page=%d"%(max_stars,i)
    req = Request(url,headers=headers)
    openurl= urlopen(req)
    response = openurl.read()

    result_decode = response.decode()
    result_json = json.loads(result_decode)

    print("max stars:",result_json["items"][0]["stargazers_count"])
    print("min stars:", result_json["items"][99]["stargazers_count"])
    with open(".\\data\\repositories\\page%d.json"%(i+page_num-1), "w", encoding='utf-8') as f:
        # json.dump(dict_var, f)  # 写为一行
        json.dump(result_json, f, indent=2, sort_keys=True, ensure_ascii=False)  # 写为多行

    remaining_time = openurl.headers["X-RateLimit-Remaining"]
    print("remaining time:",remaining_time)

    print("read finish\n")
