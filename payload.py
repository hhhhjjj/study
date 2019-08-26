import os
# wireshark use particular group export to txt

if os.path.exists(r"D:\wireshark_data.txt"):
    os.remove(r"D:\wireshark_data.txt")


def wireshark_to_packet():
    write_F = open(r"D:\wireshark_data.txt", "a")
    i = 0
    with open(r"D:\wireshark_init.txt") as f:
        for every_package in f.readlines():
            if i % 4 == 2:
                # remainder equal to 2
                data_16 = every_package[155:-17].replace("|", ",0x")[1:]
                write_F.write("[" + data_16 + "],")
            i = i + 1
    write_F.close()
    # # delete the last ,
    # 这个不删除也可以,因为打包成exe之后这个命令会报错的
    # with open(r"D:\wireshark_data.txt", 'rb+') as filehandle:
    #     filehandle.seek(-1, os.SEEK_END)
    #     filehandle.truncate()


wireshark_to_packet()

