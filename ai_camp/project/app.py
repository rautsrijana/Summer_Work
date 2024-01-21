
# Using beautiful soup
import requests
from bs4 import BeautifulSoup

# URL of the South Dakota Department of Education website
url = "https://doe.sd.gov/ofm/edudir.aspx#"

# Send a GET request to the website
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# Find specific elements on the website
# Example: Extracting links of schools
school_links = []
school_menu = soup.find('ul', id= 'ulPublic')
if school_menu:
    school_items = school_menu.find_all('a', href=True)
    school_links = [link['href'] for link in school_items]

# Print the extracted school links
for link in school_links:
    print(link)
