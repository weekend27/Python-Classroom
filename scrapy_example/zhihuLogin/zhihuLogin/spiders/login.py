# -*- coding: utf-8 -*-

import scrapy
import os
import time

# mode 1:tencent   2:free
mode = 2
proxy = "https://web-proxy.oa.com:8080" if mode == 1 else ""

#设置 用户名和密码
email = "hwj278@mail.ustc.edu.cn"
password = "hwjyj1024"


class zhihuLoginSpider(scrapy.Spider):
    name = 'zhihuLogin'
    zhihu_url = "https://www.zhihu.com"
    login_url = "https://www.zhihu.com/login/email"
    domain = "https://www.zhihu.com"

    # 设置 Headers
    headers_dict = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "zh-CN,zh;q=0.8",
        "Connection": "keep-alive",
        "Host": "www.zhihu.com",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.109 Safari/537.36"
    }

    def start_requests(self):
        yield scrapy.Request(
            url=self.zhihu_url,
            headers=self.headers_dict,
            meta={
                "proxy": proxy,
                "cookiejar": 1
            },
            callback=self.request_captcha
        )

    def request_captcha(self, response):
        # 获取_xsrf值
        _xsrf = response.css('input[name="_xsrf"]::attr(value)').extract()[0]
        # 获得验证码的地址
        captcha_url = "http://www.zhihu.com/captcha.gif?r=" + str(time.time() * 1000)
        # 准备下载验证码
        # 获取请求
        yield scrapy.Request(
            url=captcha_url,
            headers=self.headers_dict,
            meta={
                "proxy": proxy,
                "cookiejar": response.meta["cookiejar"],
                "_xsrf": _xsrf
            },
            callback=self.download_captcha
        )

    def download_captcha(self, response):
        # 下载验证码
        with open("captcha.gif", "wb") as fp:
            fp.write(response.body)
        # 打开验证码
        os.system('open captcha.gif')
        # 输入验证码
        print "请输入验证码:\n"
        captcha = raw_input()
        # 输入账号和密码
        yield scrapy.FormRequest(
                                 url= self.login_url,
                                 headers= self.headers_dict,
                                 formdata={
                                     "email": email,
                                     "password": password,
                                     "_xsrf": response.meta["_xsrf"],
                                     "remember_me": "true",
                                     "captcha": captcha
                                 },
                                 meta={
                                     "proxy": proxy,
                                     "cookiejar": response.meta["cookiejar"],
                                 },
                                 callback=self.request_zhihu
        )

    def request_zhihu(self, response):
        '''
            现在已经登录,请求www.zhihu.com的页面
        '''
        yield scrapy.Request(url = self.zhihu_url,
                            headers = self.headers_dict,
                            meta = {
                                    "proxy": proxy,
                                    "cookiejar": response.meta["cookiejar"],
                                    "from": {"sign": "else", "data": {}},
                                },
                            callback = self.end_login,
                            dont_filter = True)

    def end_login(self, response):
        #至此已经登录
        with open("base.html", "wb") as fp:
            fp.write(response.body)
