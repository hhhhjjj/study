# coding=utf-8
import os
from PyPDF4 import PdfFileReader
from PyPDF4 import PdfFileWriter


def get_reader(filename, password):
    try:
        old_file = open(filename, 'rb')
        print("第一次解密")
    except Exception as err:
        print("打开失败" + str(err))
        return None

    pdf_reader = PdfFileReader(old_file, strict=False)
#     这个strict是确定是否应该警告用户所用的问题，也导致一些可纠正的问题是致命的，默认是true
#     这个是创建读的实例
#   下面是解密操作
    if pdf_reader.isEncrypted:
        if password is None:
            print("文件被加密需密码")
            return None
        else:
            if pdf_reader.decrypt(password) != 1:
                print("密码不正确")
                return None
    if old_file in locals():
        old_file.close()
        return pdf_reader


def decrypt_pdf(filename, password, decrypted_filename=None):
    print("解密第1阶段")
    pdf_reader = get_reader(filename, password)
    if pdf_reader is None:
        return
    if not pdf_reader.isEncrypted:
        print("文件没有被加密")
        return
    pdf_writer = PdfFileWriter()
    pdf_writer.appendPagesFromReader(pdf_reader)
    if decrypted_filename is None:
        decrypted_filename = "".join(filename.split('.')[:-1] + '_decrypted.pdf')
        pdf_writer.write(open(decrypted_filename, 'wb'))


decrypt_pdf(r"pdf路径", "")

