import requests, time, re, csv, random
from urllib.parse import urljoin
from lxml import html

start_url = "http://222.82.232.6/consult/publish/question.jsp?catId=1&gotoPage={}"
detail_url = "http://222.82.232.6/consult/publish/showQuestion.jsp?{}"
data_info = []
headers = {
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Encoding":"gzip, deflate",
    "Accept-Language":"zh-CN,zh;q=0.9,zh-TW;q=0.8,en-US;q=0.7,en;q=0.6",
    "Cache-Control":"max-age=0",
    "Connection":"keep-alive",
    "Cookie":"JSESSIONID=63hGiH1AQBmaxAgMGMJXMhhWqiP_h5foXhOGc5jgCOHkEN2RwCQN!-322051910",
    "Host":"222.82.232.6",
    "Referer":"http://222.82.232.6/consult/publish/question.jsp?catId=1&gotoPage=1",
    "Upgrade-Insecure-Requests":"1",
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
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
            title = soup.xpath('//table[@bgcolor="#5871AA"]/tr[2]/td[2]/text()')
            if title:
                title = title[0].strip()
            else:
                title = "暂无"
            ask_content = soup.xpath('//table[@bgcolor="#5871AA"]/tr[3]/td[2]/table/tr/td/text()')
            if ask_content:
                ask_content= ask_content[0].strip()
            else:
                ask_content = "暂无"

            answer_content = soup.xpath('/html/body/table/tr[1]/td[1]/table[4]/tr[2]/td[2]/table/tr/td')
            if answer_content:
                answer_content = answer_content[0].xpath("string(.)")
            else:
                answer_content = "暂无"
            push_time = soup.xpath("/html/body/table/tr[1]/td[1]/table[4]/tr[1]/td[4]/text()")
            if push_time: push_time = push_time[0].split()[0]

            data_info.append({
                'title':title,
                'push_time':push_time,
                'ask_content':ask_content,
                'answer_content':answer_content,
                'url':url
            })

            print(title, push_time, ask_content, answer_content)
    except:
        get_detail(url)
        time.sleep(random.randrange(5))

def get_list(num_page):
    try:
        res = requests.get(start_url.format(num_page), headers=headers)
        soup = html.fromstring(res.content)
        for i in soup.xpath("//a[@class='b']/@onclick"):
            detail_id = re.search(r".jsp\?(.*?)'", i)
            if detail_id:
                detail_id = detail_id.group(1)
            get_detail(detail_url.format(detail_id))
            time.sleep(random.randint(3, 7))
    except Exception as e:
        print(e)
        get_list(page)
        time.sleep(30)

if __name__ == '__main__':
    for page in range(0, 471):
        get_list(page)
        time.sleep(random.randint(3, 10))
    save("nxgs.csv")