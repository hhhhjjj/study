import os
# wireshark use particular group export to txt

if os.path.exists("hhhhh_data.txt"):
    os.remove("hhhhh_data.txt")


def wireshark_to_packet():
    write_F = open("hhhhh_data.txt", "a")
    i = 0
    with open("hhhhh.txt") as f:
        for every_package in f.readlines():
            if i % 4 == 2:
                # remainder equal to 2
                data_16 = every_package[155:-17].replace("|", ",0x")[1:]
                write_F.write("[" + data_16 + "],")
            i = i + 1
    write_F.close()
    # delete the last ,
    with open("hhhhh_data.txt", 'rb+') as filehandle:
        filehandle.seek(-1, os.SEEK_END)
        filehandle.truncate()


wireshark_to_packet()

