"""
爬英文网站
先f12找到对应的内容位置
再找所需要的具体部分，鼠标右键用检查就行了
"""
from urllib import request
import re
import html
import os


class Your_text(object):
    def __init__(self):
        # 先构造内部的成员变量，属性这些
        # 这个是控制开关
        self.enable = True
        self.base_url = "https://www.scientificamerican.com/article/europe-stores-electricity-in-gas-pipes/?tdsourcetag=s_pcqq_aiomsg"
        self.base_url1 = "https://www.scientificamerican.com/article/an-arizona-utility-is-betting-big-on-energy-storage/?tdsourcetag=s_pcqq_aiomsg"
        # 构建headers也是去F12看先去找user-agent
        self.headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:66.0) Gecko/20100101 Firefox/66.0"}

    def loadpage(self, url):
        # 抓取一页
        # url = self.base_url
        request_page = request.Request(url, headers=self.headers)
        # 进行异常处理,怕网址不存在了
        try:
            response_page = request.urlopen(request_page)
        except request.URLError as e:
            if hasattr(e, "code"):
                # 这个e.code要转换成字符串，不然是数字类型，不能相加
                url_error = "错误原因：" + e.reason + "错误代码：" + str(e.code)
            else:
                url_error = "错误原因：" + e.reason
            return None, url_error
        return True, response_page.read().decode()
    #     因为涉及到中文，所以需要用utf-8编码才行
    #     需不需要头先不管，先试一下，不行再做个头出来

    def parsepage(self, page_content):
        # 构造正则表达式,写共有的属性,
        # *是可以不出现，也可以出现一次或者多次，？是最多出现一次，在这我们选择非贪婪模式
        # 最后提取的是两个h2之间的内容,我们只需要匹配第一个h2的就行了
        # .*代表所有的()表示提取括号里面的
        # 后面那个re.S是准备从后面那个S去找
        # 一定要注意这个正则表达式有没有错误，要一个个看
        pattern = re.compile('<div class="mura-region-local"><p>(.*?)</p></div>', re.S)
        # 每一个元素构造一个list
        items = re.findall(pattern, page_content)
        file = open("nlp.txt", "r+", encoding="utf-8")
        file.read()
        for item in items:
            # 处理多出来的标签
            item = item.replace("<p>", "")
            item = item.replace("</p>", "")
            item = item.replace("<em>", "")
            item = item.replace("</em>", "")
            item = item.replace("<h2>", "")
            item = item.replace("</h2>", "")
            # 处理超链接
            item = item.replace("</a>", "")
            deal_href = re.compile('(<a href=.*?>)', re.S)
            the_href = re.findall(deal_href, item)
            for href in the_href:
                item = item.replace(href, "")
            # 处理html转义字符
            item = html.unescape(item)
            file.writelines(item)
            file.writelines("\n")
        file.close()

    def start(self, url):
        # 在这不想用while true，想构造一个开关来控制这个
        while self.enable:
            # 先加载这一页
            # 命名一定要规范
            page_tuple = self.loadpage(url)
            # 再来解析这一页
            # 这个返回值的第一个正好可以用作开关
            if page_tuple[0]:
                self.parsepage(page_tuple[1])
                break
                # flag = input("输入q退出：")
                # if flag == "q":
                #     # 这样子就不需要用break了
                #     print("退出")
                #     self.enable = False
                # else:
                #     pass
            else:
                # 页面加载失败之后
                self.enable = False
                # 打印错误原因
                print(page_tuple[1])


my_nlp = Your_text()
# 写之前先检验文件是否存在，存在就删掉
if os.path.exists("nlp.txt"):
    os.remove("nlp.txt")
new_file = open("nlp.txt", "w+", encoding="utf-8")
new_file.close()
my_nlp.start(my_nlp.base_url)
my_nlp.start(my_nlp.base_url1)
