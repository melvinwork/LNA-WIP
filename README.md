# Webscraping Code for LNA Course Repository

## Overview
This repository consists of code that crawls for online course information using Selenium. The database used for storing the information is SQLite.
To get updated course information such as course dates and fees, run the python code "web_scrape.py" to crawl for updated info. The info will be saved to a python dictionary "course_dict.npy". Next, run "update_repo.py" to update the database with the crawled info.

*Note: chromedriver.exe with the matching version with the installed chrome browser must be in this folder for Selenium to work.

The crawler currently works for the following course websites:
- NUS ISS
- SMU
- SP
- Nvidia

## Items in this repository
- create_repo.py - code to create the sqlite database for storing info
- repo_to_excel.py - code to export info from database to excel file
- update_repo.py - run this code to update database with info such as coures fees, dates
- web_scrape.py - run this code to scrape all the websites links in the .txt files
- course_repo.db - sqlite database for storing course info
- course_repo.xlsx - database info exported as excel file
- course_dict.npy - python dictionary for storing crawled course info before updating database
- chromedriver.exe - required chrome webdriver for selenium (driver version must be the same as chrome browser version)
- links_nus_iss.txt - website links for courses from NUS ISS
- links_nvidia.txt - website links for courses from Nvidia
- links_smu.txt - website links for courses from SMU
- links_sp.txt - website links for course from SP
