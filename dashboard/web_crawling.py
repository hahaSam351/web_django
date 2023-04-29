import requests
from bs4 import BeautifulSoup
import random
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import os


def web_crawling(data) :
    url = 'https://zzsza.github.io/data/2019/02/06/prophet/'
    req = requests.get(url)

    if req.ok : 
        html = req.text
        soup = BeautifulSoup(html, 'html.parser')
        soup = BeautifulSoup(html, 'html.parser')
        contents = soup.text.split()[:100]

    titles = ['title_' + str(random.randint(1, 100)) for i in range(100)]
    points = [random.randint(1, 100) for i in range(100)]


    for i in range(len(contents)) :   
        content = contents[i]
        title = titles[i]
        point = points[i]    
        data.append((title, point, content)) #튜플이 여러 개인 리스트 생성
        print(title, point, content)


def make_chart() :
    df = pd.read_csv('data_time.csv', index_col=0)
    data = df[df['farm']==900300]
    plt.figure(figsize=(20,5))
    plt.plot(data['year_month'], data['count'])
    path = os.path.join('./dashboard/images/fig01.png')
    print(path)                       
    plt.savefig(path, dpi=300)