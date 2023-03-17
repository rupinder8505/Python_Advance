from bs4 import BeautifulSoup
import requests
import csv
class LgExample:
    def __init__(self):
        self.page = requests.get("https://aflcio.org/what-unions-do/social-economic-justice/advocacy/legislative-alerts")
        self.__sp=BeautifulSoup(self.page.text,'html.parser')

    def get_lobbies(self):
        
        rows= self.__sp.find_all("div",class_="view-display-full-listing")
        lobbies=[]
        blocks= rows[0].find_all("a",class_="b-inner")
        for block in blocks:
            title = block.find("h2",class_="content-title").text.strip()
            type = block.find("h5",class_="content-type").text.strip()
            date = block.find("time").text.strip()
            lobyDict= {'type':type,'title':title,'date':date}
            lobbies.append(lobyDict)
        return lobbies

    def save_file(self,lobbies,fileName):
        csv_col = ["type","title","date"]
        fileName = fileName + ".csv"
        with open(fileName,'w') as csvFile:
            writer = csv.DictWriter(csvFile,fieldnames=csv_col)
            writer.writeheader()
            for lobby in lobbies:
                writer.writerow(lobby)