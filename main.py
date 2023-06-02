from bs4 import BeautifulSoup
import requests

urls = ["https://en.wikipedia.org/wiki/Pakistanis_in_Spain", "https://en.wikipedia.org/wiki/British_Pakistanis"]

code_word = 'Pakistan'  # Code word to search for

for url in urls:
    response = requests.get(url)
    html_content = response.content

    soup = BeautifulSoup(html_content, 'html.parser')

    # Find all paragraphs on the Wikipedia page
    paragraphs = soup.find_all('p')

    # Loop through paragraphs and search for the code word
    for paragraph in paragraphs:
        if code_word in paragraph.get_text():
            print(f"{url} - {paragraph.get_text()}")
