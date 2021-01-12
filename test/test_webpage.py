from bs4 import BeautifulSoup
import pytest
import pickle
import requests


class TestWebpage:
    #@pytest.fixture(autouse=True)
    def get_soup(self):
        source = requests.get("http://127.0.0.1:8000/index.html")
        soup = BeautifulSoup(source.content, 'html.parser')
        return soup

    def test_header(self):
        soup = self.get_soup()
        assert soup.find_all('header')

    def test_footer(self):
        soup = self.get_soup()
        assert soup.find_all('footer') 
                     
    def test_cards(self):
        soup = self.get_soup()
        site = soup.find_all('article', {'class': 'card'})
        count = 0
        for article in site:
                count += 1
        assert count == 6

    def test_card_content(self):
        soup = self.get_soup()
        site = soup.find_all('article', {'class': 'card'})
        count=0
        count1=0
        for img in site:
            count+=1
        for p in site:
            count1 += 1
        assert count==6 & count1>1

    def test_heading(self):
        soup = self.get_soup()
        print(soup)
        site=soup.find('a',{'id':'title'})
        print(site)
        assert site.string=='Explore'

    def test_header_content(self):
        soup = self.get_soup()
        a=0
        site= soup.find('ul', {'class':'home_nav'})
        for p in site.find_all('a'):
            if p.contents[0]=='Home':
                a=a+1;
            if p.contents[0]=='Login':
                a=a+1;
        assert a==2

    def test_sidebar_content(self):
        soup = self.get_soup()
        a=0
        site= soup.find('div', {'class':'side'})
        for p in site.find_all('a'):
            if p.contents[0]=='About':
               a=a+1;
            if p.contents[0]=='Buses':
               a=a+1;
            if p.contents[0]=='Flights':
               a=a+1; 
            if p.contents[0]=='Hotels':
               a=a+1;
            if p.contents[0]=='Contact us':
               a=a+1;
        assert a==5

    def test_footer_content(self):
        soup = self.get_soup()
        a=0
        site= soup.find('ul', {'class':'footer-content'})
        for p in site.find_all('a'):
            if p.contents[0]=='Facebook':
               a=a+1;
            if p.contents[0]=='Instagram':
               a=a+1;
            if p.contents[0]=='Twitter':
                a=a+1
        assert a==3



       
      