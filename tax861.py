import requests, time, re, csv
from urllib.parse import urljoin
from lxml import html

start_url = "http://shiju.tax861.gov.cn/gzcy/wyzx/wyzxhf.asp?aa={}"

data_info = []

def save(filename):
    file = open(filename, 'w', encoding="utf-8", newline="")

    writer = csv.DictWriter(file, fieldnames=data_info[0].keys())
    writer.writeheader()
    writer.writerows(data_info)

def get_detail(url):
    res = requests.get(url)
    soup = html.fromstring(res.content)

    title = soup.xpath("//div[@id='div_bt']/text()")
    if title: title= title[0]

    push_time = soup.xpath("//td[@id='td_date']/text()")
    if push_time: push_time= push_time[0]

    content = soup.xpath("//div[@id='div_zhengwen']")
    if content: content= content[0].xpath("string(.)")

    data_info.append({
        'title': title.strip(),
        'push_time': push_time.strip(),
        'content': content
    })
    print(title, push_time, content)

def get_list(page):
    res = requests.get(start_url.format(page))
    content = res.text

    lists = re.findall(r"<a href='(display\.asp\?more_id=.*?)'>", content, flags=re.S)

    for i in [urljoin(start_url, item) for item in lists]:
        get_detail(i)
        time.sleep(5)

for i in range(1, 11):
    get_list(i)

save("tax81.csv")