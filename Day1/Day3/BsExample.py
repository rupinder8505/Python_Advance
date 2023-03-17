from bs4 import BeautifulSoup
import urllib.request as rq
import csv

class BsExample:
    def __init__(self):
        self.r = rq.urlopen("https://realpython.github.io/fake-jobs/")
        self.__sp = BeautifulSoup(myFile,'html.parser')

    def get_jobs(self):
        jobs=[]
        results=self.__sp.find(id="ResultsContainer")
        jobs_elem= results.find_all("div",class_="card-content")
        for job_elem in jobs_elem:
            title = job_elem.find("h2",class_="title is-5").text.strip()
            subtitle = job_elem.find("h3",class_="subtitle is-6 company").text.strip()
            location = job_elem.find("p",class_="location").text.strip()
            date = job_elem.find("time").text.strip()
            jobs=jobs+ [{"title":title,"subtitle":subtitle,"location":location,"date":date}]
            print("title:"+title+"\nsubtitle:"+subtitle+"\nlocation:"+location+"\ndate:"+date)
            print("===")
        return jobs

    def save_file(self,jobs,fileName):
        csv_col = ["title","subtitle","location","date"]
        fileName = fileName + ".csv"
        with open(fileName,'w') as csvFile:
            writer = csv.DictWriter(csvFile,fieldnames=csv_col)
            writer.writeheader()
            for job in jobs:
                writer.writerow(job)



