import re
import json
with open('data.json', 'rb') as load_json:
    # this is use rb not r,otherwise could UnicodeDecodeError
    load_all = json.load(load_json)
    print(load_all)