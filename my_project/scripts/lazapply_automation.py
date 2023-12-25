from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

# Constants for easy configuration and maintenance
LAZYAPPLY_URL = 'https://app.lazyapply.com/dashboard'
USERNAME = 'georgemyself92@gmail.com'

# Path to your Chrome executable
chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe'

# Specify the path to your user data and the profile directory
user_data_dir = 'C:/Users/jagji/AppData/Local/Google/Chrome/User Data'
profile_directory = 'Profile 3'  # Change as per your profile

# Set up Chrome options
options = Options()
options.binary_location = chrome_path
options.add_argument(f"user-data-dir={user_data_dir}")  # Set user data directory
options.add_argument(f"profile-directory={profile_directory}")  # Set profile directory

# Initialize the browser driver
service = Service('C:/WebDrivers/chromedriver.exe')
driver = webdriver.Chrome(service=service, options=options)

# Function to login to the website
def login():
    """Logs into the website using provided credentials."""
    driver.get(LAZYAPPLY_URL)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'nsm7Bb-HzV7m-LgbsSe-BPrWId'))).click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'identifierId'))).send_keys(USERNAME)
    driver.find_element(By.ID, 'identifierNext').click()

# Perform the login
login()

time.sleep(50)

# Close the browser
driver.quit()