import bs4 as bs
import requests  # python的http客户端
import pickle  # 用于序列化反序列化
import datetime as dt
import pandas as pd
import pandas_datareader.data as web
from matplotlib import style
import matplotlib.pyplot as plt
import os


# def GetHuStock():
# res = requests.get('https://www.banban.cn/gupiao/list_sh.html')
# #防止中文乱码
# res.encoding = res.apparent_encoding
# #使用bsoup的lxml样式
# soup = bs.BeautifulSoup(res.text,'lxml')
# #从html内容中找到类名为'u-postcontent cz'的div标签
# content = soup.find('div',{'class':'u-postcontent cz'})
# result= []
#
# for item in content.findAll('a'):
#     result.append(item.text)
# with open('huStock.pickle','wb') as f:
#     pickle.dump(result,f)


def GetStockFromYahoo(isHaveStockCode=False):
    if not isHaveStockCode:
         data = pd.read_csv('stock.csv')
        
    if not os.path.exists('StockDir'):
        os.makedirs('StockDir')

    for i in range(194,289):

        stock_name = data.iloc[i,0]
        if stock_name[0]=='*':
            stock_name = stock_name[1:]
        stock_code = data.iloc[i,3][1:]
        if stock_code[0] == '6' or stock_code[0]== '9':
            stock_code = stock_code + '.ss'
        else:
            stock_code = stock_code + '.sz'
        if os.path.exists('StockDir/{}.csv'.format(stock_name + stock_code)):
            print('已下载'+stock_name)
        else:
            DownloadStock(stock_name, stock_code)
            print('下载{}中...'.format(stock_name))


def DownloadStock(stockName, stockCode):
    style.use('ggplot')
    start = dt.datetime(2019, 1, 1)
    end = dt.datetime(2020, 5, 1)
    # 根据股票代码从雅虎财经读取该股票在制定时间段的股票数据
    df = web.DataReader(stockCode, 'yahoo', start, end)
    # 保存为对应的文件
    df.to_csv('StockDir/{}.csv'.format(stockName + stockCode))


GetStockFromYahoo()
