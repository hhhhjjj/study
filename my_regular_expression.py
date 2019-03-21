# coding=utf-8
import re
# # for in 后面接if else那么就可以考虑用列表生成式
# a = "ab23fd5g67"
# m = r"[0-9]+"
# r表示原始字符串，\n这些就不会当成换行符了
# num = re.findall(m, a)
# # 从字符串当中取出所有的数字
# str1 = "hello world"
# s = "hello world"
# ms = re.match(s, str1)
# # match从字符串的起始位置匹配一个正则表达式，如果成功就返回一个match对象，没成功就返回none。pattern指的是匹配的正则表达式
# print(ms.group(0))
# # group(0)用于返回匹配的整个字符串
# print(ms.span())
# # span（）用于以元组形式返回匹配的起始位置和结束位置

# s1 = "Tom"
# s2 = "Tim"
# s3 = "Tooooooom"
# m = r"T[io]+m"
# # 匹配T开头到m结尾的，中间可以i或者o，+表示可以匹配多次
# # print(re.match(m, s1).group(0))
# # print(re.match(m, s2).group(0))
# # print(re.match(m, s3).group(0))
# # 这三个都没问题，可以正常匹配，
# # print(re.match(m, "Tuple").group(0))
# # 这一个就无法匹配了

# m = r"^[0123456789]+$"
# = m = r"^[0-9]+$"
# print(re.match(m, "426576427").group(0))
# # ^匹配行首$匹配行尾，中括号内的表示字符串中所能包括的字符，所以如果这里面有字母就不成功
# m = r"^[a-zA-Z]+$"
# # 这个就是字母的了
# print(re.match(m, "sdhfaj").group(0))
# 其他的特殊字符自己百度去

# m = r"(\w+) is (\d{1,3}) years old"
# # （）用于匹配括号中的模式，可以再字符串中检索胡总匹配我们所需要的内容，这里一个是Tom，一个是23
# # \w匹配任意字母数字以及下划线
# # \d匹配任意数字
# # {1,3}将前面的模式匹配一到三次，前面是0到9，现在也就是0到999
# mat = re.match(m, "Tom is 23 years old,he is a nice boy")
# print(mat.group(0))
# print(mat.group(1))
# print(mat.group(2))
# # 字符串，以及里面两个括号

# m = r"(?P<name>\w+) is (?P<age>\d{1,3}) years old"
# mat = re.match(m, "Tom is 23 years old,he is a nice boy")
# print(mat.group("name"))
# print(mat.group("age"))
# # 这样子更加的直观了
# # mat = re.match(m, "Hi,You know?Tom is 23 years old,he is a nice boy")
# # 这时候match就不行了，match是从开始进行匹配的,要用search
# mat = re.search(m, "Hi,You know?Tom is 23 years old,he is a nice boy")
# print(mat)
# mat = re.fullmatch(m, "Tom is 23 years old")
# # fullmatch试图匹配整个字符串，而不是字符串的一部分，所以没什么用
# print(mat)

m = r"\d+"
repl = " "
s = "23ufadsjbhjb34fda"
print(re.sub(m, repl, s))
# sub用参数repl替换与正则表达式pattern相匹配的子串，其中的repl可以是字符串或者函数，如果是函数的话，必须要返回一个用于替换的字符串
# 这个就是把数字全部替换成了空格了
# subn就是在返回值中多了个匹配的数量，已元组的形式返回
print(re.split(m, s))
# 这个是分割字符串
print(re.search(m, s))
# 只返回找到的第一个匹配
print(re.findall(m, s))
# 返回所有非重叠匹配的列表，finditer返回的是包含所有匹配对象的列表
mode = re.compile("\d+")
# 编译正则表达式生成一个pattern
print(mode)
# 各个方法里面都有flags，有什么用自己研究

