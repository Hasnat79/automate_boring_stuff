import openpyxl
wb=openpyxl.load_workbook("/home/hasnat/Desktop/automate_boring_stuff/Chapter 12/example.xlsx")
# sheet=wb['Sheet1']
# print(tuple(sheet['A1':'C3']))

# for rowOfCellObjects in sheet['A1':'C3']:
#     for cellObj in rowOfCellObjects:
#         print(cellObj.coordinate,cellObj.value)
#     print('---END OF ROW---')

sheet=wb.active
print(list(sheet.columns)[1])
for i in list(sheet.columns)[1]:
    print(i.value)

