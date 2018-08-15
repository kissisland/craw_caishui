import requests, time, re, csv, random
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

    title = soup.xpath("//div[@class='box_con']/div[@id='wzpl_wzbt']/text()")
    if title: title= title[0]

    # desc = soup.xpath("//div[@class='table']/table[@class='sheet2']/tbody/tr[2]/td[@class='g_t_input']/text()")
    # if desc: desc= desc[0]

    push_time = soup.xpath("//div[@class='content']/div[@class='box_con']/div[2]/text()")
    if push_time: push_time= push_time[0]

    content = soup.xpath("//div[@class='TRS_Editor']")
    if content: content= content[0].xpath("string(.)")

    data_info.append({
        'title': title.strip(),
        # 'desc': desc.strip(),
        'push_time': push_time.strip(),
        'content': content,
        'url':url
    })
    print(title, push_time, content)

def get_list(page):
    res = requests.get(start_url.format(page))
    content = res.text

    lists = re.findall(r"<a href='(display\.asp\?more_id=.*?)'>", content, flags=re.S)

    for i in [urljoin(start_url, item) for item in lists]:
        get_detail(i)
        time.sleep(5)

urls = """
http://www.cqsw.gov.cn/cqsswj/hdjl/rdwt/zzs/201807/t20180726_283229.html
http://www.cqsw.gov.cn/cqsswj/hdjl/rdwt/zzs/201807/t20180726_283230.html
http://www.cqsw.gov.cn/cqsswj/hdjl/rdwt/zzs/201807/t20180718_283174.html
http://www.cqsw.gov.cn/cqsswj/hdjl/rdwt/zzs/201807/t20180718_283175.html
http://www.cqsw.gov.cn/cqsswj/hdjl/rdwt/zzs/201807/t20180711_283141.html
http://www.cqsw.gov.cn/cqsswj/hdjl/rdwt/zzs/201807/t20180711_283140.html
http://www.cqsw.gov.cn/cqsswj/hdjl/rdwt/zzs/201807/t20180709_283115.html
http://www.cqsw.gov.cn/cqsswj/hdjl/rdwt/zzs/201807/t20180709_283114.html
http://www.cqsw.gov.cn/cqsswj/hdjl/rdwt/zzs/201805/t20180525_280487.html
http://www.cqsw.gov.cn/cqsswj/hdjl/rdwt/zzs/201805/t20180525_280486.html
http://www.cqsw.gov.cn/cqsswj/hdjl/rdwt/zzs/201805/t20180525_280485.html
http://www.cqsw.gov.cn/cqsswj/hdjl/rdwt/zzs/201805/t20180525_280490.html
http://www.cqsw.gov.cn/cqsswj/hdjl/rdwt/zzs/201805/t20180525_280489.html
http://www.cqsw.gov.cn/cqsswj/hdjl/rdwt/zzs/201805/t20180525_280493.html
http://www.cqsw.gov.cn/cqsswj/hdjl/rdwt/zzs/201805/t20180525_280492.html
http://www.cqsw.gov.cn/cqsswj/hdjl/rdwt/zzs/201805/t20180525_280491.html
http://www.cqsw.gov.cn/cqsswj/hdjl/rdwt/zzs/201805/t20180525_280501.html
http://www.cqsw.gov.cn/cqsswj/hdjl/rdwt/zzs/201805/t20180525_280499.html
http://www.cqsw.gov.cn/cqsswj/hdjl/rdwt/zzs/201805/t20180525_280500.html
http://www.cqsw.gov.cn/cqsswj/hdjl/rdwt/zzs/201805/t20180525_280498.html
http://www.cqsw.gov.cn/cqsswj/hdjl/rdwt/zzs/201805/t20180525_280497.html
http://www.cqsw.gov.cn/cqsswj/hdjl/rdwt/zzs/201805/t20180525_280496.html
http://www.cqsw.gov.cn/cqsswj/hdjl/rdwt/zzs/201805/t20180525_280495.html
http://www.cqsw.gov.cn/cqsswj/hdjl/rdwt/zzs/201805/t20180525_280494.html
http://www.cqsw.gov.cn/cqsswj/hdjl/rdwt/zzs/201805/t20180525_280505.html
http://www.cqsw.gov.cn/cqsswj/hdjl/rdwt/zzs/201805/t20180525_280504.html
http://www.cqsw.gov.cn/cqsswj/hdjl/rdwt/zzs/201805/t20180525_280503.html
http://www.cqsw.gov.cn/cqsswj/hdjl/rdwt/qysds/201807/t20180726_283228.html
http://www.cqsw.gov.cn/cqsswj/hdjl/rdwt/qysds/201807/t20180726_283227.html
http://www.cqsw.gov.cn/cqsswj/hdjl/rdwt/qysds/201807/t20180718_283173.html
http://www.cqsw.gov.cn/cqsswj/hdjl/rdwt/qysds/201807/t20180718_283172.html
http://www.cqsw.gov.cn/cqsswj/hdjl/rdwt/qysds/201807/t20180711_283139.html
http://www.cqsw.gov.cn/cqsswj/hdjl/rdwt/qysds/201807/t20180711_283138.html
http://www.cqsw.gov.cn/cqsswj/hdjl/rdwt/qysds/201807/t20180709_283113.html
http://www.cqsw.gov.cn/cqsswj/hdjl/rdwt/qysds/201807/t20180709_283112.html
http://www.cqsw.gov.cn/cqsswj/hdjl/rdwt/qysds/201805/t20180525_280528.html
http://www.cqsw.gov.cn/cqsswj/hdjl/rdwt/qysds/201805/t20180525_280533.html
http://www.cqsw.gov.cn/cqsswj/hdjl/rdwt/qysds/201805/t20180525_280532.html
http://www.cqsw.gov.cn/cqsswj/hdjl/rdwt/qysds/201805/t20180525_280531.html
http://www.cqsw.gov.cn/cqsswj/hdjl/rdwt/qysds/201805/t20180525_280530.html
http://www.cqsw.gov.cn/cqsswj/hdjl/rdwt/qysds/201805/t20180525_280529.html
http://www.cqsw.gov.cn/cqsswj/hdjl/rdwt/qysds/201805/t20180525_280518.html
http://www.cqsw.gov.cn/cqsswj/hdjl/rdwt/qysds/201805/t20180525_280517.html
http://www.cqsw.gov.cn/cqsswj/hdjl/rdwt/qysds/201805/t20180525_280516.html
http://www.cqsw.gov.cn/cqsswj/hdjl/rdwt/qysds/201805/t20180525_280515.html
http://www.cqsw.gov.cn/cqsswj/hdjl/rdwt/qysds/201805/t20180525_280520.html
http://www.cqsw.gov.cn/cqsswj/hdjl/rdwt/qysds/201805/t20180525_280522.html
http://www.cqsw.gov.cn/cqsswj/hdjl/rdwt/qysds/201805/t20180525_280519.html
http://www.cqsw.gov.cn/cqsswj/hdjl/rdwt/qysds/201805/t20180525_280512.html
http://www.cqsw.gov.cn/cqsswj/hdjl/rdwt/qysds/201805/t20180525_280527.html
http://www.cqsw.gov.cn/cqsswj/hdjl/rdwt/qysds/201805/t20180525_280526.html
http://www.cqsw.gov.cn/cqsswj/hdjl/rdwt/qysds/201805/t20180525_280523.html
http://www.cqsw.gov.cn/cqsswj/hdjl/rdwt/qysds/201805/t20180525_280524.html
http://www.cqsw.gov.cn/cqsswj/hdjl/rdwt/xfs/201807/t20180726_283234.html
http://www.cqsw.gov.cn/cqsswj/hdjl/rdwt/xfs/201807/t20180726_283233.html
http://www.cqsw.gov.cn/cqsswj/hdjl/rdwt/xfs/201807/t20180718_283178.html
http://www.cqsw.gov.cn/cqsswj/hdjl/rdwt/xfs/201807/t20180718_283179.html
http://www.cqsw.gov.cn/cqsswj/hdjl/rdwt/xfs/201807/t20180711_283145.html
http://www.cqsw.gov.cn/cqsswj/hdjl/rdwt/xfs/201807/t20180711_283144.html
http://www.cqsw.gov.cn/cqsswj/hdjl/rdwt/xfs/201807/t20180709_283119.html
http://www.cqsw.gov.cn/cqsswj/hdjl/rdwt/xfs/201807/t20180709_283118.html
http://www.cqsw.gov.cn/cqsswj/hdjl/rdwt/xfs/201805/t20180525_280671.html
http://www.cqsw.gov.cn/cqsswj/hdjl/rdwt/xfs/201805/t20180525_280547.html
http://www.cqsw.gov.cn/cqsswj/hdjl/rdwt/xfs/201805/t20180525_280548.html
http://www.cqsw.gov.cn/cqsswj/hdjl/rdwt/xfs/201805/t20180525_280557.html
http://www.cqsw.gov.cn/cqsswj/hdjl/rdwt/xfs/201805/t20180525_280556.html
http://www.cqsw.gov.cn/cqsswj/hdjl/rdwt/xfs/201805/t20180525_280558.html
http://www.cqsw.gov.cn/cqsswj/hdjl/rdwt/xfs/201805/t20180525_280541.html
http://www.cqsw.gov.cn/cqsswj/hdjl/rdwt/xfs/201805/t20180525_280542.html
http://www.cqsw.gov.cn/cqsswj/hdjl/rdwt/xfs/201805/t20180525_280550.html
http://www.cqsw.gov.cn/cqsswj/hdjl/rdwt/xfs/201805/t20180525_280545.html
http://www.cqsw.gov.cn/cqsswj/hdjl/rdwt/xfs/201805/t20180525_280546.html
http://www.cqsw.gov.cn/cqsswj/hdjl/rdwt/xfs/201805/t20180525_280540.html
http://www.cqsw.gov.cn/cqsswj/hdjl/rdwt/clgzs/201807/t20180726_283232.html
http://www.cqsw.gov.cn/cqsswj/hdjl/rdwt/clgzs/201807/t20180726_283231.html
http://www.cqsw.gov.cn/cqsswj/hdjl/rdwt/clgzs/201807/t20180718_283177.html
http://www.cqsw.gov.cn/cqsswj/hdjl/rdwt/clgzs/201807/t20180718_283176.html
http://www.cqsw.gov.cn/cqsswj/hdjl/rdwt/clgzs/201807/t20180711_283142.html
http://www.cqsw.gov.cn/cqsswj/hdjl/rdwt/clgzs/201807/t20180711_283143.html
http://www.cqsw.gov.cn/cqsswj/hdjl/rdwt/clgzs/201807/t20180709_283117.html
http://www.cqsw.gov.cn/cqsswj/hdjl/rdwt/clgzs/201807/t20180709_283116.html
http://www.cqsw.gov.cn/cqsswj/hdjl/rdwt/clgzs/201805/t20180525_280657.html
http://www.cqsw.gov.cn/cqsswj/hdjl/rdwt/clgzs/201805/t20180525_280666.html
http://www.cqsw.gov.cn/cqsswj/hdjl/rdwt/clgzs/201805/t20180525_280674.html
http://www.cqsw.gov.cn/cqsswj/hdjl/rdwt/clgzs/201805/t20180525_280673.html
http://www.cqsw.gov.cn/cqsswj/hdjl/rdwt/clgzs/201805/t20180525_280672.html
http://www.cqsw.gov.cn/cqsswj/hdjl/rdwt/clgzs/201805/t20180525_280668.html
http://www.cqsw.gov.cn/cqsswj/hdjl/rdwt/clgzs/201805/t20180525_280670.html
http://www.cqsw.gov.cn/cqsswj/hdjl/rdwt/clgzs/201805/t20180525_280659.html
http://www.cqsw.gov.cn/cqsswj/hdjl/rdwt/clgzs/201805/t20180525_280662.html
http://www.cqsw.gov.cn/cqsswj/hdjl/rdwt/clgzs/201805/t20180525_280664.html
http://www.cqsw.gov.cn/cqsswj/hdjl/rdwt/clgzs/201805/t20180525_280654.html
http://www.cqsw.gov.cn/cqsswj/hdjl/rdwt/clgzs/201805/t20180525_280655.html
http://www.cqsw.gov.cn/cqsswj/hdjl/rdwt/clgzs/201805/t20180525_280656.html
http://www.cqsw.gov.cn/cqsswj/hdjl/rdwt/clgzs/201805/t20180525_280667.html
http://www.cqsw.gov.cn/cqsswj/hdjl/rdwt/hbs/201807/t20180726_283236.html
http://www.cqsw.gov.cn/cqsswj/hdjl/rdwt/hbs/201807/t20180726_283235.html
http://www.cqsw.gov.cn/cqsswj/hdjl/rdwt/hbs/201807/t20180718_283180.html
http://www.cqsw.gov.cn/cqsswj/hdjl/rdwt/hbs/201807/t20180718_283181.html
http://www.cqsw.gov.cn/cqsswj/hdjl/rdwt/hbs/201807/t20180711_283146.html
http://www.cqsw.gov.cn/cqsswj/hdjl/rdwt/hbs/201807/t20180711_283147.html
http://www.cqsw.gov.cn/cqsswj/hdjl/rdwt/hbs/201807/t20180709_283122.html
http://www.cqsw.gov.cn/cqsswj/hdjl/rdwt/hbs/201807/t20180709_283123.html
http://www.cqsw.gov.cn/cqsswj/hdjl/rdwt/hbs/201805/t20180523_280367.html
http://www.cqsw.gov.cn/cqsswj/hdjl/rdwt/hbs/201805/t20180523_280368.html
http://www.cqsw.gov.cn/cqsswj/hdjl/rdwt/hbs/201805/t20180523_280366.html
http://www.cqsw.gov.cn/cqsswj/hdjl/rdwt/hbs/201805/t20180523_280365.html
http://www.cqsw.gov.cn/cqsswj/hdjl/rdwt/hbs/201805/t20180523_280364.html
http://www.cqsw.gov.cn/cqsswj/hdjl/rdwt/hbs/201805/t20180523_280363.html
http://www.cqsw.gov.cn/cqsswj/hdjl/rdwt/grsds/201807/t20180726_283238.html
http://www.cqsw.gov.cn/cqsswj/hdjl/rdwt/grsds/201807/t20180726_283237.html
http://www.cqsw.gov.cn/cqsswj/hdjl/rdwt/grsds/201807/t20180718_283182.html
http://www.cqsw.gov.cn/cqsswj/hdjl/rdwt/grsds/201807/t20180718_283183.html
http://www.cqsw.gov.cn/cqsswj/hdjl/rdwt/grsds/201807/t20180711_283148.html
http://www.cqsw.gov.cn/cqsswj/hdjl/rdwt/grsds/201807/t20180711_283149.html
http://www.cqsw.gov.cn/cqsswj/hdjl/rdwt/grsds/201807/t20180709_283120.html
http://www.cqsw.gov.cn/cqsswj/hdjl/rdwt/grsds/201807/t20180709_283121.html
http://www.cqsw.gov.cn/cqsswj/hdjl/rdwt/grsds/201805/t20180523_280385.html
http://www.cqsw.gov.cn/cqsswj/hdjl/rdwt/grsds/201805/t20180523_280386.html
http://www.cqsw.gov.cn/cqsswj/hdjl/rdwt/grsds/201805/t20180523_280384.html
http://www.cqsw.gov.cn/cqsswj/hdjl/rdwt/grsds/201805/t20180523_280383.html
http://www.cqsw.gov.cn/cqsswj/hdjl/rdwt/grsds/201805/t20180523_280381.html
http://www.cqsw.gov.cn/cqsswj/hdjl/rdwt/grsds/201805/t20180523_280382.html
http://www.cqsw.gov.cn/cqsswj/hdjl/rdwt/grsds/201805/t20180523_280380.html
http://www.cqsw.gov.cn/cqsswj/hdjl/rdwt/grsds/201805/t20180523_280378.html
http://www.cqsw.gov.cn/cqsswj/hdjl/rdwt/grsds/201805/t20180523_280379.html
http://www.cqsw.gov.cn/cqsswj/hdjl/rdwt/grsds/201805/t20180523_280377.html
http://www.cqsw.gov.cn/cqsswj/hdjl/rdwt/grsds/201805/t20180523_280376.html
http://www.cqsw.gov.cn/cqsswj/hdjl/rdwt/grsds/201805/t20180523_280374.html
http://www.cqsw.gov.cn/cqsswj/hdjl/rdwt/grsds/201805/t20180523_280375.html
http://www.cqsw.gov.cn/cqsswj/hdjl/rdwt/grsds/201805/t20180523_280373.html
http://www.cqsw.gov.cn/cqsswj/hdjl/rdwt/grsds/201805/t20180523_280372.html
http://www.cqsw.gov.cn/cqsswj/hdjl/rdwt/grsds/201805/t20180523_280370.html
http://www.cqsw.gov.cn/cqsswj/hdjl/rdwt/grsds/201805/t20180523_280371.html
http://www.cqsw.gov.cn/cqsswj/hdjl/rdwt/grsds/201805/t20180523_280369.html
"""

for i in urls.split():

    get_detail(i.strip())
    time.sleep(random.randint(2,7))

save("cqsw.csv")