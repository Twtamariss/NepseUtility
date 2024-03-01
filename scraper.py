import requests
from bs4 import BeautifulSoup

class scrape():
    def __init__(self):
        self.real_address = {}
        self.url = "http://www.nepalstock.com/stocklive"
    
    def refresher(self):
        self.page = requests.get(self.url)
        self.soup = BeautifulSoup(self.page.content, "html.parser")

    def get_content(self,apprent_x,apprent_y):
        rows = (self.soup.find("tbody")).find_all_next('tr')
        columns = rows[apprent_x].find_all_next('td')
        return (columns[apprent_y]).get_text()

    def get_total(self):
        rows = (self.soup.find("tbody")).find_all_next('tr')
        return int (len(rows) - 40)
        

    def refresh_address(self):
        i = 0 
        while (self.get_total() >= i):
            self.real_address[self.get_content(i,1)] = i
            i = i + 1
    

    def refresh(self):
        self.refresher()
        self.refresh_address()
        self.get_total()


    def get_addr(self,symbol):
        return(self.real_address.get(symbol.upper()))