import requests, time, re, csv, random
from urllib.parse import urljoin
from lxml import html

start_url = "http://12366ww.xm-n-tax.gov.cn:8091/xmgsww/WslyBLH_findPageZx.do?r=0.6327293831471326&type=2&cxm=&bt=&sj_djl=undefined&lx=undefined"
detail_url = "http://12366ww.xm-n-tax.gov.cn:8091/xmgsww/WslyBLH_wslyXq.do?initbh={}"

data_info = []
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.170 Safari/537.36"
}
def save(filename):
    file = open(filename, 'w', encoding="utf-8", newline="")

    writer = csv.DictWriter(file, fieldnames=data_info[0].keys())
    writer.writeheader()
    writer.writerows(data_info)

def get_detail(url):
    try:
        res = requests.get(url, headers= headers)
        if res.status_code == 200:
            con = res.content
            res.encoding = "utf-8"
            soup = html.fromstring(con)

            title = soup.xpath("//tr[1]/td[@class='g_t_input']/text()")
            title = title[0].strip() if title else "暂无"


            desc = soup.xpath("//tr[2]/td[@class='g_t_input']/text()")
            desc = desc[0].strip() if desc else "暂无"

            content = soup.xpath("//tr[5]/td[@class='g_t_input']")
            content = content[0].xpath("string(.)") if content else "暂无"


            push_time = soup.xpath("//tr[3]/td[@class='g_t_input'][2]/text()")
            push_time = push_time[0].strip() if push_time else "暂无"

            data_info.append({
                'title': title,
                'desc': desc,
                'push_time': push_time,
                'content': content,
                'url':url
            })
            print(title,push_time,url,desc,content)
    except Exception as e:
        print(e)
        get_detail(url)
        time.sleep(30)

def get_list(page):
    try:

        res = requests.post(start_url,data={'page':page}, headers=headers)
        for item in res.json()['result']['data']:
            get_detail(detail_url.format(item['initbh']))
            time.sleep(1)
    except:
        get_list(page)
        time.sleep(30)

if __name__ == '__main__':
    for p in range(1,1139):
        get_list(p)
        time.sleep(1)
    save("xm-n-tax.csv")