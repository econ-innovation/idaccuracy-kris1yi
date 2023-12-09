# usr/bin/python
# File: google.py
# Author: Krissy
# Description: 谷歌专利数据拆解
# 从google专利⽂件中拆分出专利的filling date|publication date|grant date|priority date，并将拆分过程写成针对⽂件的函数，从命令⾏直接运⾏，参数为⽂件名（google100.txt）
# Data location: data/google.json
# 本问题只需要在命令行输入  python .\extract_dates.py --target_file google100.txt  即可，
## 如果增加参数需要修改传入文件的话： 在命令行输入  python .\extract_dates.py --target_file google100.txt --load_file data/google.json 即可，

import json
from tqdm import tqdm
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--target_file', type=str, default='', help='Target txt file to be write.')
# parser.add_argument('--load_file', type=str, default='', help='load json file to be loaded.')
args = parser.parse_args()


# 读取 JSON 文件
file_name = 'data/google.json'  # 替换为你的文件路径
# file_name = args.load_file
data = json.load(open(file_name, 'r', encoding='utf-8'))

# print(data.keys())

# 提取所需的日期和申请号
publication_date = data.get('publication_date')
filing_date = data.get('filing_date')
grant_date = data.get('grant_date')
priority_date = data.get('priority_date')
application_numbers = data.get('application_number')  # 获取所有的申请号


with open(args.target_file, 'w', encoding='utf-8') as fw:
    fw.write('\t'.join(['application_number', 'publication_date', 'filing_date', 'grant_date', 'priority_date']))
    fw.write('\n')
    fw.write('\t'.join([application_numbers, publication_date, filing_date, grant_date, priority_date]))






























