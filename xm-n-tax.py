import requests, time, re, csv, random
from urllib.parse import urljoin
from lxml import html

start_url = "http://12366ww.xm-n-tax.gov.cn:8091/xmgsww/WslyBLH_findPageZx.do?r=0.13276405784518075&type=2&cxm=&bt=&sj_djl=undefined&lx=undefined"
detail_url = "http://12366ww.xm-n-tax.gov.cn:8091/xmgsww/WslyBLH_wslyXq.do?initbh={}"


data_info = []
headers = {
    "Accept":"*/*",
    "Accept-Encoding":"gzip, deflate",
    "Accept-Language":"zh-CN,zh;q=0.9,zh-TW;q=0.8,en-US;q=0.7,en;q=0.6",
    "Connection":"keep-alive",
    "Content-Type":"application/x-www-form-urlencoded;utf-8",
    "Cookie":"JSESSIONID=zqlaVf91QS5UN-7bE2jZ8Q789woIdFBYxwVhzH6FwKB0qQ00xmUU!1956117633",
    "Host":"12366ww.xm-n-tax.gov.cn:8091",
    "Origin":"http://12366ww.xm-n-tax.gov.cn:8091",
    "Referer":"http://12366ww.xm-n-tax.gov.cn:8091/xmgsww/WslyBLH_tozxzx.do?type=2",
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
    "X-Requested-With":"XMLHttpRequest",
}
headers2 = {
"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
}
def save(filename):
    file = open(filename, 'w', encoding="utf-8", newline="")

    writer = csv.DictWriter(file, fieldnames=data_info[0].keys())
    writer.writeheader()
    writer.writerows(data_info)

def get_detail(url):
    try:
        res = requests.get(url, headers= headers2, timeout=5)
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
        print(e, url)
        time.sleep(random.randint(300, 600))
        get_detail(url)


def get_list(page):
    try:
        res = requests.post(start_url,data={'page':page}, headers=headers, timeout=5)
        if res.status_code == 200:
            for item in res.json()['result']['data']:
                get_detail(detail_url.format(item['initbh']))
                time.sleep(random.randint(5,20))
        else:
            get_list(page)
    except Exception as e:
        print("出现异常：{}".format(e))
        time.sleep(30)
        get_list(page)


if __name__ == '__main__':
    for p in range(1,1139):
        get_list(p)
        time.sleep(random.randint(10,30))
    save("xm-n-tax.csv")
