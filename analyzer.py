""" Accessibility Analysis Tool"""
import re
import sys
import requests
from bs4 import BeautifulSoup

def get_soup_from_website(url):
    print("checking out " + url)
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    page = requests.get(url, headers = headers)
    soup = BeautifulSoup(page.content, "html.parser")
    return soup

def html_tag_includes_lan(soup, debug=False):
    html_tag = soup.html["lang"]
    if(debug): print("html tag: "); print(html_tag)

def includes_headings(soup, debug=False):
    headings = soup.find_all(re.compile("^h[1-6]$"))
    if debug: print("headings: "); print(headings)
    return len(headings) > 0

def images_include_alt_text(soup, debug=False):
    alt_images = soup.find_all("img", alt=False)
    if debug: print("non-alt images: "); print(alt_images)




# ===============================================================
debug = False
if(len(sys.argv) > 1 and sys.argv[1] == "1"): debug = True


if debug:
    debug_website = "https://landonpalmer.com/489-bio.html"
    soup = get_soup_from_website(debug_website)

    # call methods
    html_tag_includes_lan(soup, 1)
    includes_headings(soup, 1)
    images_include_alt_text(soup, 1)
    exit(0)



URL = input("Enter a website here: ")

accessible_score = 0
accessible_max = 10


if(includes_headings(soup)):
    accessible_score += 1


print("accessible score: ", accessible_score)
