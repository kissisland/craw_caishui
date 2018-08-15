import requests, time, re
from urllib.parse import urljoin
from lxml import html

start_url = "http://www.chinatax.gov.cn/n810356/n3255681/index.html"

headers = {
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Encoding":"gzip, deflate",
    "Accept-Language":"zh-CN,zh;q=0.9,zh-TW;q=0.8,en-US;q=0.7,en;q=0.6",
    "Cache-Control":"max-age=0",
    "Cookie":"maxPageNum3266758=5; _gscu_244235366=3378539022mhwx20; _gscbrs_244235366=1; gwdshare_firstime=1533785390752; yfx_c_g_u_id_10003701=_ck18080911295017643330411101743; _Jo0OQK=1AD2BCA2EBD4199D9692D7ECDA24B83D59A7D9F84EFC104D054BEFD99E7705184DDC21AB1763049EFFB190507CD2DAE213D20A77C1F25A27E5DB352F0033AF819EC34275DAD340EB4DDFFF13AA80B4DD4EFFFF13AA80B4DD4EF9745663BE512BB048C9AF81BA121EF63GJ1Z1cQ==; yfx_f_l_v_t_10003701=f_t_1533785390761__r_t_1533785390761__v_t_1533807802969__r_c_0; _gscs_244235366=t338051641yn0kn10|pv:20",
    "Host":"www.chinatax.gov.cn",
    "If-Modified-Since":"Thu, 09 Aug 2018 00:03:16 GMT",
    "If-None-Match":"5200000007f69f-47d5-572f55aa2df8b",
    "Proxy-Connection":"keep-alive",
    "Referer":"http://www.chinatax.gov.cn/n810356/n3255681/index.html",
    "Upgrade-Insecure-Requests":"1",
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.170 Safari/537.36",
}

def detail(url):
    res = requests.get(url, headers=headers)
    if res.status_code == 200:
        soup = html.fromstring(res.content)
        title = soup.xpath("//li[@class='sv_texth1']/text()")
        if title: title = title[0]

        content = soup.xpath("//ul[@class='sv_textcon']/li[@id='tax_content']/p/img/@src")
        if content: content = content[0]
    else:
        detail(url)
        time.sleep(3)

    print(title, content, url)

def lists_info():
    res = requests.get(start_url, headers=headers)
    time.sleep(5)
    content = res.text
    pages = re.search(r"<div style='display:none'><a href='(.*?)'></a><a href='(.*?)'></a><a href='(.*?)'></a><a href='(.*?)'></a></div>",
              content, flags=re.S)

    if pages:
        pages = pages.groups()

    url_lists = [urljoin(start_url, page) for page in pages]
    url_lists.insert(0, start_url)
    return [url for url in url_lists]

def list_pares(url):
    res = requests.get(url, headers=headers)
    time.sleep(5)
    res.encoding = 'utf-8'
    content = res.content

    soup = html.fromstring(content)
    if soup.xpath("//div[@class='column']"):
        datas = soup.xpath("//div[@class='column']/span/dl/dd/a/@href")

    else:
        datas = soup.xpath("//dl/dd/a/@href")
    if datas:
        for i in [urljoin(start_url, data) for data in datas]:
            time.sleep(20)
            detail(i)



if __name__ == '__main__':
    # for item in [list_pares(i) for i in lists_info()]:
    #     for k in item:
    #         time.sleep(20)
    #         detail(k)

    list_pares("http://www.chinatax.gov.cn/n810356/n3255681/index.html")
