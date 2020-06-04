#!/usr/bin/env python3
# readCensusExcel.py - Tabulates population and number of census tracts for
# each county.

import openpyxl,pprint
print('Opening workbook...')
wb=openpyxl.load_workbook('/home/hasnat/Desktop/automate_boring_stuff/Chapter 12/censuspopdata.xlsx')
sheet = wb['Population by Census Tract']
countyData={}

#data structure sample
# {'AK': {'Aleutians East': {'pop': 3141, 'tracts': 1},
# 'Aleutians West': {'pop': 5561, 'tracts': 2},
# 'Anchorage': {'pop': 291826, 'tracts': 55},
# 'Bethel': {'pop': 17013, 'tracts': 3},
# 'Bristol Bay': {'pop': 997, 'tracts': 1}}

# >>> countyData['AK']['Anchorage']['pop']
# 291826
# >>> countyData['AK']['Anchorage']['tracts']
# 55


print('Reading rows...')
# with open('printedData.txt','w') as f:
for row in range(2,sheet.max_row+1):
    state=sheet['B'+str(row)].value
    county=sheet['C'+str(row)].value
    pop=sheet['D'+str(row)].value
        
    # make sure the key for this state exists.
    countyData.setdefault(state,{})
    # make sure the key for this county in this state exists
    countyData[state].setdefault(county,{'tracts':0,'pop':0})

    # each row represents one census tract, so increment by one.
    countyData[state][county]['tracts']+=1
    # Increase the county pop by the pop in this census tract.
    countyData[state][county]['pop'] += int(pop)

print('Writing results...')
resultFile=open('census2010.py','w')
resultFile.write('allData ='+pprint.pformat(countyData))
resultFile.close()
print('Done') 