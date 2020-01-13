# -*- coding: utf-8 -*-
# 接口一般是名词，然后给一个状态位，来定义动作
# 其实HTTP就是这样子
dog = ""
# 传递的时候，增删改查四个操作
status = "get" or "delete" or "put" or "post"
# GET /rest/api/deleteDogs/:dog_id要写成DELETE /rest/api/dogs/:dog_id
# GET /authors/12/categories/2的2语义不明确，所以写成GET /authors/12?categories=2

# 然后成功失败这些就看状态码，什么200这些
# 服务器返回的时候也别返回纯文本，还是要json
# 构造一个固定的格式出来，这样解析规则其实也就固定了
# HTTP / 1.1
# 200
# OK
# Content - Type: application / json
# Content - Length: xxx
#
# {
#     "url": "/api/categories/1",
#     "label": "Food",
#     "items_url": "/api/items?category=1",
#     "brands": [
#         {
#             "label": "友臣",
#             "brand_key": "32073",
#             "url": "/api/brands/32073"
#         }, {
#             "label": "乐事",
#             "brand_key": "56632",
#             "url": "/api/brands/56632"
#         }
#             ...
#     ]
# }

