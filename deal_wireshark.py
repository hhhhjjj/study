import json
import os
if os.path.exists("data.txt"):
    os.remove("data.txt")
#  if have file, first delete


def wireshark_to_packet():
    f = open("data.txt", "a")
    with open('data.json', 'rb') as load_json:
        # this is use rb not r,otherwise could UnicodeDecodeError
        load_all = json.load(load_json)
        # load_all is a list
        for package in load_all[:-1]:
            # last column alone write to avoid /n in txt
            data_16 = package['a']['b']['c']['d'][23:-12].replace(":", ",0x")[1:]
            # find data and turn to 16
            f.write("[" + data_16 + "]" + "\n")
        f.write("[" + load_all[-1]['a']['b']['c']['d'][23:-12].replace(":", ",0x")[1:] + "]")
    f.close()

    
def read_txt():
    with open("data.txt") as f:
        for every_package in f.readlines():
            print(every_package)

            
wireshark_to_packet()
#  expected an indented block
#  要注意可能是tab和空格的区别
#  各个编译器上的不一样
