# WSL : C:\Program Files\VcXsrv xlaunch.exe 실행
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("chromedriver")

# 1. Google Search
#driver.get("https://google.com")
#search_bar = driver.find_element_by_class_name("gLFyf") # textarea
#search_bar.send_keys("hello!")
#search_bar.send_keys(Keys.ENTER)

# 2. Webtoon 클릭
#driver.get("https://naver.com")
#webtoon = driver.find_element_by_css_selector("#shortcutArea > ul > li:nth-child(9) > a")
#webtoon.click()

# 3. 주가 Scrapping
code = "005930"
url = f"https://finance.naver.com/item/main.nhn?code={code}"
driver.get(url)

css_selector = "#aside > div.aside_invest_info"
elem = driver.find_element_by_css_selector(css_selector)
print(elem.text)

# 4. 창 전환
driver.get("https://naver.com")
webtoon = driver.find_element_by_css_selector("#shortcutArea > ul > li:nth-child(9) > a")
webtoon.click()
print(driver.window_handles)
driver.switch_to.window(driver.window_handles[1]) # 새 창 webtoon으로 바꾸어주어야 한다.
search = driver.find_element_by_class_name("SearchBar__search_input--k5nfk")
search.send_keys("가담항설")
search.send_keys(Keys.ENTER)

driver.implicitly_wait(3)
gadam = driver.find_element_by_css_selector("#content > div.component_wrap.type0 > ul > li:nth-child(1) > div > a")
gadam.click()
#driver.to_switch(driver.window_handles[1])

# Screenshot
