# 用浏览器看源代码，在网络里面随便找一个请求查看request-header
# 主要就是看cookie和user-agent,其他的自己百度去
# 登陆之前打开网络清空，登陆后查看抓取的网络的这些，看logic的，http协议不但有头还有内容
# request urls请求web服务器的完整域名，不只是域名，包括访问的文件所在的具体位置，url携带的访问参数
# request method是请求方式，比如post或者get方式，提交表单一般都是post
# status code：200表示访问成功，就能够获取网页资源，302是错误
# user-agent是客户端运行的浏览器类型的详细信息，能够判断出来是浏览器类别，主要是看网站开发人员是怎么做的
# host是web服务器域名地址
# accept是制定客户端能够接收的内容类型，先后次序表示客户端接收的先后次序，很多网站都是发个压缩的过来，再解压缩
# 比如弄个无图模式就没图了
# referer是父页面
# cookie是返回信息
# http协议最开始是短链接的，不会一直保持，后面才出现的长连接，后面反正服务器多了
# 短链接相当于国企服务态度，一次请求完就赶走了。长连接就是健身房的服务态度，会一直占着网络资源导致浪费
# keep-alive是表示一定时间内连接持续有效，当出现服务器后继请求之后，这个可以避免重新建立连接
# 有keep-alive就是长连接
# 无状态是协议对事务吹没有记忆能力，不知道客户端是什么状态，打开这个网页和之前的没有任何联系
# 有状态就是和之前的有联系，http是无状态的，所以需要记下来客户端的状态才行，用session
# cookie是服务器生成的，发送给浏览器，下次请求同一网站时候就会发送这个cookie给服务器
# 假设Web Server是一个商场的存包处，HTTP Request是一个顾客，
# 第一次来到存包处，管理员把顾客的物品存放在某一个柜子里面（这个柜子就相当于Session），
# 然后把一个号码牌交给这个顾 客，作为取包凭证（这个号码牌就是Session ID）
# referer可以防盗链用，就是指定只能从哪个网站进去这个子页面
# html是骨架，js是肌肉，css是衣服

from urllib import request, parse
from http import cookiejar
import re

# response = request.urlopen("http://www.baidu.com")
# # 这里面还可以设置一个data，一个timeout。
# 如果是post提交数据就需要构建data值，data一般都是放表单里面
# 设置超时时间是timeout，主要是为了解决一些网站实在是响应过慢而造成的影响，打不开就返回超时
# request = request.Request("http://www.baidu.com")
# # 这个和前面的并不一样，这个能携带的参数多很多，比如头信息这些，主要也就是用头信息
# # 如果request传入参数，那么urlopen就不用传了，都传了就以urlopen为准
# # 提交参数的话就进登陆网站，然后开发者模式一直开，登陆后看下面的包
# response1 = request.urlopen(request)

# values = {'username': 'XXX', 'password': 'XXXX'}
# # 有的要输入的信息很多，自己开发者模式去复制
# data = parse.urlencode(values).encode('utf-8')
# # 提交类型不能为str，需要为byte类型,所以就要这样子转码
# url = 'https://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn'
# headers = {"cookie": "开发者模式自己看去，再复制过来,就能进入当前cookie的状态"}
# # headers一般不需要转码
# request1 = request.Request(url, data, headers=headers)
# response1 = request.urlopen(request1)
# print(response1.read().decode('utf-8'))
# # 这个输出的就是登陆进去之后的页面了，你可以复制出来用网页打开就可以看出来了
# # python2的urllib和urllib2区别自己百度去，3中都是urllib了
# # 如果是post方式要提交表单，那么就要用data数据，参数要对应
# # 如果是get方式，就可以直接把参数写道网址上面，构建一个带参数的url就行
# my_url = url + "?" + data
# # 就这样子构建get方式下的url就行
# # 有些网站必须设置header，就是user-agent，不然直接就不响应
# # 对付防盗链，也就是referer，就在headers里面加referer为父网址就行了
#
# # 代理设置，也是怕一段时间访问过多禁止ip用的，过段时间换个代理
# # proxy_handler = request.ProxyHandler({"https": "http://127.0.0.1:1080"})
# # # 后面的网址是本地代理服务器的客户端，一般都要先下载个软件，这个连到代理服务器商，然后可以上外国网这些
# # # 反正自己百度去找个下载
# # opener = request.build_opener(proxy_handler)
# # request.install_opener(opener)
# # url1 = "http://www.google.com"
# # result = opener.open(url1).read()
# # # 这样子用这个opener就能访问国外网站了
#
# # url error：没网，连不上服务器，服务器不存在。e.reason
# # 用try except来显示错误，并且能够继续执行，不然程序就断开了
# # http error是url error的子类。会返回状态码。自己百度主要状态码去。这个一定是网址存在才会触发http error
# # 比如网址存在但是资源不存在
# # http error实例产生后又一个code属性，urllib可以处理重定向，所以只能看到400-599之间的错误号码
# # 能捕获http error就不会抛出url error
# # try:
# #     request.urlopen(url)
# # except request.URLError as e:
# #     if hasattr(e, "code"):
# # # 这个hasattr是判断对象是否包含对应的属性
# #         print(e.code)
# #     print(e.reason)
#
# # cookie主要是对抗http无状态用的,因为网站想要记录用户的登陆状态。用session也可以
# # opener就是获取url用的，比如常用的urlopen，如果需要用到cookie，那么这个就不行了，需要创建个出来
# # cookielib模块主要是提供可存储的cookie对象来配合urllib访问网络资源
# # cookiejar派生出filecookiejar派生出其他的
#
# # 将cookie保存到内存中
#
# cookie = cookiejar.CookieJar()
# # 声明对象实例来保存cookie
# handler = request.HTTPCookieProcessor(cookie)
# opener = request.build_opener(handler)
# post_data = parse.urlencode({"账号": "密码"})
# # 通过handler来构建opener
# # 前面这三步必不可少
# response = opener.open("要访问的网址", post_data)
# # cookie的生成由web服务端决定
# for item in cookie:
#     # 遍历出cookie的值，因为不止一个
#     print(item.name)
#     print(item.value)
# response2 = opener.open("另外其他的需要知道cookie的网页")
# # 这里带的是前面的cookie或者session
# # cookie中存储的内容由web服务器端来决定
# print(response2.read())
# file = 'c:/cookie.txt'
# cookie = cookiejar.MozillaCookieJar(file)
# handler = request.HTTPCookieProcessor(cookie)
# opener = request.build_opener(handler)
# cookie.save(ignore_discard=True, ignore_expires=True)
# # 就这样子保存cookie到文件
# cookie.load('c:/cookie.txt', ignore_discard=True, ignore_expires=True)
# response = opener.open("要访问的网址")
# # 这样子加载cookie，比如直接拿别人登陆好的cookie而不需要知道他的账号密码

# 正则表达式python中默认是贪婪模式，就是尽可能匹配多的字符，想要不贪婪就中间加？
# 上次基本上写过了
p = r'(\d)\1+([a-zA-Z]+)'
s = '1111werwrw3333rertert4444'
m = re.finditer(p, s)
# 这个返回的是迭代器
print(m.__next__().group())
print(m.__next__().group())
# 输出的每次会接下去之前的

