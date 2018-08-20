import requests, time, re, csv, random
from urllib.parse import urljoin
from lxml import html

start_url1 = "http://old.nb-n-tax.gov.cn/bsfw/12366lx/rdwt/"
start_url2 = "http://old.nb-n-tax.gov.cn/bsfw/12366lx/rdwt/index_{}.htm"

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

            title = soup.xpath("//div[@class='DSjc07']/font/text()")
            title = title[0].strip() if title else "暂无"
            detail_info = soup.xpath("//td//p")


            desc = detail_info[0].xpath("string(.)").strip() if detail_info else "暂无"

            content = [conn.xpath("string(.)").strip() for conn in  detail_info[1:]] if detail_info else '暂无'
            content = ''.join(content)


            push_time = soup.xpath("//td[@id='tb1']/table[1]/tr/td/text()")
            if push_time:
                push_time = push_time[0].strip().split("\xa0\xa0\xa0\xa0")
                push_time = push_time[0].replace("发布时间：", '').strip() if push_time else "暂无"

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
        if page == 0:
            res = requests.get(start_url1, headers=headers, timeout=5)
        else:
            res = requests.get(start_url2.format(page), headers=headers)
        soup = html.fromstring(res.content)
        for i in soup.xpath("//table[@class='DSjc04']/tr/td[2]/a/@href"):
            get_detail(urljoin(start_url1, i))
            time.sleep(random.randint(3, 7))
    except Exception as e:
        print(page,"失败重试：{}".format(e))
        get_list(page)
        time.sleep(30)

for i in range(0, 52):
    get_list(i)
    # time.sleep(random.randint(3, 7))
save("nb-n-tax.csv")