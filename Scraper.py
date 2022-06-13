import tabula as tb
import pandas as pd
import numpy as np

file = r'2021-2022 Sem 2/2021-2022 Round 3/DemandAllocationRptUG_R3.pdf'
#file = r'2021-2022 Sem 2/2021-2022 Round 2/DemandAllocationRptUG_R2.pdf'
#file = r'2021-2022 Sem 2/2021-2022 Round 1/DemandAllocationRptUG_R1.pdf'
#file = r'2021-2022 Sem 2/2021-2022 Round 0/DemandAllocationRptUG_R0.pdf'
first_page = tb.read_pdf(file, pages = '1')
data = tb.read_pdf(file, pages = '2-106')


defaultFileName = "page"
filenumber = 0

#handle the first page of bullshit
print(filenumber)
newdata = pd.DataFrame()
first_page[0].rename(columns={'Unnamed: 2': 'Module\rCode', 'Unnamed: 5': 'Vacancy', 'Unnamed: 6': 'Demand'}, inplace=True) 
#first_page[0] = first_page[0].astype({"Vacancy": "int"})
for (colName, colData) in first_page[0].iloc[:,[2,5,6]].iteritems():
  newdata[colName] = colData.dropna(how='any')
#handle case where vacancy is '-' which essentially means 100% in 
#also for some reason the types as not always the same so astype to typecast
#using np.where as it's faster than df.replace
newdata['Vacancy'] = np.where(newdata['Vacancy'] == '-', newdata['Demand'], newdata['Vacancy'])
newdata['Demand'] = newdata['Demand'].fillna(0).astype(int)
newdata['Vacancy'] = newdata['Vacancy'].fillna(0).astype(int)
filenumber += 1

#currently newdata has info from first page

#for the rest of the pages
for item in data:
  print(filenumber)
  tempdata = pd.DataFrame()
  for (colName, colData) in item.iloc[:,[2,5,6]].iteritems():
    tempdata[colName] = colData.dropna()
  tempdata['Vacancy'] = np.where(tempdata['Vacancy'] == '-', tempdata['Demand'], tempdata['Vacancy'])
  tempdata['Demand'] = tempdata['Demand'].fillna(0).astype(int)
  tempdata['Vacancy'] = tempdata['Vacancy'].fillna(0).astype(int) 
  newdata = pd.concat([newdata, tempdata], axis=0)
  filenumber += 1

newdata.to_json(defaultFileName + str(filenumber) + '.json', orient='records')

