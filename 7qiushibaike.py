# coding:utf-8
'''多线程爬虫'''
import urllib.request
import urllib.error
import re
import threading
class One(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):

        for i in range(2,10,2):
            url = 'https://www.qiushibaike.com/8hr/page/'+str(i)
            try:
                data = urllib.request.urlopen(url).read().decode('utf-8')
                print(data)
                pattern = '<div class="content">.*?<span>(.*)</span>.*?</div>'
                redata = re.compile(pattern, re.S).findall(data)
                print('第'+str(i)+'页')
                print(redata)
            except urllib.error.URLError as e:
                if hasattr(e,'code'):
                    print(e.code)
                if hasattr(e,'reason'):
                    print(e.reason)
            except Exception as e:
                print(e)

class Two(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        url = 'https://www.qiushibaike.com'
        for i in range(3,10,2):
            try:
                data = urllib.request.urlopen(url).read().decode('utf-8')
                print(data)
                pattern = '<div class="content">.*?<span>(.*)</span>.*?</div>'
                redata = re.compile(pattern, re.S).findall(data)
                print('第'+str(i)+'页')
                print(redata)
                url = 'https://www.qiushibaike.com/8hr/page/'+str(i)
            except urllib.error.URLError as e:
                if hasattr(e,'code'):
                    print(e.code)
                if hasattr(e,'reason'):
                    print(e.reason)
            except Exception as e:
                print(e)

if __name__ == '__main__':
    header = ('user-agent',
              'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36')
    openner = urllib.request.build_opener()
    openner.addheaders = [header]
    urllib.request.install_opener(openner)
    one = One()
    one.start()
    two = Two()
    two.start()

