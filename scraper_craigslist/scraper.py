__author__ = 'johnson'

import requests
from bs4 import BeautifulSoup
from pprint import pprint
from urlparse import urljoin

## scrapes craigslist for apt in portland that are under $1500 in rent


BASE_URL = 'http://portland.craigslist.org/search/apa/mlt?zoomToPosting=&catAbb=apa&query=&minAsk=&maxAsk=1500&bedrooms=&housing_type=&excats='

def scrape_apts():
    response = requests.get(BASE_URL)

    # parse HTML using Beautiful Soup
    soup = BeautifulSoup(response.content)

    # find all the posts in the page.
    apts = soup.find_all('span', {'class':'pl'})

    # Get all the links:
    for apt in apts:
        link = apt.find('a').attrs['href']

        # join this relative link with the
        # BASE_URL to create an absolute link
        url = urljoin(BASE_URL, link)

        scrape_apt(url)

def scrape_apt(url):
    """ Extract information from a apt page. """

    response = requests.get(url)

    # Parse the html of the  post
    soup = BeautifulSoup(response.content)

    # Extract the actual contents of some HTML elements:
    data = {
        'source_url': url,
        'subject': soup.find('h2', {'class':'postingtitle'}).text.strip(),
 #       'body': soup.find('section', {'id':'postingbody'}).text.strip(),
 #       'datetime': soup.find('time').attrs['datetime']
    }

    # Print it prettily.
    pprint(data)

if __name__ == '__main__':
    scrape_apts()