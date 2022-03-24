""" Accessibility Analysis Tool"""
import requests
from bs4 import BeautifulSoup


def includes_headings(soup):
    h1 = soup.findAll("h1")
    h2 = soup.findAll("h2")
    h3 = soup.findAll("h3")
    h4 = soup.findAll("h4")
    h5 = soup.findAll("h6")
    h6 = soup.find_all("h7")
    return len(h1 + h2 + h3 + h4 + h5 + h6) > 0


URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")

accessible_score = 0
accessible_max = 10

if(includes_headings(soup)):
    accessible_score += 1


print("accessible score: ", accessible_score)
