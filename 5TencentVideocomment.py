# coding:utf-8

import urllib.request
import re

header = ('user-agent',
          'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36')

openner = urllib.request.build_opener()
openner.addheaders = [header]
urllib.request.install_opener(openner)
commentid = '6375522289425535207'
j = 1
for i in range(0, 10):
    try:
        url = 'https://video.coral.qq.com/varticle/2457683703/comment/v2?callback=_varticle2457683703commentv2&orinum=10&oriorder=o&pageflag=1&cursor=' + commentid + '&scorecursor=0&orirepnum=2&reporder=o&reppageflag=1&source=9&_=1520088151465'
        data = urllib.request.urlopen(url).read().decode()
        patnext = '"last":"(.*?)"'
        nextid = re.compile(patnext).findall(data)
        patcomment = '"content":"(.*?)",'
        comments = re.compile(patcomment).findall(data)

        for comment in comments:
            print('第' + str(j) + '条评论')
            print(eval('u' + "'" + comment + "'"))
            j = j + 1
        commentid = ''.join(nextid)
    except urllib.error.URLError as e:
        if hasattr(e, 'code'):
            print(e.code)
        if hasattr(e, 'reason'):
            print(e.reason)
    except Exception as e:
        print(e)
