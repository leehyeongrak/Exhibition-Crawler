import requests
from bs4 import BeautifulSoup as bs
import json
from selenium import webdriver
import time

# >>> Selenium 크롤링
driver = webdriver.Chrome('/Users/rak/Python/chromedriver')
# >>> 크롬 드라이버 생성 및 데이터의 완전한 로딩을 위한 3초 기다림
driver.implicitly_wait(3)
# >>> url 실행
url = "https://search.naver.com/search.naver?sm=top_hty&fbm=0&ie=utf8&query=%EC%A0%84%EC%8B%9C%ED%9A%8C"
# url = "https://v4.map.naver.com/index.nhn?pinType=site&mapMode=0&pinId=1932056777"
driver.get(url)
time.sleep(1)

# driver.find_element_by_xpath('//*[@id="main_pack"]/div[3]/div/div[2]/div/div[1]/div[5]/ul[1]/li[1]/div[2]/div/a[2]').click()
# a = driver.find_element_by_css_selector('#main_pack > div.content_search.section._art_exhibition_base > div > div.contents03_sub > div > div.info_box.list > div.list_info._list_base > ul:nth-child(1) > li:nth-child(1) > div.item_box > div > a.map')
# for _ in range(58):
#     for i in range(6):
#         ul = str((i+2)//2)
#         li = str(1+(i%2))
#         a = driver.find_element_by_css_selector('#main_pack > div.content_search.section._art_exhibition_base > div > div.contents03_sub > div > div.info_box.list > div.list_info._list_base > ul:nth-child('+ul+') > li:nth-child('+li+') > div.item_box > div > a.map')
#         href = a.get_attribute('href')
#         print(href)
#     driver.find_element_by_css_selector('#main_pack > div.content_search.section._art_exhibition_base > div > div.contents03_sub > div > div.info_box.list > div.page_sec._page_navi > a.next._btn._btn_next.on').click()
#     time.sleep(1)
# # address = driver.find_element_by_css_selector('#naver_map > div.nmap_movable_container > div.nmap_info_pane > div.nmap_infowindow._none_pointer > div > div > div._infowindow_content > div.spotly_container > div.spotly_detail > div > dl > dt')
# # print(address.text)


count = 0
for j in range(58):
    for i in range(6):
        # 전시회 하나 검색
        count += 1
        ul = str((i+2)//2)
        li = str(1+(i%2))

        info = driver.find_element_by_css_selector('#main_pack > div.content_search.section._art_exhibition_base > div > div.contents03_sub > div > div.info_box.list > div.list_info._list_base > ul:nth-child('+ul+') > li:nth-child('+li+')')
        # print(info.text)


        # 지도 없는 전시회는 에러뜸 처리해줘야댐
        if (j == 0):
            a = driver.find_element_by_css_selector('#main_pack > div.content_search.section._art_exhibition_base > div > div.contents03_sub > div > div.info_box.list > div.list_info._list_base > ul:nth-child('+ul+') > li:nth-child('+li+') > div.item_box > div > a.map')
        else:
            a = driver.find_element_by_css_selector('#main_pack > div.content_search.section._art_exhibition_base > div > div.contents03_sub > div > div.info_box.list > div.list_info._list_base > ul:nth-child('+ul+') > li:nth-child('+li+') > div > div.item_box > div > a.map')
        href = a.get_attribute('href')
        print(href)

        # # 이미지 url
        # driver.find_element_by_xpath('//*[@id="main_pack"]/div[3]/div/div[2]/div/div[1]/div[5]/ul['+ul+']/li['+li+']/div[2]/dl/dd[1]/a').click()
        # img = driver.find_element_by_css_selector('#main_pack > div.content_search.section._art_exhibition_base > div > div.contents03_sub > div > div.info_box > div > div.img_box > a > img')
        # print(img.get_attribute('src'))
        # driver.back()
        print('count: '+str(count)+' - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')
    driver.find_element_by_css_selector('#main_pack > div.content_search.section._art_exhibition_base > div > div.contents03_sub > div > div.info_box.list > div.page_sec._page_navi > a.next._btn._btn_next.on').click()
    time.sleep(1)

driver.quit()

#
# def crawlAddress():
#     driver.get(url)
#     address = driver.find_element_by_css_selector('#naver_map > div.nmap_movable_container > div.nmap_info_pane > div.nmap_infowindow._none_pointer > div > div > div._infowindow_content > div.spotly_container > div.spotly_detail > div > dl > dt')
#     print(address.text)
#     driver.quit()
