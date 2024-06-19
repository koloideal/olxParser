from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException


async def parser(url):

    EXE_PATH = "D:\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe"

    service = Service(executable_path=EXE_PATH)

    opts = Options()

    opts.add_experimental_option("excludeSwitches", ["enable-automation"])
    opts.add_experimental_option('useAutomationExtension', False)
    opts.add_argument("--headless")
    opts.add_argument("window-size=1920,1080")

    driver = webdriver.Chrome(options=opts, service=service)

    driver.get(url)
    time.sleep(3)

    items = driver.find_elements(By.CSS_SELECTOR, ".css-1sw7q4x")

    first_step_list = []

    for item in items:

        try:

            locate_and_date = item.find_element(By.CSS_SELECTOR, ".css-1a4brun").text
            locate = locate_and_date.split("-")[0]
            date = locate_and_date.split("-")[1]
            price = item.find_element(By.CSS_SELECTOR, ".css-tyui9s").text
            alt = item.find_element(By.CSS_SELECTOR, ".css-16v5mdi").text
            link = item.find_element(By.CSS_SELECTOR, ".css-z3gu2d").get_attribute('href')

            first_step_list.append({"title": alt,
                                    "price": price,
                                    'locate': locate,
                                    'date': date,
                                    'link': link})

        except (NoSuchElementException, ElementClickInterceptedException):

            continue

    result_list = []

    for item in first_step_list:

        url = item["link"]

        driver.get(url)
        time.sleep(2)

        try:

            description = driver.find_element(By.CSS_SELECTOR, ".css-1t507yq").text
            author_name = driver.find_element(By.CSS_SELECTOR, ".css-1lcz6o7").text
            on_olx = driver.find_element(By.CSS_SELECTOR, ".css-2zk10x").text
            link_img = driver.find_element(By.CSS_SELECTOR, '.css-1bmvjcs').get_attribute('src')

            driver.find_element(By.CSS_SELECTOR, ".css-1l3tcy7").click()
            time.sleep(2)
            phone = driver.find_element(By.CSS_SELECTOR, ".css-v1ndtc").text

        except NoSuchElementException:

            pass

        try:

            result_list.append({"title": item['title'],
                                "price": item['price'],
                                'locate': item['locate'],
                                'date': item['date'],
                                'link': item['link'],
                                'author_name': author_name,
                                'on_olx': on_olx,
                                'phone': phone,
                                'description': description,
                                'link_img': link_img})

        except UnboundLocalError:

            continue

    return result_list
