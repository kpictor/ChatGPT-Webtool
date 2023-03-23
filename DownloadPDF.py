import os
import requests
from bs4 import BeautifulSoup

url = 'https://www.massgeneral.org/orthopaedics/sports-medicine/physical-therapy/sports-rehab-protocols' # Replace with the URL of the website you want to download PDFs from
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
pdf_links = soup.find_all('a', href=True)

for link in pdf_links:
    if link['href'].endswith('.pdf'):
        pdf_url = link['href']
        if pdf_url.startswith('/'):
            pdf_url = 'https://www.massgeneral.org' + pdf_url
        filename = os.path.basename(pdf_url)
        with open(filename, 'wb') as f:
            f.write(requests.get(pdf_url).content)