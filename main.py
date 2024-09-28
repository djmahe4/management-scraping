
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import StaleElementReferenceException

def safe_click(driver,result):
    attempts = 0
    while attempts < 3:
        try:
            element = result.find_element(By.TAG_NAME, "a").get_attribute("href")
            return element
        except StaleElementReferenceException:
            attempts += 1
            driver.refresh()


def driver_init():
    chromedriver_path = "D:\chromedriver-win64\chromedriver-win64\chromedriver.exe"

    # Alternatively, use ChromeDriverManager to automatically handle updates
    # chromedriver_path = ChromeDriverManager().install()

    service = Service(chromedriver_path)
    options = Options()
    options.add_argument("--headless")  # Headless mode
    options.add_argument("--disable-gpu")  # Disable GPU acceleration

    driver = webdriver.Chrome(service=service, options=options)
    driver.set_page_load_timeout(10)

    return driver

#url=input("Enter url:")
#if url=="":
    #url = "https://www.flybuys.com.au/"
#parsed_url = urlparse(url)
#domain = parsed_url.netloc.lstrip('www.')
#print(domain)
driver = driver_init()
#queries = ["management team at manchester united"]
while True:
    query=input("Enter query:")
    if query !="":
        #driver.get("https://www.bing.com/search?q="+query.replace(' ', '+').replace(":","%3A"))
        #print("https://www.bing.com/search?q="+query.replace(' ', '+').replace(":","%3A"))
        driver.get('https://www.bing.com')
        time.sleep(5)
        search_box = driver.find_element(By.ID, 'sb_form_q')
        oquery="Management team at "
        oquery=oquery+query
        search_box.send_keys(oquery)
        search_box.submit()
        driver.implicitly_wait(10)

        #print(driver.page_source)
        #break
        results = driver.find_elements(By.CSS_SELECTOR, "li.b_algo")[:10]
        #results = driver.find_elements(By.TAG_NAME, 'a')
        for result in results:
            try:
                link = safe_click(driver,result)#result.find_element(By.TAG_NAME, "a").get_attribute("href")
                print(link)
                break
                #print(result.get_attribute('href'))
            except NoSuchElementException:
                print("No link found in this result.")
        time.sleep(2)
    else:
        driver.close()
        exit(0)
