# usr/bin/python
# File: gaode.py
# Author: Krissy
# Description: 利用高德查询985大学的经纬度信息


import requests
import json
from tqdm import tqdm

KEY = "xxx"   # 请输入个人的 高德地图的 API Key
GD_URL = "https://restapi.amap.com/v3/geocode/geo?address=%s&key=%s"
SUCCESS_FLAG = "1"

def get_lon_and_lat_by_address(address):
    gd_url = GD_URL % (address, KEY)
    # 发起 GET 请求
    response = requests.get(gd_url)
    query_result = response.text
    obj = json.loads(query_result)
    if str(obj.get("status")) == SUCCESS_FLAG:
        location = obj.get("geocodes")[0].get("location")
        return location
    else:
        raise RuntimeError("地址转换经纬度失败，错误码：" + str(obj.get("infocode")))

if __name__ == "__main__":
    with open('../addresses.txt', 'r', encoding='utf-8') as fp:
        uni_loc_info = {'university':[], 'lat':[], 'long':[]}
        for line in tqdm(fp.readlines()):
            line = line.strip().split('\t')
            uni, loc = line[0], line[1]
            try:
                coordinates = get_lon_and_lat_by_address(loc)
                coord_lat, coord_long = coordinates.split(',')
                print(uni, ' ', coord_lat, ', ', coord_long)
                uni_loc_info['university'].append(uni)
                uni_loc_info['lat'].append(coord_lat)
                uni_loc_info['long'].append(coord_long)
            except Exception:
                print(uni, ' ', loc, '查询失败！')
                continue

        import pandas as pd
        df = pd.DataFrame(uni_loc_info)
        print(df)
        df.to_csv('university_address.csv')
# 成功查询32个  查询失败7个~

    # address = "江苏省南京市南京大学"
    # location = get_lon_and_lat_by_address(address)
    # print("经纬度：" + location)
