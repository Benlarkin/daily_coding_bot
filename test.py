#!/usr/bin/env python3
"""
Module Docstring
"""

__author__ = "Your Name"
__version__ = "0.1.0"
__license__ = "MIT"

# import requests, json
# from bs4 import BeautifulSoup as bs
from selenium import webdriver
from time import sleep
import os

def main():
    #r = requests.get('https://leetcode.com/list/xoqag3yj/')
    # r = requests.post('https://leetcode.com/list/xoqag3yj/', data = {'key':'value'})
    # print(r)
    #print(r.json())
    


    # initialise browser
    browser = webdriver.Chrome(os.getcwd() + '/chromedriver')
    # load page
    browser.get('https://leetcode.com/list/xoqag3yj/')

    # execute java script
    browser.execute_script("return document.getElementsByTagName('html')[0].innerHTML")

    # wait page to load
    sleep(5)

    # get selected content
    problem_description = browser.find_element_by_class_name('question-content__JfgR')
    print(problem_description.text)
    browser.quit()


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
