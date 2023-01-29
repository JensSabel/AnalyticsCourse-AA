import csv
from lib2to3.pgen2 import driver
from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome("C:\Webdrivers\chromedriver.exe")
url = "https://www.booking.com/searchresults.en-us.html?ss=Oslo%2C+Oslo+County%2C+Norway&aid=304142&lang=en-us&sb=1&src_elem=sb&src=searchresults&dest_id=-273837&dest_type=city&ac_position=0&ac_click_type=b&ac_langcode=en&ac_suggestion_list_length=5&search_selected=true&search_pageview_id=0d1a538822020089&ac_meta=GhAwZDFhNTM4ODIyMDIwMDg5IAAoATICZW46BE9zbG9AAEoAUAA%3D&checkin=2022-11-08&checkout=2022-11-09&group_adults=1&no_rooms=1&group_children=0&sb_travel_purpose=leisure"
driver.get(url)

def get_url(search_term):
    template = "https://www.booking.com/searchresults.en-us.html?ss="
    search_term = search_term.replace(" ", "+")
    return template.format(search_term)

soup = BeautifulSoup(driver.page_source, "1xm1")
listings = soup.find_all