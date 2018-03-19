# coding:utf-8

import urllib.request

import re

# key = '修身'
# keyname = urllib.request.quote(key)
header = ('user-agent',
          'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36')

openner = urllib.request.build_opener()
openner.addheaders = [header]
urllib.request.install_opener(openner)
j = 1
for i in range(0, 10):
    try:
        url = 'http://www.58pic.com/tupian/xingganmeinv-0-0-'+str(i)+'.html'
        data = urllib.request.urlopen(url).read().decode('gbk', 'ignore')
        print(data)
        pattern = 'data-original="(.*?).jpg'
        imagelink = re.compile(pattern).findall(data)
        print(imagelink)

        for link in imagelink:
            urllib.request.urlretrieve(link+'.jpg',
                                       'F:/编程语言/python/33.Python数据分析与挖掘实战视频教程/qiantuimage/' + str(j) + '.jpg')
            j += 1

    except urllib.error.URLError as e:
        if hasattr(e,'code'):
            print(e.code)
        if hasattr(e,'reason'):
            print(e.reason)
    except Exception as e:
        print(e)
