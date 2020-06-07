import openpyxl
from  openpyxl import Workbook
wb=Workbook()
sheet=wb.active

for i in range(1,11):
    sheet['A'+str(i)]=i

refObj=openpyxl.chart.Reference(sheet,min_row=1,min_col=1,max_row=10,max_col=1)

seriesObj=openpyxl.chart.Series(refObj,title='First series')

chartObj= openpyxl.chart.BarChart()
chartObj.append(seriesObj)
chartObj.anchor='B3' # set position
chartObj.width=7.94 # set the size (in centimeters, where 1 cm = 37.8 pixels)
chartObj.height=5.29 


sheet.add_chart(chartObj)
wb.save('SampleChart.xlsx')