import sqlite3
from xlsxwriter.workbook import Workbook
import numpy as np

# load course info from web scraping
courses = np.load('courses_dict.npy', allow_pickle=True)
courses = courses.item()

# create/connect to course_repo.db
conn = sqlite3.connect('course_repo.db')

c = conn.cursor()   

# delete if table "courses" already exists
try:
    c.execute("DROP TABLE courses")
    conn.commit()
    
    print('Dropping previously created table...')
    
except:
    print('No previously created table.')

# create table courses
c.execute("""CREATE TABLE courses (
     course_name text,
     course_info text,
     course_date text,
     course_fee text,
     course_link text,
     course_code text,
     course_provider text
     )""")

# add courses to table
for i in courses:
    course_name = courses[i]['course_title']
    course_date = courses[i]['course_dates']
    course_fee = courses[i]['course_fees']
    course_info = courses[i]['course_info']
    course_link = courses[i]['course_link']
    course_code = courses[i]['course_code']
    course_provider = courses[i]['course_provider']

    c.execute("""INSERT INTO courses (
        course_name,
        course_info,
        course_date,
        course_fee,
        course_link,
        course_code,
        course_provider
        ) VALUES(?,?,?,?,?,?,?)""", 
        (course_name, course_info, course_date, course_fee, course_link, course_code, course_provider))

    conn.commit()
    
check_all = c.execute("SELECT * FROM courses")
fetch_all = c.fetchall()

conn.close()

