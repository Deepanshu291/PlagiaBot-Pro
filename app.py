
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
import random
import string



DirectoryName = 'Data'  #'Write your directory name here where you want to save pdf'
Projectfilepath = 'project.txt' #'write your file path here'

def genrate_emailandusername():
    letters = string.ascii_lowercase
    username = ''.join(random.choice(letters) for _ in range(10))
    email = username + "@gmail.com"
    print("Username:", username, "Email:", email)
    return username, email

def register(driver):
    driver.get("https://plagiarisma.net/register.php")  # Open the Plagiarisma website
    driver.implicitly_wait(100)  # Wait for the page to load
    UserName, Email = genrate_emailandusername()
    username = driver.find_element(By.XPATH, '//*[@id="name"]')
    username.clear()
    username.send_keys(UserName)  # Enter your username

    email = driver.find_element(By.XPATH, '//*[@id="email"]')
    email.clear()
    email.send_keys(Email)  # Enter your email address

    password = driver.find_element(By.XPATH, '//*[@id="password"]')
    password.clear()
    password.send_keys(Email)  # Enter your password

    signupbtn = driver.find_element(By.XPATH, '//*[@id="regForm"]/div[5]/input')
    signupbtn.click()  # Click the "Sign Up" button
    time.sleep(2)

def logout(driver):
    driver.get('https://plagiarisma.net/logout.php')
    print('Logout Successfully')
    time.sleep(2)

# def login(driver):  
#     driver.get("https://plagiarisma.net/login.php")  # Open the Plagiarisma website
#     driver.implicitly_wait(100)  # Wait for the page to load

#     email = driver.find_element(By.NAME, "email")
#     email.clear()
#     email.send_keys(EmailnPassword)  # Enter your email address

#     password = driver.find_element(By.NAME, "password")
#     password.clear()
#     password.send_keys(EmailnPassword)  # Enter your password

#     rememberclick = driver.find_element(By.NAME, "remember")
#     rememberclick.click()  # Click the "Remember Me" checkbox

#     signbtn = driver.find_element(By.XPATH, '//*[@id="regForm"]/input[3]')
#     signbtn.click()  # Click the "Sign In" button
#     time.sleep(2)

def postanddownload(driver, text):
    driver.get("https://plagiarisma.net/")  # Open the Plagiarisma website
    
    queryfield = driver.find_element(By.NAME, "query")
    queryfield.clear()
    queryfield.send_keys(text)  # Enter the text to check for plagiarism

    check_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "Submit")))

    # Retry clicking in case of an intercepting element
    attempts = 0
    while attempts < 3:
        try:
            check_button.click()  # Try to click the "Check Plagiarism" button
            break  # Exit the loop if successful
        except Exception as e:
            print(f"Click intercepted, attempt {attempts + 1}: {e}")
            time.sleep(2)  # Wait and retry
            attempts += 1

    WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH, '//*[@id="plagiarism"]')))
    
    # download_button = driver.find_element(By.XPATH, '//*[@id="plagiarism"]/div[3]/div/form/div/button')
    download_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="plagiarism"]/div[3]/div/form/div/button')))
    while attempts < 3:
        try:
            download_button.click()  # Click the "Download Report" button
            break
        except Exception as e:
            print(f"Click intercepted, attempt {attempts + 1}: {e}")
            time.sleep(2)
            attempts += 1

    print('Pdf Download Successfully')


# def postanddownload(driver,text):

#     driver.get("https://plagiarisma.net/")  # Open the Plagiarisma website
    
#     queryfield = driver.find_element(By.NAME, "query")

#     queryfield.clear()
#     queryfield.send_keys(text)  # Enter the text to check for plagiarism
#     # time.sleep(3)
#     check_button = driver.find_element(By.NAME, "Submit")
#     check_button.click()  # Click the "Check Plagiarism" button

#     downloadpdf = WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH, '//*[@id="plagiarism"]')))  # Wait for the report to load
#     # if downloadpdf:
#     download_button = driver.find_element(By.XPATH, '//*[@id="plagiarism"]/div[3]/div/form/div/button')
#     download_button.click()  # Click the "Download Report" button
#     # else:
#     #     print('Registring new user')

# # report_content = driver.find_element(By.ID, "plagiarism").text  # Get the report content
#     print('Pdf Download Successfully')

# Function to split the text into chunks of 500 words
def split_text_into_chunks(text, chunk_size=70):
    words = text.split()
    chunks = [words[i:i + chunk_size] for i in range(0, len(words), chunk_size)]
    return [' '.join(chunk) for chunk in chunks]

def get_text_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()
    
def create_directory(filename):
    data_directory = os.getcwd()+'\\'+filename
    if not os.path.exists(data_directory):
        os.makedirs(data_directory)
    return data_directory

if __name__ == "__main__":
    
    # file_path = 'project.txt'  # Specify the path to your input text file
    text = get_text_from_file(Projectfilepath)

    chunks = split_text_into_chunks(text)

    chrome_options = Options()
    # chrome_options.add_argument("--headless")  # Run in headless mode (no browser UI)
    chrome_options.add_experimental_option("prefs", {
        "download.default_directory": create_directory(filename=DirectoryName),  # Set default download directory to current working directory
        "download.prompt_for_download": False,  # Disable the prompt for download
        "download.directory_upgrade": True
    })


    # Automatically download and use the correct version of ChromeDriver
    driverFilepath = os.getcwd() + '\\drivers\\chromedriver.exe'
    service = Service(driverFilepath)

    # Start the WebDriver (e.g., Chrome)
    driver = webdriver.Chrome(service=service, options=chrome_options)

    # login(driver)
    register(driver)
    # formplag = driver.find_element(By.XPATH, '//*[@id="splash"]/div/div/div[1]/div/div/div[1]')
    chunkquanter = 0
    for i, chunk in enumerate(chunks, start=1):
        print(f"Processing chunk {i}/{len(chunks)}...")
        postanddownload(driver,chunk)
        chunkquanter += 1
        if chunkquanter == 4:
            print('Processing 4 chunks now logout and register new user')
            logout(driver)
            register(driver)
            chunkquanter = 0

    driver.quit()  # Close the browser

# time.sleep(100)  # Wait for the page to load
    password.clear()
    password.send_keys(Email)  # Enter your password

    signupbtn = driver.find_element(By.XPATH, '//*[@id="regForm"]/div[5]/input')
    signupbtn.click()  # Click the "Sign Up" button
    time.sleep(2)

def logout(driver):
    driver.get('https://plagiarisma.net/logout.php')
    print('Logout Successfully')
    time.sleep(2)

# def login(driver):  
#     driver.get("https://plagiarisma.net/login.php")  # Open the Plagiarisma website
#     driver.implicitly_wait(100)  # Wait for the page to load

#     email = driver.find_element(By.NAME, "email")
#     email.clear()
#     email.send_keys(EmailnPassword)  # Enter your email address

#     password = driver.find_element(By.NAME, "password")
#     password.clear()
#     password.send_keys(EmailnPassword)  # Enter your password

#     rememberclick = driver.find_element(By.NAME, "remember")
#     rememberclick.click()  # Click the "Remember Me" checkbox

#     signbtn = driver.find_element(By.XPATH, '//*[@id="regForm"]/input[3]')
#     signbtn.click()  # Click the "Sign In" button
#     time.sleep(2)

def postanddownload(driver, text):
    driver.get("https://plagiarisma.net/")  # Open the Plagiarisma website
    
    queryfield = driver.find_element(By.NAME, "query")
    queryfield.clear()
    queryfield.send_keys(text)  # Enter the text to check for plagiarism

    check_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "Submit")))

    # Retry clicking in case of an intercepting element
    attempts = 0
    while attempts < 3:
        try:
            check_button.click()  # Try to click the "Check Plagiarism" button
            break  # Exit the loop if successful
        except Exception as e:
            print(f"Click intercepted, attempt {attempts + 1}: {e}")
            time.sleep(2)  # Wait and retry
            attempts += 1

    WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH, '//*[@id="plagiarism"]')))
    
    # download_button = driver.find_element(By.XPATH, '//*[@id="plagiarism"]/div[3]/div/form/div/button')
    download_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="plagiarism"]/div[3]/div/form/div/button')))
    while attempts < 3:
        try:
            download_button.click()  # Click the "Download Report" button
            break
        except Exception as e:
            print(f"Click intercepted, attempt {attempts + 1}: {e}")
            time.sleep(2)
            attempts += 1

    print('Pdf Download Successfully')


# def postanddownload(driver,text):

#     driver.get("https://plagiarisma.net/")  # Open the Plagiarisma website
    
#     queryfield = driver.find_element(By.NAME, "query")

#     queryfield.clear()
#     queryfield.send_keys(text)  # Enter the text to check for plagiarism
#     # time.sleep(3)
#     check_button = driver.find_element(By.NAME, "Submit")
#     check_button.click()  # Click the "Check Plagiarism" button

#     downloadpdf = WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH, '//*[@id="plagiarism"]')))  # Wait for the report to load
#     # if downloadpdf:
#     download_button = driver.find_element(By.XPATH, '//*[@id="plagiarism"]/div[3]/div/form/div/button')
#     download_button.click()  # Click the "Download Report" button
#     # else:
#     #     print('Registring new user')

# # report_content = driver.find_element(By.ID, "plagiarism").text  # Get the report content
#     print('Pdf Download Successfully')

# Function to split the text into chunks of 500 words
def split_text_into_chunks(text, chunk_size=70):
    words = text.split()
    chunks = [words[i:i + chunk_size] for i in range(0, len(words), chunk_size)]
    return [' '.join(chunk) for chunk in chunks]

def get_text_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()
    
def create_directory(filename):
    data_directory = os.getcwd()+'\\'+filename
    if not os.path.exists(data_directory):
        os.makedirs(data_directory)
    return data_directory

if __name__ == "__main__":
    
    # file_path = 'project.txt'  # Specify the path to your input text file
    text = get_text_from_file(Projectfilepath)

    chunks = split_text_into_chunks(text)

    chrome_options = Options()
    # chrome_options.add_argument("--headless")  # Run in headless mode (no browser UI)
    chrome_options.add_experimental_option("prefs", {
        "download.default_directory": create_directory(filename=DirectoryName),  # Set default download directory to current working directory
        "download.prompt_for_download": False,  # Disable the prompt for download
        "download.directory_upgrade": True
    })


    # Automatically download and use the correct version of ChromeDriver
    driverFilepath = os.getcwd() + '\\drivers\\chromedriver.exe'
    service = Service(driverFilepath)

    # Start the WebDriver (e.g., Chrome)
    driver = webdriver.Chrome(service=service, options=chrome_options)

    # login(driver)
    register(driver)
    # formplag = driver.find_element(By.XPATH, '//*[@id="splash"]/div/div/div[1]/div/div/div[1]')
    chunkquanter = 0
    for i, chunk in enumerate(chunks, start=1):
        print(f"Processing chunk {i}/{len(chunks)}...")
        postanddownload(driver,chunk)
        chunkquanter += 1
        if chunkquanter == 4:
            print('Processing 4 chunks now logout and register new user')
            logout(driver)
            register(driver)
            chunkquanter = 0

    driver.quit()  # Close the browser

# time.sleep(100)  # Wait for the page to load
