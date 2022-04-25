""" Accessibility Analysis Tool"""
import re
import sys
import requests
from bs4 import BeautifulSoup


''' DOCSTRING:

DESCRIPTION:
    Welcome to this prototype for analyzing website accessibility!
    This script will use webscraping to analyze the DOM of a given site.
    It will consider the following criteria:
        1. Whether or not the <html> tag includes the 'lan' attribute (for translating screen readers)
        2. Whether or not headings [any <h1>...<h6>] are included in content (for screen reader organization)
        3. Whether or not all included images have alt text (also screen readers/visually impaired)
    Enter a URL to see the results of this analysis! See usage below.

USAGE:
    `python analyzer.py 0` for regular usage, prompted for URL (including surrounding quotes [sorry, lazy])
    `python analyzer.py 1` for ~debug~ that polls my personal accessible(ish) website
    OUTPUT is printed object in form of `('HAS HTML LAN: {T/F}', 'HAS HEADINGS: {T/F}', 'HAS ALT TEXT: {T/F}')`

Enjoy :D
'''


def get_soup_from_website(url):
    print("checking out " + url)
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    page = requests.get(url, headers = headers)
    soup = BeautifulSoup(page.content, "html.parser")
    return soup

def html_tag_includes_lan(soup, debug=False):
    html_tag = soup.html
    if(debug): print("html tag: "); print(html_tag)
    return html_tag.has_attr("lang")

def includes_headings(soup, debug=False):
    headings = soup.find_all(re.compile("^h[1-6]$"))
    if debug: print("headings: "); print(headings)
    return len(headings) > 0

def images_include_alt_text(soup, debug=False):
    alt_images = soup.find_all("img", alt=False)
    if debug: print("non-alt images: "); print(alt_images); print(type(alt_images))
    for img in alt_images: # quick workaround for bs4.resultset
        return False
    return True

# ===============================================================

debug = False
if(len(sys.argv) > 1 and sys.argv[1] == "1"): debug = True


if debug:
    debug_website = "https://landonpalmer.com/489-bio.html"
    soup = get_soup_from_website(debug_website)

    # call methods
    print(html_tag_includes_lan(soup, 1))
    includes_headings(soup, 1)
    images_include_alt_text(soup, 1)
    exit(0)

else:
    class AccessibilityReport:

        def __init__(self, u = "NO URL", l=False, h=False, a=False):
            self.url = u
            self.html_includes_lan_attribute = l
            self.content_includes_headings = h
            self.images_include_alt_text = a

        def get_data(self):
            print("RESULTS FOR: " + self.url)
            print(
                "HAS HTML LAN: " + str(self.html_includes_lan_attribute), 
                "HAS HEADINGS: " + str(self.content_includes_headings), 
                "HAS ALT TEXT: " + str(self.images_include_alt_text)
            )


    url = input("Enter a website in quotes: ")
    soup = get_soup_from_website(url)
    lan = html_tag_includes_lan(soup)
    headings = includes_headings(soup)
    alt = images_include_alt_text(soup)
    result = AccessibilityReport(url, lan, headings, alt)

    result.get_data()


