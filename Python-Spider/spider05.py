import gzip
import re
import http.cookiejar
import urllib.request
import urllib.parse
 
def ungzip(data):
    try:        # 尝试解压
        print('正在解压.....')
        data = gzip.decompress(data)
        print('解压完毕!')
    except:
        print('未经压缩, 无需解压')
    return data

def getXSRF(data):
    cer = re.compile('name=\"_xsrf\" value=\"(.*)\"', flags = 0)
    strlist = cer.findall(data)
    return strlist[0]
 
def getOpener(head):
    # deal with the Cookies
    cj = http.cookiejar.CookieJar()
    pro = urllib.request.HTTPCookieProcessor(cj)
    opener = urllib.request.build_opener(pro)
    header = []
    for key, value in head.items():
        elem = (key, value)
        header.append(elem)
    opener.addheaders = header
    return opener

header = {
    'Connection': 'Keep-Alive',
    'Accept': 'text/html, application/xhtml+xml, */*',
    'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Accept-Encoding': 'gzip, deflate',
    'Host': 'mail.163.com',
    'DNT': '1'
}
 
url = 'http://mail.163.com/'
opener = getOpener(header)
op = opener.open(url)
data = op.read()
data = ungzip(data)     # 解压
_xsrf = getXSRF(data.decode())

# url += 'login'
id = 'weekend27'
password = 'HWJ041'
postDict = {
        '_xsrf':_xsrf,
        'email': id,
        'password': password
}
postData = urllib.parse.urlencode(postDict).encode()
op = opener.open(url, postData)
data = op.read()
data = ungzip(data)

print(data.decode())

###
#正在解压.....
#解压完毕!
#Traceback (most recent call last):
#  File "/home/weekend27/workspace/15_Python/Python-Classroom/Python-Spider/spider05.py", line 48, in <module>
#    _xsrf = getXSRF(data.decode())
#  File "/home/weekend27/workspace/15_Python/Python-Classroom/Python-Spider/spider05.py", line 19, in getXSRF
#    return strlist[0]
#IndexError: list index out of range
###
