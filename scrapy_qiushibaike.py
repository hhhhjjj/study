"""
scratch qiushibaike
先f12找到对应的内容位置
再找所需要的具体部分，鼠标右键用检查就行了
"""
from urllib import request
import re


class QSBK(object):
    def __init__(self):
        # 先构造内部的成员变量，属性这些
        # 这个是控制开关
        self.enable = True
        self.page = 1
        self.base_url = "http://www.qiushibaike.com/hot/page/"
        # 构建headers也是去F12看先去找user-agent
        self.headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:66.0) Gecko/20100101 Firefox/66.0"}

    def loadpage(self):
        # 抓取一页
        url = self.base_url + str(self.page)
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
        return True, response_page.read().decode("utf-8")
    #     因为涉及到中文，所以需要用utf-8编码才行
    #     需不需要头先不管，先试一下，不行再做个头出来

    def parsepage(self, page_content):
        # 构造正则表达式,写共有的属性,
        # *是可以不出现，也可以出现一次或者多次，？是最多出现一次，在这我们选择非贪婪模式
        # 最后提取的是两个h2之间的内容,我们只需要匹配第一个h2的就行了
        # .*代表所有的()表示提取括号里面的
        # 后面那个re.S是准备从后面那个S去找
        # 一定要注意这个正则表达式有没有错误，要一个个看
        pattern = re.compile('<div class="author clearfix">.*?<h2>(.*?)</h2>'
                             '.*?<div class="content">.*?<span>(.*?)</span>'
                             '.*?<span class="stats-vote">.*?<i class="number">(.*?)</i>'
                             '.*?</span>.*?<span class="stats-comments">.*?<i class="number">(.*?)</i>', re.S)
        # 每一个元素构造一个list
        items = re.findall(pattern, page_content)
        qlist = []
        for item in items:
            # 不要的空格都替换掉，只要指定的空格
            qlist.append([item[0].replace("\n", ""), item[1].replace("\n", ""), item[2].replace("\n", ""),
                          item[3].replace("\n", "")])
        for index, item in enumerate(qlist):
            print("第" + str(self.page) + "页" + "第" + str(index + 1) + "条段子")
            print(item[0] + "\n" + item[1] + "\n" + item[2] + "\n" + item[3])

    def start(self):
        # 在这不想用while true，想构造一个开关来控制这个
        while self.enable:
            # 先加载这一页
            # 命名一定要规范
            page_tuple = self.loadpage()
            # 再来解析这一页
            # 这个返回值的第一个正好可以用作开关
            if page_tuple[0]:
                self.parsepage(page_tuple[1])
                flag = input("输入其他任何显示下一页段子\n输入q退出\n：")
                if flag == "q":
                    # 这样子就不需要用break了
                    print("退出")
                    self.enable = False
                else:
                    self.page += 1
            else:
                # 页面加载失败之后
                self.enable = False
                # 打印错误原因
                print(page_tuple[1])


qsbk = QSBK()
# 这样子来自行，而不是直接就调用了
qsbk.start()

# QSBK().loadpage()
# # 这样子就打不开，估计是必须要构建headers才行
