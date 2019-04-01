"""
scratch qiushibaike
先f12找到对应的内容位置
再找所需要的具体部分，鼠标右键用检查就行了
"""
from urllib import request


class QSBK(object):
    def __init__(self):
        # 先构造内部的成员变量，属性这些
        # 这个是控制开关
        self.enable = True
        self.page = 1
        self.base_url = "http://www.qiushibaike.com/hot/page"
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
                url_error = e.reason + e.code
            else:
                url_error = e.reason
            return None, url_error
        return True, response_page.read().decode("utf-8")
    #     因为涉及到中文，所以需要用utf-8编码才行
    #     需不需要头先不管，先试一下，不行再做个头出来

    def parsepage(self):
        pass

    def start(self):
        # 在这不想用while true，想构造一个开关来控制这个
        while self.enable:
            # 先加载这一页
            page = self.loadpage()
            # 再来解析这一页
            if page:
                self.parsepage()
                flag = input("输入回车显示下一页段子\n输入q或者Q退出程序\n")
                if flag == "q" or "Q":
                    # 这样子就不需要用break了
                    self.enable = False
                else:
                    pass
            else:
                # 页面加载失败之后
                self.enable = False


# qsbk = QSBK()
# # 这样子来自行，而不是直接就调用了
# qsbk.start()

QSBK().loadpage()
# 这样子就打不开，估计是必须要构建headers才行
