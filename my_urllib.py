# coding=utf-8
from urllib import request
import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
# 由于print的局限不能完全打印所有的unicode字符，win7python的默认编码不是utf-8，所以要这样子改默认编码
# 如果是控制台的话用gb18030，简体中文
req = request.Request("http://www.baidu.com")
req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
# 这个是模拟iPhone6去请求，这样子返回的是移动版网页。其他的自己百度去
with request.urlopen(req) as f:
    # with主要是用作文件处理这些，需要事先设置，事后做清理工作这种。
    # 文件处理可能会忘记关闭文件或者读取数据时候发生异常，用try finally太冗长了，用with就挺好，都能自动处理了
    data = f.read()
    print("status", f.status, f.reason)
    for k, v in f.getheaders():
        print(k, v)
    print(data.decode('utf-8'))

