import openpyxl

str_file_path = "E:\python projects\data\excel_data.xlsx"
# load excel with its path
wrkbk = openpyxl.load_workbook(str_file_path)

sh = wrkbk.active

# iterate through excel and display data
for row in sh.iter_rows(min_row=1, min_col=1, max_row=12, max_col=4):
    for cell in row:
        if cell.value is not None:
            print(cell.value, end=" ")
        else:
            break
    print()
print("testing-----------------")