import time

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def get_toss_data(keyword):
    # 1. 메인페이지 받아오기
    url = 'https://tossinvest.com/'

    # 2. 크롬 옵션 객체 생성
    options = webdriver.ChromeOptions()
    # options.add_argument("headless")
    options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"
    )
    # 자동화 탐지 우회 옵션 추가
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)
    options.add_argument("disable-blink-features=AutomationControlled")

    # 3) Service 객체를 통해 크롬 드라이버 실행
    service = Service(
        ChromeDriverManager().install()  # ChromeDriverManager를 사용하여 드라이버 자동 설치
    )
    driver = webdriver.Chrome(service=service, options=options)

    # 4) url로 이동하기
    driver.get(url)

    # 페이지 로딩 대기
    time.sleep(5)

    # 5) 검색창 찾기
    # 5-1) 검색창 누르기
    search_button = driver.find_element(By.CSS_SELECTOR, '.u09klc0')
    search_button.click()
    time.sleep(2)

    # 5-2) 검색하기
    search_input = driver.find_element(By.CSS_SELECTOR, "input._1x1gpvi6[placeholder='검색어를 입력해주세요']")
    search_input.send_keys(keyword)
    search_input.send_keys(Keys.RETURN)
    time.sleep(2)


    




get_toss_data('삼성전자')