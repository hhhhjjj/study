import xlrd
read_book = xlrd.open_workbook(r'.xls')
sheet = read_book.sheet_by_index(0)
icd_num = 1
icd = []
for icd_num in range(1, 19):
        for raw in range(1, 2):
                print(sheet.cell(0, icd_num).value)
                print(sheet.cell(raw, icd_num).value)


