import requests, time, re
from urllib.parse import urljoin
from lxml import html
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

start_url = "http://www.chinatax.gov.cn/n810356/n3255681/index.html"


# def detail(url):
#     res = requests.get(url, headers=headers)
#     if res.status_code == 200:
#         soup = html.fromstring(res.content)
#         title = soup.xpath("//li[@class='sv_texth1']/text()")
#         if title: title = title[0]
#
#         content = soup.xpath("//ul[@class='sv_textcon']/li[@id='tax_content']/p/img/@src")
#         if content: content = content[0]
#     else:
#         detail(url)
#         time.sleep(3)
#
#     print(title, content, url)

# def lists_info():
#     res = requests.get(start_url, headers=headers)
#     time.sleep(5)
#     content = res.text
#     pages = re.search(r"<div style='display:none'><a href='(.*?)'></a><a href='(.*?)'></a><a href='(.*?)'></a><a href='(.*?)'></a></div>",
#               content, flags=re.S)
#
#     if pages:
#         pages = pages.groups()
#
#     url_lists = [urljoin(start_url, page) for page in pages]
#     url_lists.insert(0, start_url)
#     return [url for url in url_lists]

def list_pares(url):
    browser = webdriver.Chrome("E:\chromedriver.exe")
    browser.get(url)
    # datas = browser.find_element_by_xpath("//div[@class='column']")
    next_page = browser.find_element_by_xpath("//div[@class='column']/table[@class='pageN']/tbody/tr/td/a[text()='下页']")
    if next_page:
        next_page.click()
    # if datas:
    #     datas = browser.find_elements_by_xpath("//div[@class='column']/span/dl/dd/a")
    #     for i in datas:
    #         i.click()
    #         time.sleep(4)
    #         ActionChains(browser).key_down(Keys.CONTROL).send_keys("w").key_up(Keys.CONTROL).perform()


            # if soup.xpath():
    #     datas = soup.xpath("//div[@class='column']/span/dl/dd/a/@href")
    #
    # else:
    #     datas = soup.xpath("//dl/dd/a/@href")
    # if datas:
    #     for i in [urljoin(start_url, data) for data in datas]:
    #         time.sleep(20)
    #         detail(i)



if __name__ == '__main__':
    # for item in [list_pares(i) for i in lists_info()]:
    #     for k in item:
    #         time.sleep(20)
    #         detail(k)

    list_pares("http://www.chinatax.gov.cn/n810356/n3255681/index.html")
