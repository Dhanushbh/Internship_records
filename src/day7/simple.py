from openpyxl import load_workbook

wb = load_workbook("sample_students.xlsx")
sheet = wb.active

for row in sheet.values:
    print(row)
