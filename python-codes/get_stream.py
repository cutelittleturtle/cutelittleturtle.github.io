#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import codecs
import re
import sys
import os
import shutil

import requests
from bs4 import BeautifulSoup
from datetime import datetime

def remove_nbws(text):
    """ remove unwanted unicode punctuation: zwsp, nbws, \t, \r, \r.
    """

    # ZWSP: Zero width space
    text = text.replace(u'\u200B', '')
    # NBWS: Non-breaking space
    text = text.replace(u'\xa0', ' ')
    # HalfWidth fullstop
    text = text.replace(u'\uff61', '')
    # Bullet
    text = text.replace(u'\u2022', '')
    # White space
    text = text.replace(u'\t', ' ').replace(u'\r', ' ')

    # General Punctuation
    gpc_pattern = re.compile(r'[\u2000-\u206F]')
    text = gpc_pattern.sub('', text)

    # Mathematical Operator
    mop_pattern = re.compile(r'[\u2200-\u22FF]')
    text = mop_pattern.sub('', text)

    # Combining Diacritical Marks
    dcm_pattern = re.compile(r'[\u0300-\u036F]')
    text = dcm_pattern.sub('', text)

    lsp_pattern = re.compile(r'[\x80-\xFF]')
    text = lsp_pattern.sub('', text)

    text = re.sub(r'\s+', ' ', text)

    return text

def date_extractor(arbString):
    if  re.search(r'\d*年\d*月\d*日',arbString):
        date = re.search(r'\d*年\d*月\d*日',arbString).group(0)
        Y = re.search(r'\d*年',date).group(0)[:-1]
        m = re.search(r'年\d*月',date).group(0)[1:-1]
        d =  re.search(r'月\d*日',date).group(0)[1:-1]
        if len(Y) == 2:
            Y = '20' + Y
        if len(m) == 1:
            m = '0' + m
        if len(d) == 1:
            d = '0' + d
        date = Y + '-' + m + '-' + d
    elif re.search(r'\d{6}',arbString):
        date = re.search(r'\d{6}',arbString).group(0)
        date = '20' + date[:2] + '-' + date[2:4] + '-' + date[4:6]
    else:
        date = "" # last resolve

    return date

def get_new_stream(sourcedate):

    API='https://space.bilibili.com/ajax/member/getSubmitVideos?mid=37694382&pagesize=30&tid=0&page=1&keyword=&order=pubdate'

    r = requests.get(API)
    json_content = r.json()

    vlist = json_content['data']['vlist']

    new_addition = []

    for video in vlist:
        title = remove_nbws(video['title'])
        aid = int(video['aid'])
        url = "https://www.bilibili.com/video/av" + str(aid)

        if "直播" in title and "口袋48" in title:
            date = date_extractor(title)
            if not date:
                r = requests.get(url)
                soup = BeautifulSoup(r.content, 'lxml')
                date = soup.find('meta', {'itemprop':'uploadDate'})['content']
                date = date[:4] + '-' + date[5:7] + '-' + date[8:10]

            title = (title.replace('【SNH48】', '').replace('TeamX', '').strip() + ' (' + date + ')')
            if datetime.strptime(date, '%Y-%m-%d') > datetime.strptime(sourcedate, '%Y-%m-%d'):
                new_addition.append({'title':title, 'url':url, 'aid':aid})

    return new_addition

def update_stream_archive():
    print("更新直播")
    sourcefolder = os.path.abspath(os.path.join(os.getcwd(), "..")) + os.path.sep + "文章" + os.path.sep + "补档模块" + os.path.sep
    sourcefile = sourcefolder + "直播.txt"
    sourcestring = ""
    sourcedate = datetime.now().strftime('%Y-%m-%d')

    try:
        with codecs.open(sourcefile, 'r', encoding='utf-8') as f:
            lineno = 1
            for line in f:
                if codecs.BOM_UTF8.decode('utf-8') in line:
                    line = line.replace(codecs.BOM_UTF8.decode('utf-8'),"")
                if lineno == 3:
                    sourcedate = re.search(r'\d{4}-\d{2}-\d{2}', line).group(0)
                if lineno>2:
                    sourcestring += line

                lineno+=1
    except Exception as e:
        print(e)

    new_stream_items = get_new_stream(sourcedate)
    if new_stream_items:
        print("共更新%d条信息" % len(new_stream_items))
        with codecs.open(sourcefolder + "temp.txt",'w',encoding='utf-8') as f:
            result = '直播' + os.linesep + os.linesep
            for video in new_stream_items:
               result = result + video['title'] + os.linesep + video['url'] + os.linesep + os.linesep

            result = result + sourcestring
            f.write(result)

        try:
            shutil.copy2(sourcefolder + 'temp.txt', sourcefolder + '直播.txt')
            os.remove(sourcefolder + 'temp.txt')
        except Exception as e:
            print(e)
    else:
        print("没有新信息")