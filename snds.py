import requests, time, re, csv, random
from urllib.parse import urljoin
from lxml import html

start_url = "http://www.snds.gov.cn/portal/jsp/portal/interaction/zxzx/zxzx_list.jsp?siteCategoryCode=003001001&styleName=blue&pageNo={}"
# testing2
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
            con = res.text
            soup = html.fromstring(con)
            title = soup.xpath("//th[@scope='col']/text()")
            if title: title= title[0].strip()

            desc = soup.xpath("//td[@class='detail-ask-snds-04-wnfw-01']/text()")
            if desc: desc= desc[0].strip()

            push_time = re.search(r'>提问时间：(.*?)<', con, flags=re.S)
            if push_time: push_time= push_time.group(1)

            content = soup.xpath("//td[@class='detail-answer-snds-04-wnfw-01']")
            if content: content= content[0].xpath("string(.)")

            data_info.append({
                'title': title,
                'desc': desc,
                'push_time': push_time,
                'content': content,
                'url':url
            })
            print(title,push_time,desc,content)
    except:
        get_detail(url)
        time.sleep(30)

def get_list(page):
    try:
        res = requests.get(start_url.format(page), headers=headers)
        soup = html.fromstring(res.content)
        for i in soup.xpath("//td[@align='left']/a/@href"):
            get_detail(urljoin(start_url, i))
            time.sleep(random.randint(3, 7))
    except:
        get_list(page)
        time.sleep(30)

# for i in urls.split():
#     get_detail(i)
#     time.sleep(random.randint(3,7))
for i in range(1, 672):
    get_list(i)
    time.sleep(random.randint(3, 7))
save("snds.csv")