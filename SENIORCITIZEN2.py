from selenium import webdriver
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common import action_chains, keys
import time
import random
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
import pickle

driver = webdriver.Chrome("/Users/adhyadagar/PycharmProjects/WebCrawler1/Drivers/chromedriver")

site = driver.get("https://njdg.ecourts.gov.in/njdgnew/index.php")

title = driver.title

print(title)

my_url = "https://njdg.ecourts.gov.in/njdgnew/index.php"


class wait_for_page_load(object):

    def __init__(self, browser):
        self.browser = browser

    def __enter__(self):
        self.old_page = self.browser.find_element_by_tag_name('html')

    def page_has_loaded(self):
        new_page = self.browser.find_element_by_tag_name('html')
        return new_page.id != self.old_page.id

    def __exit__(self, *_):
        wait_for_page_load(self.page_has_loaded)



dict = {}

pickle_out = open("Trial.pickle","wb")




driver.maximize_window()
#WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="report_body"]/tr[25]/td[1]')))
key = driver.find_element_by_xpath('//*[@id="report_body"]/tr[25]/td[1]').text
value = driver.find_element_by_xpath('//*[@id="report_body"]/tr[25]/td[3]/a').text
time.sleep(3)
dict[key]=value
print(dict)
driver.find_element_by_xpath('//*[@id="report_body"]/tr[25]/td[3]/a').click()
for i in range(11,13):
    try:
        dict1 = {}
        time.sleep(3)
        select = Select(driver.find_element_by_xpath('//*[@id="example_CitizenState_length"]/label/select'))
        select.select_by_value('50')
        key1 = driver.find_element_by_xpath('//*[@id="CitizenState_body"]/tr['+ str(i) +']/td[1]').text
        value1 = driver.find_element_by_xpath('//*[@id="CitizenState_body"]/tr['+ str(i) +']/td[2]/a').text
        Key1 = key + ' - ' + key1
        dict1[Key1] = value1
        dict.update(dict1)
        print(dict)
        driver.find_element_by_xpath('//*[@id="CitizenState_body"]/tr[' + str(i) + ']/td[2]/a').click()
    except Exception as e:
        driver.execute_script("window.scrollTo(0, 0)")
        with wait_for_page_load(driver):
            driver.find_element_by_link_text("Back")
        driver.find_element_by_link_text("Back").click()
        #element = WebDriverWait(driver, 10).until(
            #EC.visibility_of_element_located((By.XPATH, '//*[@id="citizen_stateDetails_tab"]/a')))
        #element.click()
        #driver.find_element_by_xpath('//*[@id="citizen_stateDetails_tab"]/a').click()
        break
    for j in range(1, 12):
        try:
            dict2 = {}
            time.sleep(3)
            select = Select(driver.find_element_by_xpath('//*[@id="example_Citizendist_length"]/label/select'))
            select.select_by_value('50')
            key2 = driver.find_element_by_xpath('//*[@id="Citizendist_body"]/tr['+ str(j) +']/td[1]').text
            value2 = driver.find_element_by_xpath('//*[@id="Citizendist_body"]/tr['+ str(j) +']/td[2]/a').text
            Key2 = Key1 + ' - ' + key2
            dict2[Key2] = value2
            dict.update(dict2)
            print(dict)
            #time.sleep(10)
            driver.find_element_by_xpath('//*[@id="Citizendist_body"]/tr['+ str(j) +']/td[2]/a').click()
        except Exception as e:
            driver.execute_script("window.scrollTo(0, 0)")
            with wait_for_page_load(driver):
                driver.find_element_by_link_text("Back")
            driver.find_element_by_link_text("Back").click()
            #driver.find_element_by_xpath('//*[@id="citizen_distDetails_tab"]/a').click()
            break
        for k in range(1,51):
            try:
                dict3 = {}
                time.sleep(3)
                select = Select(driver.find_element_by_xpath('//*[@id="example_citizenest_length"]/label/select'))
                select.select_by_value('50')
                key3 = driver.find_element_by_xpath('//*[@id="citizenest_body"]/tr['+ str(k) +']/td[1]').text
                value3 = driver.find_element_by_xpath('//*[@id="citizenest_body"]/tr['+ str(k) +']/td[2]/a').text
                Key3 = Key2 + ' - ' + key3
                dict3[Key3] = value3
                dict.update(dict3)
                print(dict)
                time.sleep(10)
                z = value3 = driver.find_element_by_xpath('//*[@id="citizenest_body"]/tr['+ str(k) +']/td[2]/a').text
                driver.find_element_by_xpath('//*[@id="citizenest_body"]/tr['+ str(k) +']/td[2]/a').click()
                z = str(z)
                z = int(z)
                y = int(z/100)
                if z > 100:
                    for w in range(1,y+2):
                        for l in range(1, 101):
                            try:
                                dict4 = {}
                                time.sleep(3)
                                select = Select(driver.find_element_by_xpath('//*[@id="example_citizencase_length"]/label/select'))
                                select.select_by_value('100')
                                # driver.find_element_by_xpath(('// *[ @ id = "example_regnoWise_caseDetails_next"]').click
                                key4 = driver.find_element_by_xpath('//*[@id="citizencase_body"]/tr[' + str(l) + ']/td/a').text
                                value4 = driver.find_element_by_xpath('//*[@id="citizencase_body"]/tr[' + str(l) + ']/td/a').text
                                Key4 = Key3 + ' - ' + key4
                                dict4[Key4] = value4
                                dict.update(dict4)
                                print(dict)
                            except Exception as e:
                                driver.execute_script("window.scrollTo(0, 0)")
                                with wait_for_page_load(driver):
                                    # time.sleep(10)
                                    driver.find_element_by_link_text("Back")
                                driver.find_element_by_link_text("Back").click()
                                break
                        with wait_for_page_load(driver):
                            driver.find_element_by_xpath('//*[@id="example_citizencase_next"]').click()
                else:
                    for l in range(1, 101):
                        try:
                            dict4 = {}
                            time.sleep(3)
                            select = Select(
                                driver.find_element_by_xpath('//*[@id="example_citizencase_length"]/label/select'))
                            select.select_by_value('100')
                            # driver.find_element_by_xpath(('// *[ @ id = "example_regnoWise_caseDetails_next"]').click
                            key4 = driver.find_element_by_xpath(
                                '//*[@id="citizencase_body"]/tr[' + str(l) + ']/td/a').text
                            value4 = driver.find_element_by_xpath(
                                '//*[@id="citizencase_body"]/tr[' + str(l) + ']/td/a').text
                            Key4 = Key3 + ' - ' + key4
                            dict4[Key4] = value4
                            dict.update(dict4)
                            print(dict)
                        except Exception as e:
                            driver.execute_script("window.scrollTo(0, 0)")
                            with wait_for_page_load(driver):
                                # time.sleep(10)
                                driver.find_element_by_link_text("Back")
                            driver.find_element_by_link_text("Back").click()
                            break
            except Exception as e:
                driver.execute_script("window.scrollTo(0, 0)")
                with wait_for_page_load(driver):
                    driver.find_element_by_link_text("Back")
                driver.find_element_by_link_text("Back").click()
                break





pickle.dump(dict,pickle_out)
pickle_out.close()