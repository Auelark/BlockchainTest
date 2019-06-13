import urllib.request
import json


def get_page(data_length):
      url = 'https://api.alternative.me/fng/?limit='
      res = urllib.request.urlopen(url=url+data_length)
      data10 = res.read().decode('utf-8')
      data2 = json.loads(data10)
      print("输出数据", data2)


data_length = input("输入天数：");
get_page(data_length)

