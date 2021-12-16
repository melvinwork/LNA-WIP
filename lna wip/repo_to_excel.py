import sqlite3
from xlsxwriter.workbook import Workbook
import numpy as np

workbook = Workbook('course_repo.xlsx')
worksheet = workbook.add_worksheet()

conn = sqlite3.connect('course_repo.db')

c = conn.cursor()   

select_all = c.execute("SELECT * FROM courses")

column_names = c.description

for i, column in enumerate(column_names):
    worksheet.write(0, i, column[0])

for i, row in enumerate(select_all):
    for j, value in enumerate(row):
        worksheet.write(i+1, j, row[j])

workbook.close()

conn.close()

