import pandas as pds
from pandas import ExcelWriter
from pandas import ExcelFile
import numpy as np

file = (r'C:/Users/Admin/Desktop/15872 PV Status.xlsx')
newData = pds.read_excel(file)
print(newData)
print(type(newData))
writer = ExcelWriter(r'C:/Users/Admin/Desktop/output.xlsx')
newData.to_excel(writer,'Sheet1',index=False)
writer.save()