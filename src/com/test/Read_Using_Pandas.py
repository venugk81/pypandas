import pandas as pd
from openpyxl import load_workbook

str_file_path = "E:\python projects\data\excel_data.xlsx"
df_emps = pd.read_excel(str_file_path, sheet_name='Sheet1')
df_it = df_emps.loc[(df_emps.Execute == 'Y')]
print(df_it)
print("-------------")
print(type(df_emps))

print(df_it.iloc[2])            #.ix is deprecated. use iloc[2]


