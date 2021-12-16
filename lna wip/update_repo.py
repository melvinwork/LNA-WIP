import sqlite3
from xlsxwriter.workbook import Workbook
import numpy as np

courses = np.load('courses_dict.npy', allow_pickle=True)
courses = courses.item()

conn = sqlite3.connect('course_repo.db')

c = conn.cursor()   

# update courses
for i in courses:
    course_name = courses[i]['course_title']
    course_date = courses[i]['course_dates']
    course_fee = courses[i]['course_fees']
    course_info = courses[i]['course_info']
    course_link = courses[i]['course_link']
    course_code = courses[i]['course_code']
    course_provider = courses[i]['course_provider']

    c.execute("SELECT * FROM courses WHERE course_name=? AND course_code=?", (course_name, course_code))
    
    select_check = c.fetchall()
    
    if not select_check:
        print('Course not in table. Inseting course...')
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
        
    else:
        print('Course already in table. Updating course...')
        
        c.execute("""UPDATE courses SET 
                  course_date = ?,
                  course_fee = ?,
                  course_info = ?
                  WHERE course_name = ? AND course_code = ?
                  """, (course_date, course_fee, course_info, course_name, course_code))

    conn.commit()
    

check_all = c.execute("SELECT * FROM courses")
fetch_all = c.fetchall()

conn.close()

