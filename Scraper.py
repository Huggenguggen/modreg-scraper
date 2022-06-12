import tabula as tb
import pandas as pd
import re

file = 'DemandAllocationRptUG_R2.pdf'
output = open("test.txt", "a")
data = tb.read_pdf(file, pages = '1')

print(data[0].iloc[:,2].dropna())

newdata = pd.DataFrame()

for (colName, colData) in data[0].iloc[:,[2,5,6]].iteritems():
  #output.write("\n------------------------------------------------\n")
  newdata[colName] = colData.dropna()

output.write(newdata.to_string())



#table = data.to_string()
#output.write(data[0])
  
output.close()