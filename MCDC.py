# coding=utf-8
import xlrd
import xlwt
read_book = xlrd.open_workbook(r'需要的.xlsx')
write_book = xlwt.Workbook(r'需要的.xlsx')
sheet = read_book.sheet_by_index(3)
write_sheet = write_book.add_sheet("需要的")
orgin_number = 0
list_set = []
list_value = []
for i in range(10, 50):
    if str(sheet.cell(i, 1).value) == "SET":
        my_set = str(sheet.cell(i, 2).value)
        my_value = str(sheet.cell(i, 3).value)
        list_set.insert(i - 10, my_set)
        list_value.insert(i - 10, my_value)
        orgin_number = orgin_number + 1
    elif str(sheet.cell(i, 1).value) == "VERIFY":
        break
print(list_set)
print(list_value)
# 读最开始的数据
for i in range(0, orgin_number):
    write_sheet.write(i, 1, "SET")
    write_sheet.write(i, 2, list_set[i])
    write_sheet.write(i, 3, list_value[i])
write_sheet.write(orgin_number, 1, "VERIFY")
write_sheet.write(orgin_number, 2, "显示")
# 第一行显示
for mid in range(0, orgin_number):
    for i in range((mid + 1) * orgin_number + 1 + mid, mid + (mid + 1) * orgin_number + 1 + mid):
        write_sheet.write(i, 1, "SET")
        write_sheet.write(i, 2, list_set[i - ((mid + 1) * orgin_number + 1 + mid)])
        write_sheet.write(i, 3, list_value[i - ((mid + 1) * orgin_number + 1 + mid)])
    write_sheet.write(mid + (mid + 1) * orgin_number + 1 + mid, 1, "SET")
    write_sheet.write(mid + (mid + 1) * orgin_number + 1 + mid, 2, list_set[mid + (mid + 1) * orgin_number + 1 + mid
                                                                            - ((mid + 1) * orgin_number + 1 + mid)])
    write_sheet.write(mid + (mid + 1) * orgin_number + 1 + mid, 3, 0)
    # 各赋值为0一次
    for i in range(mid + (mid + 1) * orgin_number + 1 + mid + 1, orgin_number + (mid + 1) * orgin_number + 1 + mid):
        write_sheet.write(i, 1, "SET")
        write_sheet.write(i, 2, list_set[i - ((mid + 1) * orgin_number + 1 + mid)])
        write_sheet.write(i, 3, list_value[i - ((mid + 1) * orgin_number + 1 + mid)])
    write_sheet.write(orgin_number + (mid + 1) * orgin_number + 1 + mid, 1, "VERIFY")
    write_sheet.write(orgin_number + (mid + 1) * orgin_number + 1 + mid, 2, "不显示")
# 中间阶段不显示
for i in range(orgin_number + (orgin_number + 1) * orgin_number + 1,
               orgin_number + orgin_number + (orgin_number + 1) * orgin_number + 1):
    write_sheet.write(i, 1, "SET")
    write_sheet.write(i, 2, list_set[i - (orgin_number + (orgin_number + 1) * orgin_number + 1)])
    write_sheet.write(i, 3, 0)
write_sheet.write(orgin_number + orgin_number + (orgin_number + 1) * orgin_number + 1, 1, "VERIFY")
write_sheet.write(orgin_number + orgin_number + (orgin_number + 1) * orgin_number + 1, 2, "clear")
# 最后阶段消失
write_book.save(r'需要的1.xlsx')















