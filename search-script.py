from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36")

path = Service(ChromeDriverManager().install())
browser = webdriver.Chrome(service=path, options=options)

link = "https://google.com/"
browser.get(link)

# Wait for the search input field to load
search_input = browser.find_element(By.NAME, "q")


search_input.send_keys("my")
search_input.send_keys(Keys.RETURN)

links = []
for i in range(1, 11):
    try:
        link = browser.find_element_by_xpath(f'//*[@id="rso"]/div[{i}]/div/div[1]/a')
        links.append(link.get_attribute('href'))
    except:
        pass

browser.quit()
# Write links to a text file
with open('search_results.txt', 'w') as f:
    for link in links:
        f.write(link + '\n')

print(links)
