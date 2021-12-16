from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import numpy as np

courses = {}

# set up selenium chrome driver
DRIVER_PATH = r'chromedriver.exe'

options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")

driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)

#%% scrape nus iss courses
course_links = []
course_provider = 'NUS ISS'

with open('links_nus_iss.txt') as file:
    for line in file:
        # line = line.replace(line.split('/')[-1], '')
        if line not in course_links:
            course_links.append(line)

# with open('links_new.txt', 'w') as f:
#     f.write("\n".join(map(str, course_links)))



#address = 'https://www.iss.nus.edu.sg/executive-education/course/detail/architecting-iot--solutions/'
# address = 'https://www.iss.nus.edu.sg/executive-education/course/detail/vision--systems/artificial-intelligence'
# address = 'https://www.iss.nus.edu.sg/executive-education/course/detail/graph-and-web--mining/data-science'


for address in course_links:
    driver.get(address)
    html_text = driver.page_source #get html text
    
    
    # course title
    course_title = driver.find_element_by_id('hdrTitle').text
    
    # course fees
    container = driver.find_element_by_id('tab4')
    container = container.find_elements_by_tag_name('tr')
    try:
        container = container[-1]
    except:
        container = driver.find_element_by_id('tab5')
        container = container.find_elements_by_tag_name('tr')
        container = container[-1]
        
    container = container.find_elements_by_tag_name('td')
    container = container[-1]
    course_fees = container.text
    
    # course dates
    container = driver.find_elements_by_class_name('accordion_header-date')
    course_dates = []
    
    for e in container:
        course_dates.append(e.text)
    
    course_dates = '\n'.join(course_dates)    
    
    
    # course info
    container = driver.find_element_by_id('overview')
    container = container.find_elements_by_tag_name('p')
    
    course_info = []
    
    for e in container:
        course_info.append(e.text)
    
    course_info = ' '.join(course_info)
    
    if not container:
        container = driver.find_element_by_id('overview')
        text = container.text
        course_info = text.split('\n')[6] + text.split('\n')[8]
        
        if not text.split('\n')[6]:
            course_info = text.split('\n')[7] + text.split('\n')[9]
        
           
    
    
    # course code
    container = container = driver.find_element_by_id('overview')
    container = container.find_elements_by_tag_name('td')
    course_code = container[0].text
    
    courses[len(courses) + 1] = {}
    courses[len(courses)]['course_title'] = course_title
    courses[len(courses)]['course_fees'] = course_fees
    courses[len(courses)]['course_dates'] = course_dates
    courses[len(courses)]['course_info'] = course_info
    courses[len(courses)]['course_link'] = address
    courses[len(courses)]['course_code'] = course_code
    courses[len(courses)]['course_provider'] = course_provider

#%% scrape SP courses
course_links = []
course_provider = 'SP'

with open('links_sp.txt') as file:
    for line in file:
        # line = line.replace(line.split('/')[-1], '')
        if line not in course_links:
            course_links.append(line)

for address in course_links:
    driver.get(address)
    html_text = driver.page_source #get html text

    #course title
    container = driver.find_elements_by_class_name('rte')
    container = container[-1]
    container = container.find_element_by_tag_name('h1')
    course_title = container.text
    
    #course dates
    container = driver.find_element_by_id('course-info')
    container = container.find_element_by_tag_name('p')
    course_dates = container.text
    course_dates = course_dates.split('\n')[-1]
    
    #course info
    container = driver.find_element_by_id('course-info')
    container = container.find_elements_by_tag_name('p')
    container = container[6:14]
    
    course_info = ''
    
    for i in container:
        course_info += i.text
        course_info += '\n'
        
    #course fees
    container = driver.find_element_by_link_text('Fees & Funding')
    container.click()
    container = driver.find_element_by_id('fees-funding')
    container = container.find_elements_by_tag_name('tr')[2]
    container = container.find_elements_by_tag_name('td')[1]
    course_fees = container.text
    
    
    #course code
    course_code = '-'

    courses[len(courses) + 1] = {}
    courses[len(courses)]['course_title'] = course_title
    courses[len(courses)]['course_fees'] = course_fees
    courses[len(courses)]['course_dates'] = course_dates
    courses[len(courses)]['course_info'] = course_info
    courses[len(courses)]['course_link'] = address
    courses[len(courses)]['course_code'] = course_code
    courses[len(courses)]['course_provider'] = course_provider


#%% scrape SMU courses
course_links = []
course_provider = 'SMU'

with open('links_smu.txt') as file:
    for line in file:
        # line = line.replace(line.split('/')[-1], '')
        if line not in course_links:
            course_links.append(line)

for address in course_links:
    driver.get(address)
    html_text = driver.page_source #get html text
    
    #course title
    container = driver.find_element_by_id('page-title')
    course_title = container.text
    
    #course dates
    container = driver.find_element_by_id('schedule')
    container = container.find_element_by_class_name('course-details-section-content')
    container = container.find_element_by_class_name('field--item')
    course_dates = container.text
    
    
    #course info
    container = driver.find_element_by_id('overview')
    container = container.find_elements_by_tag_name('div')[6]
    container = container.find_elements_by_tag_name('p')
    container = container[0:-1]
    
    course_info = ''
    for i in container:
        course_info += i.text
        course_info += '\n'
    
    #course fees
    container = driver.find_elements_by_class_name('info-table')[1]
    container = container.find_elements_by_tag_name('tr')[1]
    container = container.find_elements_by_tag_name('td')[0]
    course_fees = container.text[0:-1]
    
    #course code
    course_code = '-'

    courses[len(courses) + 1] = {}
    courses[len(courses)]['course_title'] = course_title
    courses[len(courses)]['course_fees'] = course_fees
    courses[len(courses)]['course_dates'] = course_dates
    courses[len(courses)]['course_info'] = course_info
    courses[len(courses)]['course_link'] = address
    courses[len(courses)]['course_code'] = course_code
    courses[len(courses)]['course_provider'] = course_provider

#%% scrape nvidia
course_links = []
course_provider = 'Nvidia'

#with open('links_test.txt') as file:
with open('links_nvidia.txt') as file:
    for line in file:
        if line not in course_links:
            course_links.append(line)

for address in course_links:
    driver.get(address)
    html_text = driver.page_source #get html text
     
    #course title
    container = driver.find_element_by_class_name('heroBanner')
    container = container.find_element_by_tag_name('h1')
    course_title = container.text.split('\n')[-1]
     
    #course dates
    if html_text.find('Upcoming Public Workshops') == -1:
        course_dates = '-'
    
    else:
        course_dates = html_text[html_text.find('Upcoming Public Workshops'):]
        course_dates = course_dates[course_dates.find('<p>')+3:course_dates.find('</p>')]
        course_dates = course_dates.split('<br>')[0]
    
     
    #course info
    course_info = html_text.split('<div class="description color-black  body-text"><p>')[1]
    course_info = course_info.split('<p>')[0]
    course_info = course_info.split('</p>')[0]
    
    #course fees
    course_fees = html_text.split('Price')[-1]
    course_fees = course_fees.split('</strong>')[1]
    course_fees = course_fees.split(' for')[0]
    try:
        course_fees = course_fees.split('$')[1]
        course_fees = "USD " + course_fees
    except:
        course_fees = '-'
    
    #course code
    course_code = '-'
    
    courses[len(courses) + 1] = {}
    courses[len(courses)]['course_title'] = course_title
    courses[len(courses)]['course_info'] = course_info
    courses[len(courses)]['course_fees'] = course_fees
    courses[len(courses)]['course_link'] = address
    courses[len(courses)]['course_code'] = course_code
    courses[len(courses)]['course_dates'] = course_dates
    courses[len(courses)]['course_provider'] = course_provider
    
    
    
#%%close driver and save to .npy
driver.quit()

np.save('courses_dict.npy', courses)


