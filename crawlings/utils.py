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
    
    
    # print(driver.current_url)     # https://tossinvest.com/stocks/A005930/order
    stock_code = driver.current_url.split('/')[-2]
    # print(stock_code)
    community_url = 'https://tossinvest.com/stocks/'+stock_code+'/community'
    # print(community_url)        # https://tossinvest.com/stocks/A005930/community
    keyword,stock_code,content = get_community_data(community_url,stock_code)
    
    return keyword,stock_code,content


def get_community_data(url,stock_code):
    
    # 2) 크롬 옵션 객체 생성
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

    # 4) 구글 검색 결과 페이지로 이동
    driver.get(url)
    
    # 페이지 로딩 대기
    time.sleep(2)

    # 5) 페이지의 HTML 소스 가져오기
    html = driver.page_source

    # 6) BeautifulSoup 객체 생성(파서: html.parser)
    soup = BeautifulSoup(html, "html.parser")
    

    # 7) 검색 결과에서 제목 추출
    results = soup.select("div._1p19xcx1")
    # print(results)
    content = []  # 결과 제목을 저장할 리스트
    
    # for i in range(10):
    #     contents = result.
    for result in results:
        spans = result.find_all('span',class_="tw-1r5dc8g0 _60z0ev1 _60z0ev6 _60z0ev0 _1tvp9v41 _1sihfl60")    
        for span in spans:
            text = span.get_text(strip=True)
            if text:
                content.append(text)
   
    keyword_element = soup.select('div._1sivumi0')[0].select_one('span.tw-1r5dc8g0')
    keyword = keyword_element.get_text()

    

   
    driver.quit()
    
    return keyword,stock_code,content

