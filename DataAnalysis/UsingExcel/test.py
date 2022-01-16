from random import sample
import pandas as pd
from openpyxl.styles import Border, Side, Font

sample_data = {"a": ["1","2","3","4"], "b":["2","3","4","5"], "c":["3","4","5","7"], "d":["a","b","c","d"]}

df1 = pd.DataFrame(sample_data)
df2 = pd.DataFrame(sample_data)
df3 = pd.DataFrame(sample_data)

write = pd.ExcelWriter("./hello.xlsx")
df1.to_excel(write, sheet_name="test1", index=False)
df2.to_excel(write, sheet_name="test2")
df3.to_excel(write, sheet_name="test3")

non_border = Border(right=Side(), left=Side(), top=Side(), bottom=Side())

worksheet = write.sheets['test1']

for i in worksheet["1:1"]:
  i.border = non_border
  i.font = Font(bold=False)
for j in worksheet["a"]:
  j.number_format = '###.00'

for column_cells in worksheet.columns:
    length = max(len(str(cell.value)) for cell in column_cells)
    worksheet.column_dimensions[column_cells[0].column_letter].width = length

write.save()