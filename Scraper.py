import tabula as tb
import pandas as pd
import re

file = 'DemandAllocationRptUG_R2.pdf'
data = tb.read_pdf(file, pages = '1-3')

#print(data[0].iloc[:,2].dropna())


defaultFileName = "page"
filenumber = 0
for item in data:
  print(filenumber)
  output = open(defaultFileName + str(filenumber) + ".txt", "a")
  newdata = pd.DataFrame()
  for (colName, colData) in item.iloc[:,[2,5,6]].iteritems():
    #output.write("\n------------------------------------------------\n")
    newdata[colName] = colData.dropna()
  output.write(newdata.to_string())
  output.close()
  filenumber += 1

