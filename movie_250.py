import bs4
# 在这不用正则表达式，用这个beautiful soup，帮我从页面上抓出想要的数据
import urllib.request
# 如果需要加访问头的话，用request好些，人为的加header装成是人为浏览器操作,有的网站反爬虫
# 可以用ip代理，每次访问就换个ip
# scrapy框架专门爬虫用的
url = 'http://movie.douban.com/top250'
movie_name_list = []


def get_Data(url):
    result = urllib.request.urlopen(url, data=None)
# 这个data默认表示是get操作，如果放上值就说明是post操作，其他什么timeout这些自己百度
    html = result.read().decode()
# 读取访问到的数据，但是这个数据不友好，所以要解码变成结构化的数据
    return html


# 处理数据
def paesr_data(html):
    soup = bs4.BeautifulSoup(html, 'html.parser')
# 后面那个是选择解析器，其他的都要装c语言的库
    movie_zone = soup.find('ol')
    movie_list = movie_zone.find_all('li')
    # 这是找所有的
    for movie in movie_list:
        movie_name = movie.find('span', attrs={'class': 'title'}).getText()
    #     这个还不是理想的效果,所以需要后面的get text才能拿到文本
        movie_name_list.append(movie_name)
    next_page = soup.find('span', attrs={'class': 'next'}).find('a')
    # 翻页如果存在
    if next_page:
        # 拿到新的超链接修改url来完成翻页
        new_url = url + next_page['href']
        paesr_data(get_Data(new_url))
    return movie_name_list


# def save_data(name_list):
#     res_file = open('top250movie.txt', 'w')
#     for name in name_list:
#         res_file.write(name + '\n')
#     #     写文件记得换行并且保存，记得关闭
#     res_file.close()


html = get_Data(url)
name_list = paesr_data(html)
for n in name_list:
    print(n)

