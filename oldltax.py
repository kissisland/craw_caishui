import requests, time, re, csv, random
from urllib.parse import urljoin
from lxml import html

start_url = "http://12366.he-n-tax.gov.cn/WslyBLH_findPageZx.do?r=0.8383920276229324&type=2&kssj=&jssj=&bt="

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
    res = requests.get(url, headers= headers)
    soup = html.fromstring(res.text)
    title = soup.xpath("//th[@scope='col']/text()")
    if title: title= title[0].strip()

    desc = soup.xpath("//td[@class='detail-ask-snds-04-wnfw-01']/text()")
    if desc: desc= desc[0].strip()

    # push_time = soup.xpath("//td[@class='detail-time-snds-04-wnfw-01']/table/tbody/tr/td[1]/text()")
    # if push_time: push_time= push_time[0]

    content = soup.xpath("//td[@class='detail-answer-snds-04-wnfw-01']")
    if content: content= content[0].xpath("string(.)")

    data_info.append({
        'title': title,
        'desc': desc,
        # 'push_time': push_time.strip(),
        'content': content,
        'url':url
    })
    print(title,desc,content)

def get_list(page):
    res = requests.get(start_url.format(page))
    content = res.text

    lists = re.findall(r"<a href='(display\.asp\?more_id=.*?)'>", content, flags=re.S)

    for i in [urljoin(start_url, item) for item in lists]:
        get_detail(i)
        time.sleep(5)

urls = """
http://www.sn-n-tax.gov.cn/portal/jsp/portal/interaction/zxzx/zxzx_result.jsp?siteCategoryCode=003001007&styleName=blue&contentId=LU6HN76CD6HQYU7MTGCXD5X23CWBEKRM
http://www.sn-n-tax.gov.cn/portal/jsp/portal/interaction/zxzx/zxzx_result.jsp?siteCategoryCode=003001007&styleName=blue&contentId=K6DDTN15LAEBEEOUTINDM64G3SLV1GI9
http://www.sn-n-tax.gov.cn/portal/jsp/portal/interaction/zxzx/zxzx_result.jsp?siteCategoryCode=003001007&styleName=blue&contentId=UTI2EU2JNZE8CH13HT9MN06D8FFR4NF
http://www.sn-n-tax.gov.cn/portal/jsp/portal/interaction/zxzx/zxzx_result.jsp?siteCategoryCode=003001007&styleName=blue&contentId=Q37VEA6ZOS2G5FENMKMJFW85UT77YC2E
http://www.sn-n-tax.gov.cn/portal/jsp/portal/interaction/zxzx/zxzx_result.jsp?siteCategoryCode=003001007&styleName=blue&contentId=9WHNRJAPD2CZF5HHTT0UG76B5T82QTQV
http://www.sn-n-tax.gov.cn/portal/jsp/portal/interaction/zxzx/zxzx_result.jsp?siteCategoryCode=003001007&styleName=blue&contentId=MELRDXQIHOC30OO69XQ8XNSLSB6L6KC8
http://www.sn-n-tax.gov.cn/portal/jsp/portal/interaction/zxzx/zxzx_result.jsp?siteCategoryCode=003001007&styleName=blue&contentId=5B2FFIVIFR2PCOFBG1M8IWH7C0AP1FS3
http://www.sn-n-tax.gov.cn/portal/jsp/portal/interaction/zxzx/zxzx_result.jsp?siteCategoryCode=003001007&styleName=blue&contentId=95ZNCYER222CRF90G0FSKD1VSN1CRT9Z
http://www.sn-n-tax.gov.cn/portal/jsp/portal/interaction/zxzx/zxzx_result.jsp?siteCategoryCode=003001007&styleName=blue&contentId=8KDCN688DOCJDJL72ACTJ80LD8GWGJE0
http://www.sn-n-tax.gov.cn/portal/jsp/portal/interaction/zxzx/zxzx_result.jsp?siteCategoryCode=003001007&styleName=blue&contentId=7FRGH5KJBQ1PATG8PMBT80P6S8VLEO56
http://www.sn-n-tax.gov.cn/portal/jsp/portal/interaction/zxzx/zxzx_result.jsp?siteCategoryCode=003001007&styleName=blue&contentId=L2N2MOPMTE67NU5S9VVIZJHW6JJD6MA3
http://www.sn-n-tax.gov.cn/portal/jsp/portal/interaction/zxzx/zxzx_result.jsp?siteCategoryCode=003001007&styleName=blue&contentId=FDLPYKJENQ49T2EVHNBQNH5OQOG2WQOZ
http://www.sn-n-tax.gov.cn/portal/jsp/portal/interaction/zxzx/zxzx_result.jsp?siteCategoryCode=003001007&styleName=blue&contentId=I9N34WZFWVJVUROG8RZFPC04MBYDY3QL
http://www.sn-n-tax.gov.cn/portal/jsp/portal/interaction/zxzx/zxzx_result.jsp?siteCategoryCode=003001007&styleName=blue&contentId=K2JAO81L7YEJJL3WDVA6JXSE9T2HIIY3
http://www.sn-n-tax.gov.cn/portal/jsp/portal/interaction/zxzx/zxzx_result.jsp?siteCategoryCode=003001007&styleName=blue&contentId=F0RUNZ59LEXTDCXSNP7ZX83AT70Q0GCO
http://www.sn-n-tax.gov.cn/portal/jsp/portal/interaction/zxzx/zxzx_result.jsp?siteCategoryCode=003001007&styleName=blue&contentId=F1HVDNNQGOFNLQER6T0MIB0GU40YJQX9
http://www.sn-n-tax.gov.cn/portal/jsp/portal/interaction/zxzx/zxzx_result.jsp?siteCategoryCode=003001007&styleName=blue&contentId=18DD7NLLMRPMT8X0G7YVZC3H5XLY8VGK
http://www.sn-n-tax.gov.cn/portal/jsp/portal/interaction/zxzx/zxzx_result.jsp?siteCategoryCode=003001007&styleName=blue&contentId=I37MHEBTSG3JX39N88MAYB4CAALA10CY
http://www.sn-n-tax.gov.cn/portal/jsp/portal/interaction/zxzx/zxzx_result.jsp?siteCategoryCode=003001007&styleName=blue&contentId=MAIWNOWXBL7INGDFBN8TFMBSU59JTG08
http://www.sn-n-tax.gov.cn/portal/jsp/portal/interaction/zxzx/zxzx_result.jsp?siteCategoryCode=003001007&styleName=blue&contentId=Q636TCPOO9A0M0NS1MYOPQ0PB5OLS7N1
http://www.sn-n-tax.gov.cn/portal/jsp/portal/interaction/zxzx/zxzx_result.jsp?siteCategoryCode=003001007&styleName=blue&contentId=NPXZNJG6CG9FT3IEKLN4RBKAS3KDNFWL
http://www.sn-n-tax.gov.cn/portal/jsp/portal/interaction/zxzx/zxzx_result.jsp?siteCategoryCode=003001007&styleName=blue&contentId=LR6ZVHYVBGVHCB2P09AAVKBM54I1EFEN
http://www.sn-n-tax.gov.cn/portal/jsp/portal/interaction/zxzx/zxzx_result.jsp?siteCategoryCode=003001007&styleName=blue&contentId=36FHJN6KKAHWBAGG81HOABHY6SFHA1T6
http://www.sn-n-tax.gov.cn/portal/jsp/portal/interaction/zxzx/zxzx_result.jsp?siteCategoryCode=003001007&styleName=blue&contentId=3574932BF760ZQ1KBOM1KAV2BRE3F56Q
http://www.sn-n-tax.gov.cn/portal/jsp/portal/interaction/zxzx/zxzx_result.jsp?siteCategoryCode=003001007&styleName=blue&contentId=JPQSCI0VK6LQY51AM0M1MSA7TXFX18N6
http://www.sn-n-tax.gov.cn/portal/jsp/portal/interaction/zxzx/zxzx_result.jsp?siteCategoryCode=003001007&styleName=blue&contentId=C197TIOFP73Z99NMYIMLMQZ5G824MV1D
http://www.sn-n-tax.gov.cn/portal/jsp/portal/interaction/zxzx/zxzx_result.jsp?siteCategoryCode=003001007&styleName=blue&contentId=KN2UOHX5QW9MIH1SJAE5J9C8W8H4U6LN
http://www.sn-n-tax.gov.cn/portal/jsp/portal/interaction/zxzx/zxzx_result.jsp?siteCategoryCode=003001007&styleName=blue&contentId=OQPRUOR2OGB81R26DER7IDFT0T9STQV1
http://www.sn-n-tax.gov.cn/portal/jsp/portal/interaction/zxzx/zxzx_result.jsp?siteCategoryCode=003001007&styleName=blue&contentId=2QGLC2U3LJ256FQ2HKH6BCJYJ24YBHTR
http://www.sn-n-tax.gov.cn/portal/jsp/portal/interaction/zxzx/zxzx_result.jsp?siteCategoryCode=003001007&styleName=blue&contentId=7MHZ8PKX3J1A2F5FGYRH7NMEMDWP7G0X
http://www.sn-n-tax.gov.cn/portal/jsp/portal/interaction/zxzx/zxzx_result.jsp?siteCategoryCode=003001007&styleName=blue&contentId=1YB4MLTSAVWT4J9BW1DM3TFT03Y7EHDF
http://www.sn-n-tax.gov.cn/portal/jsp/portal/interaction/zxzx/zxzx_result.jsp?siteCategoryCode=003001007&styleName=blue&contentId=7DUVTEAMI8N79JW7TWLF2SYVVYXDNBFQ
http://www.sn-n-tax.gov.cn/portal/jsp/portal/interaction/zxzx/zxzx_result.jsp?siteCategoryCode=003001007&styleName=blue&contentId=PJEX6IIPQGNFIQJ4PN8EL86H0J5UKSFS
http://www.sn-n-tax.gov.cn/portal/jsp/portal/interaction/zxzx/zxzx_result.jsp?siteCategoryCode=003001007&styleName=blue&contentId=6SXAPLAOEA6C525R1D58IT6QUX63PCAD
http://www.sn-n-tax.gov.cn/portal/jsp/portal/interaction/zxzx/zxzx_result.jsp?siteCategoryCode=003001007&styleName=blue&contentId=H8TIVC5796QN0GDHVYD85Q7L4I5DVVY4
http://www.sn-n-tax.gov.cn/portal/jsp/portal/interaction/zxzx/zxzx_result.jsp?siteCategoryCode=003001007&styleName=blue&contentId=8D1ATR14PU31426Q3UWGVVXBR753R3CY
http://www.sn-n-tax.gov.cn/portal/jsp/portal/interaction/zxzx/zxzx_result.jsp?siteCategoryCode=003001007&styleName=blue&contentId=DKAIUZCZ2JRPGIS8DT9ITC40UJGD9K8P
http://www.sn-n-tax.gov.cn/portal/jsp/portal/interaction/zxzx/zxzx_result.jsp?siteCategoryCode=003001007&styleName=blue&contentId=BE0RZ94F51SICB00TCKBRS8AIP2PHCY7
http://www.sn-n-tax.gov.cn/portal/jsp/portal/interaction/zxzx/zxzx_result.jsp?siteCategoryCode=003001007&styleName=blue&contentId=BRTTPMT5MJUB1VOQ5F8AHOLJ5PA0D8N0
http://www.sn-n-tax.gov.cn/portal/jsp/portal/interaction/zxzx/zxzx_result.jsp?siteCategoryCode=003001007&styleName=blue&contentId=248ZA26FC2OS72M524W8BKC1A3U48J6
http://www.sn-n-tax.gov.cn/portal/jsp/portal/interaction/zxzx/zxzx_result.jsp?siteCategoryCode=003001007&styleName=blue&contentId=F6X977DXGBDBNS9GTE4RAXMALHDZSGZ6
http://www.sn-n-tax.gov.cn/portal/jsp/portal/interaction/zxzx/zxzx_result.jsp?siteCategoryCode=003001007&styleName=blue&contentId=QI7JV1PPJKRQ0TO9EPJ64UEJT7XY9KUI
http://www.sn-n-tax.gov.cn/portal/jsp/portal/interaction/zxzx/zxzx_result.jsp?siteCategoryCode=003001007&styleName=blue&contentId=MAIQCRFXC7H64ZRL91ZP5L8TI667P1HT
http://www.sn-n-tax.gov.cn/portal/jsp/portal/interaction/zxzx/zxzx_result.jsp?siteCategoryCode=003001007&styleName=blue&contentId=3VTNMSG29ZDO0GN2HWV7AAA10X3JDSWR
http://www.sn-n-tax.gov.cn/portal/jsp/portal/interaction/zxzx/zxzx_result.jsp?siteCategoryCode=003001007&styleName=blue&contentId=F5BKV5N5AH18UFOT3PE7A7LJ2XG6Q5FR
http://www.sn-n-tax.gov.cn/portal/jsp/portal/interaction/zxzx/zxzx_result.jsp?siteCategoryCode=003001007&styleName=blue&contentId=KB40MI0XEEXH6ICCE0MEE6MTGEV0I394
http://www.sn-n-tax.gov.cn/portal/jsp/portal/interaction/zxzx/zxzx_result.jsp?siteCategoryCode=003001007&styleName=blue&contentId=ACUHXYDNC5YNU3BNAC7Y745OKXNNUIZ6
http://www.sn-n-tax.gov.cn/portal/jsp/portal/interaction/zxzx/zxzx_result.jsp?siteCategoryCode=003001007&styleName=blue&contentId=BP41AOXZD2X5874BH1C2X68XPNRL7MMO
http://www.sn-n-tax.gov.cn/portal/jsp/portal/interaction/zxzx/zxzx_result.jsp?siteCategoryCode=003001007&styleName=blue&contentId=7S92C71S8QHQQSPKMS71RWL7AMZPNTKE
http://www.sn-n-tax.gov.cn/portal/jsp/portal/interaction/zxzx/zxzx_result.jsp?siteCategoryCode=003001007&styleName=blue&contentId=1XIOYTV2YHF1C3TE5Y3LI9DLTQAG2X7W
http://www.sn-n-tax.gov.cn/portal/jsp/portal/interaction/zxzx/zxzx_result.jsp?siteCategoryCode=003001007&styleName=blue&contentId=Q3OQMK57VB87YSZGVITKGTAL0VZ52AXE
http://www.sn-n-tax.gov.cn/portal/jsp/portal/interaction/zxzx/zxzx_result.jsp?siteCategoryCode=003001007&styleName=blue&contentId=49RD5YCVYRAK351CMC0JVPG9SUA8DCGD
http://www.sn-n-tax.gov.cn/portal/jsp/portal/interaction/zxzx/zxzx_result.jsp?siteCategoryCode=003001007&styleName=blue&contentId=7HXVFITHLH4YL9LF4NDP9ODOTPLQJ5PU
http://www.sn-n-tax.gov.cn/portal/jsp/portal/interaction/zxzx/zxzx_result.jsp?siteCategoryCode=003001007&styleName=blue&contentId=4PMBCDTOUR1CCMX9BMCFHO2D65FMVZO
http://www.sn-n-tax.gov.cn/portal/jsp/portal/interaction/zxzx/zxzx_result.jsp?siteCategoryCode=003001007&styleName=blue&contentId=1KWJZATLBZ0J2LXFV7P16MZNB3MBQ99V
http://www.sn-n-tax.gov.cn/portal/jsp/portal/interaction/zxzx/zxzx_result.jsp?siteCategoryCode=003001007&styleName=blue&contentId=8H1SL9EX4EMMNS4TNDYLU3RFFZTKEUZ
http://www.sn-n-tax.gov.cn/portal/jsp/portal/interaction/zxzx/zxzx_result.jsp?siteCategoryCode=003001007&styleName=blue&contentId=7GQL3ZQRI77O6925PS5YOPS7C936ASLQ
http://www.sn-n-tax.gov.cn/portal/jsp/portal/interaction/zxzx/zxzx_result.jsp?siteCategoryCode=003001007&styleName=blue&contentId=1CJPOE8KNHNE25TPPF2M83HFC2WLQKEQ
http://www.sn-n-tax.gov.cn/portal/jsp/portal/interaction/zxzx/zxzx_result.jsp?siteCategoryCode=003001007&styleName=blue&contentId=MAS9WUULUL99DON6WU9T6JGWQ5Z9WIC9
http://www.sn-n-tax.gov.cn/portal/jsp/portal/interaction/zxzx/zxzx_result.jsp?siteCategoryCode=003001007&styleName=blue&contentId=FAMTZ3NLURMZQRZ1EA1J68EM0E0I03HG
http://www.sn-n-tax.gov.cn/portal/jsp/portal/interaction/zxzx/zxzx_result.jsp?siteCategoryCode=003001007&styleName=blue&contentId=KVW87G9Z7VSVSWXUO1AFOSYG3NT6NFLN
http://www.sn-n-tax.gov.cn/portal/jsp/portal/interaction/zxzx/zxzx_result.jsp?siteCategoryCode=003001007&styleName=blue&contentId=D1CPZTMD6TTAB3G9MF52X2WA5BFM31L2
http://www.sn-n-tax.gov.cn/portal/jsp/portal/interaction/zxzx/zxzx_result.jsp?siteCategoryCode=003001007&styleName=blue&contentId=20SJ07IJ1F6E833M1MA9NG8SXBLLTU9I
http://www.sn-n-tax.gov.cn/portal/jsp/portal/interaction/zxzx/zxzx_result.jsp?siteCategoryCode=003001007&styleName=blue&contentId=AB1V5CDM2API78NO5LNVZNIGHSCET93
http://www.sn-n-tax.gov.cn/portal/jsp/portal/interaction/zxzx/zxzx_result.jsp?siteCategoryCode=003001007&styleName=blue&contentId=EQ4ZT47PXGPLFVRCKHEER9QOCNMZZ8I2
http://www.sn-n-tax.gov.cn/portal/jsp/portal/interaction/zxzx/zxzx_result.jsp?siteCategoryCode=003001007&styleName=blue&contentId=OH589U88NOZYVLY3H5JA1AHAWM66Z9H0
http://www.sn-n-tax.gov.cn/portal/jsp/portal/interaction/zxzx/zxzx_result.jsp?siteCategoryCode=003001007&styleName=blue&contentId=2L42OPRKMR309Z3HNNNEKA9IG5HEMX7W
http://www.sn-n-tax.gov.cn/portal/jsp/portal/interaction/zxzx/zxzx_result.jsp?siteCategoryCode=003001007&styleName=blue&contentId=3O1VF1DDRM0Y1BBN67K0FBDX9OLRI9KK
http://www.sn-n-tax.gov.cn/portal/jsp/portal/interaction/zxzx/zxzx_result.jsp?siteCategoryCode=003001007&styleName=blue&contentId=C22PRGEM4DXT7BYQPNPE1PWXEKRQPV18
http://www.sn-n-tax.gov.cn/portal/jsp/portal/interaction/zxzx/zxzx_result.jsp?siteCategoryCode=003001007&styleName=blue&contentId=1MD2OJZBLZK6KFL1E89RF4U886OEJKK
http://www.sn-n-tax.gov.cn/portal/jsp/portal/interaction/zxzx/zxzx_result.jsp?siteCategoryCode=003001007&styleName=blue&contentId=9M22CLU3TP3FQM36HBIMOLU3CO8NK1Y6
http://www.sn-n-tax.gov.cn/portal/jsp/portal/interaction/zxzx/zxzx_result.jsp?siteCategoryCode=003001007&styleName=blue&contentId=NUBXHM6UKTIDK15ZHZ7TFQSO26WQ8JDN
http://www.sn-n-tax.gov.cn/portal/jsp/portal/interaction/zxzx/zxzx_result.jsp?siteCategoryCode=003001007&styleName=blue&contentId=I56B9H7E2K8AVK5P6FC861O0Z1NOQ6Z5
http://www.sn-n-tax.gov.cn/portal/jsp/portal/interaction/zxzx/zxzx_result.jsp?siteCategoryCode=003001007&styleName=blue&contentId=HREVDCU9NCEH0A82TPRHF0K5EME09WFL
http://www.sn-n-tax.gov.cn/portal/jsp/portal/interaction/zxzx/zxzx_result.jsp?siteCategoryCode=003001007&styleName=blue&contentId=N2KC9XUIL0L16R8DBOYHT2E2WGOFZVAV
http://www.sn-n-tax.gov.cn/portal/jsp/portal/interaction/zxzx/zxzx_result.jsp?siteCategoryCode=003001007&styleName=blue&contentId=L59J8L50W942SZV7I578T99H526IWYGX
http://www.sn-n-tax.gov.cn/portal/jsp/portal/interaction/zxzx/zxzx_result.jsp?siteCategoryCode=003001007&styleName=blue&contentId=FHK4JW9LY1H4Z7ZWT9MZHFH9RZCAJE2B
"""

for i in urls.split():
    get_detail(i)
    time.sleep(random.randint(3,7))

save("oldtax.csv")