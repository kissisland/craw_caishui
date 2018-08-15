import requests, time, re, csv
from urllib.parse import urljoin
from lxml import html

start_url = "http://12366.he-n-tax.gov.cn/WslyBLH_findPageZx.do?r=0.8383920276229324&type=2&kssj=&jssj=&bt="

data_info = []

def save(filename):
    file = open(filename, 'w', encoding="utf-8", newline="")

    writer = csv.DictWriter(file, fieldnames=data_info[0].keys())
    writer.writeheader()
    writer.writerows(data_info)

def get_detail(url):
    res = requests.get(url)
    soup = html.fromstring(res.content)
    print(res.text)
    # title = soup.xpath("//div[@class='pageFormContent']/div[@id='t']/div[@class='table']/table[@class='sheet2']/tbody/tr[1]/td[@class='g_t_input']/text()")
    # if title: title= title[0]
    #
    # desc = soup.xpath("//div[@class='table']/table[@class='sheet2']/tbody/tr[2]/td[@class='g_t_input']/text()")
    # if desc: desc= desc[0]
    #
    # push_time = soup.xpath("//div[@class='table']/table[@class='sheet2']/tbody/tr[3]/td[@class='g_t_input'][2]/text()")
    # if push_time: push_time= push_time[0]
    #
    # content = soup.xpath("//div[@class='table']/table[@class='sheet2']/tbody/tr[5]/td[@class='g_t_input']")
    # if content: content= content[0].xpath("string(.)")
    #
    # data_info.append({
    #     'title': title.strip(),
    #     'desc': desc.strip(),
    #     'push_time': push_time.strip(),
    #     'content': content
    # })
    # print(title, desc, push_time, content)

def get_list(page):
    res = requests.get(start_url.format(page))
    content = res.text

    lists = re.findall(r"<a href='(display\.asp\?more_id=.*?)'>", content, flags=re.S)

    for i in [urljoin(start_url, item) for item in lists]:
        get_detail(i)
        time.sleep(5)

get_detail("http://12366.he-n-tax.gov.cn/WslyBLH_wslyXq.do?initbh=ww20180705016226")

# save("tax81.csv")