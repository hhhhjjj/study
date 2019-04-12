# coding=utf-8
# 这个http的header其实就是类似tcp构造协议包头一样的，在这用wireshark抓http包
# POST / HTTP/1.1第一行的首先是请求类型，然后是请求资源，在这没有，然后是http版本。这是请求行
# 从这开始就进入请求头了，User-Agent就不说了
# Host是请求的目的地
# 这个content长度是指的这个包的的长度，不包括请求行和包头，因为也是有封包粘包处理这些
# 空行之后是这个包的数据
# Request Method现在有8种方式了，除了GET和POST，HEAD是类似get，只不过是获取报头用，没具体内容
# DELETE是请求服务器删除指定的页面，CONNECT是预留给代理服务器用的，OPTIONS是运行客户端查看服务器性能，TRACE是回显服务器收到的请求，用于测试
# Content-Type和charset是返回的数据类型和字符编码格式
import json
import time
http_version = "HTTP/1.1\n"
Server = "Server:nginx\n"
# 格式化获得当前的时间
Date = time.strftime('%Y-%m-%d %H:%M:%S\n', time.localtime(time.time()))
ContentType = "Content-Type: text/html\n"
charset = "charset=GBK\n"
RequestMethod = "GET\n"
first_header = ""
first_body = {"flag": None, "content": None}


def make_header(replace_body_len):
    addheader(http_version)
    addheader(Server)
    addheader(Date)
    addheader(ContentType)
    addheader(charset)
    addheader(RequestMethod)
    addheader("Content_Lenth:" + str(len(replace_body_len)) + "\n")
    header = first_header
    print(header)
    return json.dumps(header)


def addheader(add_header):
    global first_header
    header = first_header
    first_header = header[0:len(header)] + add_header + header[len(header) + len(add_header):]
    return first_header


def make_body(body):
    return json.dumps(body)


def close_package(body):
    body = make_body(body)
    header = make_header(str(len(body)))
    return header+body


print(close_package(first_body))

