#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ref:https://github.com/omengye/spider

import urllib.request
import re
import bs4
import os

headers = ('User-Agent', 'Mozilla/5.0 (Windows NT 6.3; WOW64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.154 Safari/537.36')
path = os.getcwd()                  # 获取当前工作目录
path = os.path.join(path, 'pic')    # 在当前工作目录下添加/pic/
if not os.path.exists(path):        # 如果./pic/不存在
    os.mkdir(path)                  # 豆瓣禁止图片外链，将图片保存至pic文件夹

def get_sort_films(url):
    opener = urllib.request.build_opener()
    opener.add_handler = headers
    content = opener.open(url).read()
    soup = bs4.BeautifulSoup(content)

    now_playing_film = soup.find('div', {'id': 'nowplaying'})               # 获取正在上映电影
    list_content = now_playing_film.findAll('li', {'class': 'list-item'})   # 获取电影列表

    all_film_content = []   # 将所有电影内容结果放在这个数组

    for list_film in list_content:
        film_content={}
        if (list_film.ul.li['class'] == ['poster']):
            film_content['film_name']       =    list_film.ul.li.img['alt']         # 电影名字
            film_content['film_release']    =    list_film['data-release'] + '年'   # 上映年份 
            film_content['film_actors']     =    list_film['data-actors']           # 主演
            film_content['film_director']   =    list_film['data-director']         # 导演
            film_content['film_href']       =    list_film.ul.li.a['href']          # 链接
            film_content['film_src']        =    list_film.ul.li.a.img['src']       # 图片链接
            pic_name = path + os.sep + film_content['film_name'] + '.gif'      # 创建图片的下载路径
            urllib.request.urlretrieve(film_content['film_src'], pic_name)     # 下载图片
            film_content['film_pic'] = film_content['film_name'] + '.gif'      # 图片名
            if list_film.find('span', {'class', 'subject-rate'}):
                film_content['points'] = list_film.find('span', {'class', 'subject-rate'}).string.strip()
                film_content['film_points'] = film_content['points'] + '分'
            else:
                film_content['points'] = '0'
                film_content['film_points'] = '暂无评分'

            stars = list_film.find('li', {'class' : 'srating'}).span['class']

            if stars[0] != 'rating-star':
                film_content['film_stars'] = '评论人数不足'
            else:
                original_film_stars = stars[1]
                re_film_stars = re.compile(r'^\D*(\d{2})$')    # 用正则提取星数
                film_content['film_stars'] = str(int(re_film_stars.search(original_film_stars).groups()[0])/10) + '颗星'
        all_film_content.append(film_content)

    sort_all_film = sorted(all_film_content, key = lambda x:x['points'], reverse = True)   # 将列表中的字典元素按照分数从大到小排列

    return sort_all_film   # 返回根据评分排序的电影内容，评分从高到低

url = 'http://movie.douban.com/nowplaying/beijing'   # 该爬虫只对此网站有效，不具有可移植性
msg = get_sort_films(url)
print(msg)
