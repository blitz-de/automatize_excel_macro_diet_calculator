import xlwings as xw
import pandas as pd



wk = xw.books.open(r'Muscle Macros.xlsx')
sheet = wk.sheets("Food List")
rg = sheet.range("A1:C2")
sheet.range("A32").value = "hello mate"

print(sheet.range("A32").value)
# df = sheet.range("A1:C13").options(pd.DataFrame).value


# xw.view(df)
# wk.close


