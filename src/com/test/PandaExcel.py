import pandas as pd


# df= pd.read_excel("E:\python projects\data\excel_data.xlsx", sheet_name="Sheet2")
# df1 = df[df['Execute'].str.contains("Y|Yes")]
# print (df1)
#
# for index, row in df1.iterrows():
#     print(row["TestName"], row["Steps"])
#     df1.at[index, 'Status']= "Pass"
#
# print("DONE")
# df1.to_excel("E:\python projects\data\excel_data2.xlsx", index=False, header=True)


def read_excel_file(exl_path, sheet_name):
    df1 = pd.DataFrame
    try:
        df = pd.read_excel(exl_path, sheet_name=sheet_name)
        # return test steps marked Yes for execution
        df1 = df[df['Execute'].str.contains("Y|Yes")]
    except Exception as err:
        raise err
    return df1

def update_status(dataframe, index, col, status):
    dataframe.at[index, col] = status

def save_file(dataframe, str_file_path):
    dataframe.to_excel("E:\python projects\data\excel_data4.xlsx", index=False, header=True)

df = read_excel_file("E:\python projects\data\excel_data.xlsx", "Sheet2")
for index, row in df.iterrows():
    update_status(df, index, "Status", "PASS")

save_file(df, "E:\python projects\data\excel_data4.xlsx")
