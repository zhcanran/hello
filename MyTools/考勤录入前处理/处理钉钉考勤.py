# coding=utf-8
import pandas as pd
import time
from datetime import datetime
import re


def data_pro(path, name_num, Ldap=None, group='开发一部', company=None):
    # 读取数据来源
    data = pd.read_excel(path)
    # 获取年，月份
    year = int(re.findall('统计日期：(.*?)-', list(data)[0])[0])
    month = int(re.findall('2022-(.*?)-', list(data)[0])[0])
    # 获取个人数据
    data = data.iloc[name_num - 2].tolist()
    name, data = data[0], data[6:]  # 名字和考勤数据

    # 清洗数据
    for _, i in enumerate(data):
        if isinstance(i, float):
            continue
        data[_] = i.replace('外勤', '').split('\n')
    # 整理数据
    list1 = []
    for _, i in enumerate(data):
        dict1 = dict()
        t = datetime(year, month, _ + 1)
        dict1['date'] = time.strftime('%Y-%m-%d', t.timetuple())
        if isinstance(i, float):
            dict1['start'] = i
            dict1['end'] = i
            list1.append(dict1)
        else:
            dict1['start'] = i[0] + ':00'
            dict1['end'] = i[-1] + ':00'
            list1.append(dict1)

    # 写入数据
    dates, starts, ends = [], [], []
    for i in range(len(list1)):
        dates.append(list1[i]['date'])
        starts.append(list1[i]['start'])
        ends.append(list1[i]['end'])
    # 清理无效数据
    remove = [indx for indx, i in enumerate(starts) if isinstance(i, float) and isinstance(ends[indx], float)]
    dates = [i for indx, i in enumerate(dates) if indx not in remove]
    starts = [i for indx, i in enumerate(starts) if indx not in remove]
    ends = [i for indx, i in enumerate(ends) if indx not in remove]

    df_data = {
        'Ldap账号': Ldap,
        '姓名': name,
        '部门': group,
        '公司': company,
        '考勤日期': dates,
        '签到时间': starts,
        '签退时间': ends}
    df = pd.DataFrame(df_data)
    print(df)
    path = f"考勤导入{month}月-{name}.xlsx"
    df.to_excel(path, index=False)


if __name__ == '__main__':
    path = r'中汇开发一部_打卡时间表_20220701-20220731(1).xlsx'
    while True:
        name_no=int(input("请输入姓名所在行号："))
        data_pro(path, name_no)
        yes_no=input("是否继续（y/n）")
        if yes_no=="n":
            break
