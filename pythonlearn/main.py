"""

学生：张宜
时间：2023-12-08
来源：史东波老师第四讲课 python基础

"""
tup1 = (1,23,4,'a')
tup2 = ("x","y")
tup = tup1 + tup2
tup[0:3]


import json
with open("../data/assignment_google/google100.txt","r") as f:
    for pt in f.readlines():
        patent = json.loads(pt)
        if len(patent["ipc"]) > 0:
            for ipc in patent["ipc"]:
                with open('../data/assignment_google/ipc.txt', 'a') as fs:
                    fs.write("{1}{0}{2}\n".format("|",
                                                  patent["application_number"],ipc["code"]))# 申请号 | IPC分类号 的形式呈现


import requests
from bs4 import BeautifulSoup
# 发送 GET 请求
url = 'https://patents.google.com/patent/CN114409796A'
response = requests.get(url)
# 检查请求是否成功
if response.status_code == 200:
    # 使用 response.encoding 来确定正确的编码方式
    response.encoding = response.apparent_encoding
    # 使用BeautifulSoup解析HTML内容
    soup = BeautifulSoup(response.text, 'html.parser')
    # 这里可以使用BeautifulSoup的功能来提取所需的信息
    # 例如，获取标题
    title = soup.find('title')
    print("标题：", title.text)
    # 获取特定元素
    # 这里是获取专利文本内容，你可以通过查看网页源代码找到对应元素的class或id
    patent_content = soup.find('div', class_='abstract')
    print("专利内容：", patent_content.text)
else:
    print("请求失败，状态码：", response.status_code)





import requests
import xml.etree.ElementTree as ET # 或者使用 lxml 库更高效
import pandas as pd

location = "南京大学"
key = "79c02e71e2b5c407b83afff7c12afe04"
url = f'https://restapi.amap.com/v3/geocode/geo?address={location}&output=XML&key={key}'
response = requests.get(url)
response_text = response.text
# 解析 XML 数据
root = ET.fromstring(response_text)
# 创建一个空的DataFrame来存储数据
data = []
# 遍历XML并提取数据
for geocode in root.findall('.//geocode'):  # 这里的路径根据实际 XML 结构来定
    ida = geocode.findtext('ida')
    countrycode = geocode.findtext('countrycode')
    postcode = geocode.findtext('postcode')
    address = geocode.findtext('address')
    country = geocode.findtext('country')
    province = geocode.findtext('province')
    city = geocode.findtext('city')
    citycode = geocode.findtext('citycode')
    district = geocode.findtext('district')
    street = geocode.findtext('street')
    number = geocode.findtext('number')
    adcode = geocode.findtext('adcode')
    longitude = geocode.findtext('longitude')
    latitude = geocode.findtext('latitude')
    level = geocode.findtext('level')
    formatted_address = geocode.findtext('formattedaddress')

    # 将提取的数据添加到列表中
    data.append({
        'Ida': ida,
        'CountryCode': countrycode,
        'Postcode': postcode,
        'Address': address,
        'Country': country,
        'Province': province,
        'City': city,
        'CityCode': citycode,
        'District': district,
        'Street': street,
        'Number': number,
        'Adcode': adcode,
        'Longitude': longitude,
        'Latitude': latitude,
        'Level': level,
        'Formatted_Address': formatted_address
    })

# 将列表转换为DataFrame
df = pd.DataFrame(data)

# 显示DataFrame
print(df)



# 学校信息
schools = [
    ("清华大学", "北京市", "海淀区"),
    ("北京大学", "北京市", "海淀区"),
    ("中国人民大学", "北京市", "海淀区"),
    ("北京理工大学", "北京市", "海淀区"),
    ("北京航空航天大学", "北京市", "海淀区"),
    ("中央民族大学", "北京市", "海淀区"),
    ("北京师范大学", "北京市", "海淀区"),
    ("中国农业大学", "北京市", "海淀区"),
    ("天津大学", "天津市", "南开区"),
    ("南开大学", "天津市", "南开区"),
    ("复旦大学", "上海市", "杨浦区"),
    ("上海交通大学", "上海市", "闵行区"),
    ("同济大学", "上海市", "杨浦区"),
    ("华东师范大学", "上海市", "闵行区"),
    ("重庆大学", "重庆市", "沙坪坝区"),
    ("四川大学", "四川省", "成都市"),
    ("电子科技大学", "四川省", "成都市"),
    ("湖南大学", "湖南省", "长沙市"),
    ("国防科技大学", "湖南省", "长沙市"),
    ("中南大学", "湖南省", "长沙市"),
    ("厦门大学", "福建省", "厦门市"),
    ("中国科技技术大学", "安徽省", "合肥市"),
    ("南京大学", "江苏省", "南京市"),
    ("东南大学", "江苏省", "南京市"),
    ("哈尔滨工业大学", "黑龙江省", "哈尔滨市"),
    ("浙江大学", "浙江省", "杭州市"),
    ("西安交通大学", "陕西省", "西安市"),
    ("西北农林科技大学", "陕西省", "咸阳市"),
    ("西北工业大学", "陕西省", "西安市"),
    ("华中科技大学", "湖北省", "武汉市"),
    ("武汉大学", "湖北省", "武汉市"),
    ("中国海洋大学", "山东省", "青岛市"),
    ("山东大学", "山东省", "济南市"),
    ("吉林大学", "吉林省", "长春市"),
    ("大连理工大学", "辽宁省", "大连市"),
    ("东北大学", "辽宁省", "沈阳市"),
    ("华南理工大学", "广东省", "广州市"),
    ("中山大学", "广东省", "广州市"),
    ("兰州大学", "甘肃省", "兰州市")
]

with open('addresses.txt', 'w', encoding='utf-8') as fp:
    for ele in schools:
        add = ele[1] + ele[2] + ele[0]
        fp.write(ele[0] + '\t' + add + '\n')













