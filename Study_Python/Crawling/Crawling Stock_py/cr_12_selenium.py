import time
from selenium import webdriver

browser = webdriver.Chrome('~/Downloads/chromedriver.exe')

#naver 열기
browser.get("http://naver.com")

time.sleep(1)
#로그인 버튼 들어가기
elem = browser.find_element_by_class_name("link_login")
elem.click()

time.sleep(1)
#아이디 패스워드 입력
browser.find_element_by_id("id").send_keys("naver_id")
browser.find_element_by_id("pw").send_keys("naver_pw")

time.sleep(1)
#로그인 버튼 클릭
browser.find_element_by_id("log.login").click()

time.sleep(1)

#아이디를 새로 입력
browser.find_element_by_id("id").clear()
browser.find_element_by_id("id").send_keys("my_id")

# html 정보 출력
print(browser.page_source)

time.sleep(1)
# 브라우저 종료
browser.quit()