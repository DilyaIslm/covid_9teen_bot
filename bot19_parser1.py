import requests
from bs4 import BeautifulSoup

class ParserNews:
    def __init__(self):
        self.url = 'https://covid19.rosminzdrav.ru/news/' 
        url = 'https://covid19.rosminzdrav.ru/news/'
        req = requests.get(url).text
        soup = BeautifulSoup(req, 'html.parser')

    def get_img(self):
        url = 'https://covid19.rosminzdrav.ru/news/'
        req = requests.get(url).text
        soup = BeautifulSoup(req, 'html.parser')
        s = soup.find_all("img")
        pic = []
        for element in s:
            pic.append(element.get("src"))
       
        return pic

    def get_href(self):
        url = 'https://covid19.rosminzdrav.ru/news/'
        req = requests.get(url).text
        soup = BeautifulSoup(req, 'html.parser')        
        h = soup.find_all('a')
        head = []
        for element in h:
            head.append(element.get("href")) 
        return head

    def get_time(self):
        url = 'https://covid19.rosminzdrav.ru/news/'
        req = requests.get(url).text
        soup = BeautifulSoup(req, 'html.parser')       
        t = soup.find_all('time')
        time = []
        for element in t:
            time.append(element.text)
             
        return time   
        
    def get_heading(self):
        url = 'https://covid19.rosminzdrav.ru/news/' 
        req = requests.get(url).text
        soup = BeautifulSoup(req, 'html.parser')
        ttl = soup.find_all('a')
        heading = []
        for element in ttl:
            heading.append(element.get("title"))

        return heading    
    def get_samll_cards(self):
        small_cards = []
        time_array = time
        href_array = head
        image_array = pic
        title_array = heading

        for title, href, image, time in zip (title_array, href_array, image_array, time_array):
            one_card = {}
            one_card['title'] = title
            one_card['image'] = image
            one_card['href'] = href
            one_card['time'] = time

            # one_card [{'title':,'image':,'href':,'time':}, {}, {}]

            return small_cards





if __name__ == "__main__":
    ParserCov = ParserNews() 
    pic = ParserCov.get_img() 
    head = ParserCov.get_href()
    time = ParserCov.get_time()
    heading = ParserCov.get_heading()
    small_cards = ParserCov.get_samll_cards()
    print(small_cards)
    # print(pic, head, time, heading) 
      



