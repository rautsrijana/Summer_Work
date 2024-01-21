# # import my_selenium_script
# # from my_selenium_script import webdriver

# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By


# # PATH = "/Users/srijanaraut/Desktop/ai_camp/project/chromedriver.exe"

# # webdriver_service = Service("/usr/local/bin/chromedriver.exe")  # Replace with the path to your WebDriver executable
# driver = webdriver.Chrome()

# driver.get('https://www.paly.net/connecting/staff-directory')

# name_elements = driver.find_elements(By.XPATH, "//span[@class='view-name']")
# email_elements = driver.find_elements(By.XPATH, "//a[contains(@href, 'mailto:')]")
# for i in range(len(name_elements)):
#     name = name_elements[i].text
#     email = email_elements[i].get_attribute('href').split(':')[-1]
#     print("Name:", name)
#     print("Email:", email)

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# Set up ChromeDriver in headless mode
options = Options()
options.add_argument("--headless")
driver = webdriver.Chrome(options=options)  # Adjust this line based on your WebDriver setup
driver.get("https://www.paly.net/connecting/staff-directory")

# Find all staff names on the page
names_elements = driver.find_elements(By.CSS_SELECTOR, ".staff-title")

# Extract the names
names = [element.text for element in names_elements]

# Print the extracted names
for name in names:
    print(name)

# Quit the WebDriver
# driver.quit()

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

item_names = []
options = webdriver.ChromeOptions() 
options.add_argument("start-maximized")
options.add_argument('disable-infobars')
driver=webdriver.Chrome(chrome_options=options, executable_path=r'C:\Utility\BrowserDrivers\chromedriver.exe')
driver.get("https://redmart.com/fresh-produce/fresh-vegetables")
titles = WebDriverWait(driver, 5).until(EC.visibility_of_all_elements_located((By.XPATH, "//div[@class='productDescriptionAndPrice']//h4/a")))
for title in titles:
    item_names.append(title.text)
try:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    titles = WebDriverWait(driver, 5).until(EC.visibility_of_all_elements_located((By.XPATH, "//div[@class='productDescriptionAndPrice']//h4/a")))
    for title in titles:
    item_names.append(title.text)
except:
    pass
for item_name in item_names:
    print(item_name)
