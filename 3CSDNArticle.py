# coding:utf-8
import urllib.request
import re

url = 'http://blog.csdn.net/'

header = ('User-Agent',
          'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36')
openner = urllib.request.build_opener()
openner.addheaders = [header]
urllib.request.install_opener(openner)

data = urllib.request.urlopen(url).read()
print(data.decode('utf-8'))

pattern = '<a strategy=".*?" href="(http://blog.csdn.net/.*?)" target="_blank">'
all_link = re.compile(pattern).findall(data.decode('utf-8'))

print(all_link)

for link in all_link:
    data = urllib.request.urlopen(link).read()
    pattern = '<h1 class="csdn_top">(.*)</h1>'
    title = re.findall(pattern, data.decode('utf-8'))
    strtitle = ''.join(title)
    print(strtitle)
    urllib.request.urlretrieve(link, 'G:/python/Spider/DataAnalysis/3CSDNArticle/' + strtitle + '.html')


