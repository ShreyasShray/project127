from bs4 import BeautifulSoup
import requests
import csv
import time

Start_url = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
page = requests.get(Start_url)
soup_object = BeautifulSoup(page.contents, "html.parser")
headers = ["name", "distance", "mass", "radius"]
time.sleep(6)
planet_data = []

def scrapper():
    for tr_tag in soup_object.find_all("tr"):
        temp_list = []
        td_tags = tr_tag.find_all("td")
        for index, td_tag in enumerate(td_tags):
            if(index == 1):
                temp_list.append(td_tag.find_all("a")[0].contents[0])
            elif(index == 3):
                temp_list.append(td_tag.contents[0])
            elif(index == 5):
                temp_list.append(td_tag.contents[0])
            elif(index == 6):
                temp_list.append(td_tag.contents[0])
            else:
                    try:
                        temp_list.append(td_tag.contents[0])
                    except:
                        temp_list.append("")

        planet_data.append(temp_list)

    with open("scrapper_2.csv", "w") as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(headers)
        csvwriter.writerows(planet_data)

scrapper()