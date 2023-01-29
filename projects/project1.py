from threading import main_thread
import requests
import array as arr
import html5lib
from bs4 import BeautifulSoup
def get_expedia_data():
  URL="https://www.expedia.com/Hotel-Search?adults=2&d1=2022-10-06&d2=2022-10-07&destination=Oslo%2C%20Norway%20%28OSL-All%20Airports%29&directFlights=false&endDate=2022-11-09&hotels-destination=Oslo%2C%20Norway%20%28OSL-All%20Airports%29&l10n=%5Bobject%20Object%5D&localDateFormat=M%2Fd%2Fyyyy&partialStay=false&regionId=6139244&semdtl=&sort=RECOMMENDED&startDate=2022-11-08&theme=&useRewards=false&userIntent="
  r=requests.get(URL)

  soup=BeautifulSoup(r.content, 'lxml') 

  main_section = soup.find("section", attrs= {'class':'results'})

  hotels = main_section.find_all("h3", attrs={'class':'uitk-heading uitk-heading-6 is-visually-hidden'})
  hotels_list = []
  for b in hotels[0:]:
      result = b.text.strip()
      hotels_list.append(result)

  prices = main_section.find_all("div", attrs={'class':'uitk-text uitk-type-600 uitk-type-bold uitk-text-emphasis-theme'})
  price_list = []
  for c in prices[0:]:
      result = c.text.strip()
      price_list.append(result)

  ratings = main_section.find_all("span", attrs={'class':'uitk-text uitk-type-300 uitk-type-bold uitk-text-default-theme'})
  ratings_list = []
  for d in ratings[0:]:
      result = d.text.strip()
      ratings_list.append(result)
    
  expedia_list = list(zip(hotels_list,price_list,ratings_list))
  print(expedia_list)

def get_booking_data():
    URL="https://www.booking.com/searchresults.en-us.html?ss=Oslo%2C+Oslo+County%2C+Norway&aid=304142&lang=en-us&sb=1&src_elem=sb&src=searchresults&dest_id=-273837&dest_type=city&ac_position=0&ac_click_type=b&ac_langcode=en&ac_suggestion_list_length=5&search_selected=true&search_pageview_id=0d1a538822020089&ac_meta=GhAwZDFhNTM4ODIyMDIwMDg5IAAoATICZW46BE9zbG9AAEoAUAA%3D&checkin=2022-11-08&checkout=2022-11-09&group_adults=1&no_rooms=1&group_children=0&sb_travel_purpose=leisure"
    r=requests.get(URL)
    soup = BeautifulSoup(r.content, 'html5lib')

    names = soup.find_all("div", attrs= {'class':'fcab3ed991 a23c043802'})
    print(names)


def get_hotels_data():
    URL = "https://www.hotels.com/Hotel-Search?adults=1&d1=2022-11-08&d2=2022-11-09&destination=Oslo%2C%20Norway&endDate=2022-11-09&latLong=59.911936%2C10.746272&regionId=2702&selected=&semdtl=&sort=RECOMMENDED&startDate=2022-11-08&theme=&useRewards=false&userIntent="
    r=requests.get(URL)
    soup = BeautifulSoup(r.content, 'lxml')

    main_section = soup.find("section", attrs={'class':'results'})

    print(main_section)
    hotels = main_section.find_all("h2", attrs={'class':'uitk-heading uitk-heading-5 overflow-wrap'})
    hotels_list = []
    for b in hotels[0:]:
        result = b.text.strip()
        hotels_list.append(result)
    
    #print(hotels_list)

get_expedia_data()
#get_booking_data()
#get_hotels_data()