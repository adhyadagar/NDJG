from selenium import webdriver
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
import pickle

driver = webdriver.Chrome("/Users/adhyadagar/PycharmProjects/WebCrawler1/Drivers/chromedriver")

site = driver.get("https://njdg.ecourts.gov.in/njdgnew/index.php")

title = driver.title

print(title)

my_url = "https://njdg.ecourts.gov.in/njdgnew/index.php"

#driver.manage().window().maximize()

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

pickle_out = open("P2015b2.pickle","wb")
driver.maximize_window()
for i in range(4, 5):
    element = driver.find_element_by_xpath(
        '//*[@id="report_body"]/tr[' + str(i) + ']/td[1]')
    driver.execute_script("arguments[0].scrollIntoView(true);", element)
    key = driver.find_element_by_xpath('//*[@id="report_body"]/tr[' + str(i) + ']/td[1]').text
    value = driver.find_element_by_xpath('//*[@id="report_body"]/tr[' + str(i) + ']/td[3]/a').text
    time.sleep(3)
    dict[key]=value
    print(dict)
    driver.find_element_by_xpath('//*[@id="report_body"]/tr[' + str(i) + ']/td[3]/a').click()
    for j in range(2, 3): #Year #2014
        try:
            dict1 = {}
            time.sleep(3)
            select = Select(driver.find_element_by_xpath('//*[@id="example_year_length"]/label/select'))
            select.select_by_value('50')
            key1 = driver.find_element_by_xpath(
                '//*[@id="state_report_body"]/tr[' + str(j) + ']/td[1]').text
            value1 = driver.find_element_by_xpath(
                '//*[@id="state_report_body"]/tr[' + str(j) + ']/td[2]/a').text
            Key1 = key + ' - ' + key1
            dict1[Key1] = value1
            dict.update(dict1)
            print(dict)
            driver.find_element_by_xpath('//*[@id="state_report_body"]/tr['+ str(j) +']/td[2]/a').click()
        except Exception as e:
            driver.execute_script("window.scrollTo(0, 0)")
            with wait_for_page_load(driver):
                # time.sleep(10)
                driver.find_element_by_link_text("Back")
            driver.find_element_by_link_text("Back").click()
            break
        for k in range(3, 5): #State
            try:
                dict2 = {}
                time.sleep(3)
                select = Select(driver.find_element_by_xpath('//*[@id="example_state_length"]/label/select'))
                select.select_by_value('50')
                #element = driver.find_element_by_xpath('//*[@id="state_report_body"]/tr[' + str(k) + ']/td[2]/a')
                #driver.execute_script("arguments[0].scrollIntoView(true);", element)
                key2 = driver.find_element_by_xpath('//*[@id="state_report_body"]/tr[' + str(k) + ']/td[1]').text
                value2 = driver.find_element_by_xpath('//*[@id="state_report_body"]/tr[' + str(k) + ']/td[2]/a').text
                Key2 = Key1 + ' - ' + key2
                dict2[Key2] = value2
                dict.update(dict2)
                print(dict)
                #time.sleep(10)
                driver.find_element_by_xpath('//*[@id="state_report_body"]/tr[' + str(k) + ']/td[2]/a').click()
            except Exception as e:
                print(e)
                driver.execute_script("window.scrollTo(0, 0)")
                with wait_for_page_load(driver):
                    # time.sleep(10)
                    driver.find_element_by_link_text("Back")
                driver.find_element_by_link_text("Back").click()
                break
            for l in range(1,101):
                try:
                    dict3 = {}
                    time.sleep(3)
                    select = Select(driver.find_element_by_xpath('//*[@id="example_dist_length"]/label/select'))
                    select.select_by_value('100')
                    key3 = driver.find_element_by_xpath('//*[@id="dist_report_body"]/tr[' + str(l) + ']/td[1]').text
                    value3 = driver.find_element_by_xpath('//*[@id="dist_report_body"]/tr[' + str(l) + ']/td[2]/a').text
                    Key3 = Key2 + ' - ' + key3
                    dict3[Key3] = value3
                    dict.update(dict3)
                    print(dict)
                    #time.sleep(10)
                    driver.find_element_by_xpath('//*[@id="dist_report_body"]/tr[' + str(l) + ']/td[2]/a').click()
                except Exception as e:
                    print("YOYO")
                    driver.execute_script("window.scrollTo(0, 0)")
                    with wait_for_page_load(driver):
                        # time.sleep(10)
                        driver.find_element_by_link_text("Back")
                    driver.find_element_by_link_text("Back").click()
                    break
                for m in range(1,51):
                    try:
                        dict4 = {}
                        time.sleep(3)
                        select = Select(driver.find_element_by_xpath('//*[@id="example_est_length"]/label/select'))
                        select.select_by_value('50')
                        key4 = driver.find_element_by_xpath('//*[@id="est_report_body"]/tr[' + str(m) + ']/td[1]').text
                        value4 = driver.find_element_by_xpath('//*[@id="est_report_body"]/tr[' + str(m) + ']/td[2]/a').text
                        Key4 = Key3 + ' - ' + key4
                        dict4[Key4] = value4
                        dict.update(dict4)
                        print(dict)
                        z = driver.find_element_by_xpath('//*[@id="est_report_body"]/tr[' + str(m) + ']/td[2]/a').text
                        driver.find_element_by_xpath('//*[@id="est_report_body"]/tr[' + str(m) + ']/td[2]/a').click()
                        z = str(z)
                        z = int(z)
                        y = int(z / 100)

                        if z > 0:
                            for o in range(1, y + 2):
                                for n in range(1, 101):
                                    try:
                                        dict5 = {}
                                        time.sleep(3)
                                        select = Select(driver.find_element_by_xpath(
                                            '//*[@id="example_cases_length"]/label/select'))
                                        select.select_by_value('100')
                                        key5 = driver.find_element_by_xpath(
                                            '//*[@id="cases_report_body"]/tr[' + str(n) + ']/td/a').text
                                        value5 = driver.find_element_by_xpath(
                                            '//*[@id="cases_report_body"]/tr[' + str(n) + ']/td/a').text
                                        Key5 = Key4 + ' - ' + key5
                                        dict5[Key5] = value5
                                        dict.update(dict5)
                                        print(dict)
                                        # time.sleep(10)
                                        pickle.dump(dict, pickle_out)
                                    except Exception as e:
                                        driver.execute_script("window.scrollTo(0, 0)")
                                        with wait_for_page_load(driver):
                                            # time.sleep(10)
                                            driver.find_element_by_link_text("Back")
                                        driver.find_element_by_link_text("Back").click()
                                        break
                                with wait_for_page_load(driver):
                                    element = driver.find_element_by_xpath(
                                        '//*[@id="example_cases_next"]')
                                    driver.execute_script("arguments[0].scrollIntoView(true);", element)
                                    driver.find_element_by_xpath('//*[@id="example_cases_next"]').click()
                        else:
                            for n in range(1, 101):
                                try:
                                    dict5 = {}
                                    time.sleep(3)
                                    select = Select(driver.find_element_by_xpath(
                                        '//*[@id="example_cases_length"]/label/select'))
                                    select.select_by_value('100')
                                    key5 = driver.find_element_by_xpath(
                                        '//*[@id="cases_report_body"]/tr[' + str(n) + ']/td/a').text
                                    value5 = driver.find_element_by_xpath(
                                        '//*[@id="cases_report_body"]/tr[' + str(n) + ']/td/a').text
                                    Key5 = Key4 + ' - ' + key5
                                    dict5[Key5] = value5
                                    dict.update(dict5)
                                    print(dict)
                                    # time.sleep(10)
                                    pickle.dump(dict, pickle_out)
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
                            # time.sleep(10)
                            driver.find_element_by_link_text("Back")
                        driver.find_element_by_link_text("Back").click()
                        break






pickle.dump(dict,pickle_out)
pickle_out.close()