import time
from bs4 import BeautifulSoup
from msedge.selenium_tools import Edge, EdgeOptions

# Define the URL for the "Rehabilitation (Q1)" category
url = 'https://www.scimagojr.com/journalrank.php?category=3612&ranking=q1'

# Set the path to the Edge WebDriver you downloaded
webdriver_path = r'C:\Users\Dicrix\Desktop\msedgedriver.exe'

# Configure Edge WebDriver options
options = EdgeOptions()
options.use_chromium = True

# Create a WebDriver instance and open the URL
driver = Edge(executable_path=webdriver_path, options=options)
driver.get(url)

# Wait for the page to load completely
time.sleep(10)

# Get the page source and parse it using BeautifulSoup
page_source = driver.page_source
soup = BeautifulSoup(page_source, 'html.parser')

# Find the table containing the journal rankings
table = soup.find('table', {'class': 'tabla_datos'})

if table is not None:
    # Extract the journal names and rankings from the table rows
    rows = table.find_all('tr')[1:]  # Skip the header row

    for row in rows:
        columns = row.find_all('td')
        rank = columns[0].text.strip()
        journal_name = columns[1].text.strip()
        print(f'{rank}. {journal_name}')
else:
    print("Table not found. Please check the website and update the code accordingly.")

# Close the WebDriver
driver.quit()
