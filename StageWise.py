from selenium import webdriver
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
import pickle

driver = webdriver.Chrome("/Users/adhyadagar/PycharmProjects/WebCrawler1/Drivers/chromedriver")

site = driver.get("https://njdg.ecourts.gov.in/njdgnew/index.php")

title = driver.title
driver.execute_script("window.scrollTo(0, 0)")
print(title)

my_url = "https://njdg.ecourts.gov.in/njdgnew/index.php"
driver.maximize_window()
dict = {}


pickle_out = open("P4.pickle","wb")

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


for i in range(19, 20):
    try:
        #WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="report_body"]/tr[' + str(i) + ']/td[1]')))
        element = driver.find_element_by_xpath('//*[@id="report_body"]/tr[' + str(i) + ']/td[3]/a')
        driver.execute_script("arguments[0].scrollIntoView(true);", element)
        key = driver.find_element_by_xpath('//*[@id="report_body"]/tr[' + str(i) + ']/td[1]').text
        value = driver.find_element_by_xpath('//*[@id="report_body"]/tr[' + str(i) + ']/td[3]/a').text
        time.sleep(3)
        dict[key]=value
        print(dict)
        #WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="report_body"]/tr[' + str(i) + ']/td[1]')))
        driver.find_element_by_xpath('//*[@id="report_body"]/tr[' + str(i) + ']/td[3]/a').click()
    except Exception as e:
        break
    for j in range(4, 5):
        try:
            dict1 = {}
            time.sleep(3)
            #driver.execute_script("window.scrollTo(0, 0)")
            #element = driver.find_element_by_xpath('//*[@id="caseDetails_report_body"]/tr['+ str(j) +']/td[1]')
            #driver.execute_script("arguments[0].scrollIntoView(true);", element)
            select = Select(driver.find_element_by_xpath('//*[@id="example_caseDetails_length"]/label/select'))
            select.select_by_value('50')
            key1 = driver.find_element_by_xpath('//*[@id="caseDetails_report_body"]/tr[' + str(j) + ']/td[1]').text
            value1 = driver.find_element_by_xpath('//*[@id="caseDetails_report_body"]/tr[' + str(j) + ']/td[2]/a').text
            Key1 = key + ' - ' + key1
            dict1[Key1] = value1
            dict.update(dict1)
            print(dict)
            driver.find_element_by_xpath('//*[@id="caseDetails_report_body"]/tr[' + str(j) + ']/td[2]/a').click()
        except Exception as e:
            driver.execute_script("window.scrollTo(0, 0)")
            with wait_for_page_load(driver):
                # time.sleep(10)
                driver.find_element_by_link_text("Back")
            driver.find_element_by_link_text("Back").click()
            print("HERE")
            break
        for k in range(1, 51):
            try:
                dict2={}
                time.sleep(3)
                #element = driver.find_element_by_xpath('//*[@id="stateWise_caseDetails_report_body"]/tr[' + str(k) + ']/td[2]/a')
                #driver.execute_script("arguments[0].scrollIntoView(true);", element)
                select = Select(driver.find_element_by_xpath('//*[@id="example_stateWise_caseDetails_length"]/label/select'))
                select.select_by_value('50')
                key2 = driver.find_element_by_xpath('//*[@id="stateWise_caseDetails_report_body"]/tr[' + str(k) + ']/td[1]').text
                value2 = driver.find_element_by_xpath('//*[@id="stateWise_caseDetails_report_body"]/tr[' + str(k) + ']/td[2]/a').text
                Key2 = Key1 + ' - ' + key2
                dict2[Key2] = value2
                dict.update(dict2)
                print(dict)
                #time.sleep(10)
                driver.find_element_by_xpath('//*[@id="stateWise_caseDetails_report_body"]/tr[' + str(k) + ']/td[2]/a').click()
            except Exception as e:
                driver.execute_script("window.scrollTo(0, 0)")
                with wait_for_page_load(driver):
                    # time.sleep(10)
                    driver.find_element_by_link_text("Back").click()
                #driver.find_element_by_link_text("Back").click()
                print("HERE2")
                break
            for l in range(1 ,101):
                try:
                    dict3 = {}
                    time.sleep(3)
                    select = Select(driver.find_element_by_xpath(
                        '//*[@id="example_distWise_caseDetails_length"]/label/select'))
                    select.select_by_value('50')
                    key3 = driver.find_element_by_xpath(
                        '//*[@id="distWise_caseDetails_report_body"]/tr[' + str(l) + ']/td[1]').text
                    value3 = driver.find_element_by_xpath(
                        '//*[@id="distWise_caseDetails_report_body"]/tr[' + str(l) + ']/td[2]/a').text
                    Key3 = Key2 + ' - ' + key3
                    dict3[Key3] = value3
                    dict.update(dict3)
                    print(dict)
                    #time.sleep(10)
                    driver.find_element_by_xpath('//*[@id="distWise_caseDetails_report_body"]/tr[' + str(l) + ']/td[2]/a').click()
                except Exception as e:
                    driver.execute_script("window.scrollTo(0, 0)")
                    with wait_for_page_load(driver):
                    # time.sleep(10)
                        driver.find_element_by_link_text("Back").click()
                    #driver.find_element_by_link_text("Back").click()
                    break
                for m in range(1,51):
                    try:
                        dict4 = {}
                        time.sleep(3)
                        select = Select(driver.find_element_by_xpath('//*[@id="example_estCodeWise_caseDetails_length"]/label/select'))
                        select.select_by_value('50')
                        key4 = driver.find_element_by_xpath('//*[@id="estCodeWise_caseDetails_report_body"]/tr[' + str(m) + ']/td[1]').text
                        value4 = driver.find_element_by_xpath('//*[@id="estCodeWise_caseDetails_report_body"]/tr[' + str(m) + ']/td[2]/a').text
                        Key4 = Key3 + ' - ' + key4
                        dict4[Key4] = value4
                        dict.update(dict4)
                        print(dict)
                        #time.sleep(10)
                        driver.find_element_by_xpath('//*[@id="estCodeWise_caseDetails_report_body"]/tr[' + str(m) + ']/td[2]/a').click()
                    except Exception as e:
                        driver.execute_script("window.scrollTo(0, 0)")
                        with wait_for_page_load(driver):
                        # time.sleep(10)
                            driver.find_element_by_link_text("Back").click()
                        #driver.find_element_by_link_text("Back").click()
                        break
                    for t in range(1,51):
                        try:

                            dict5 = {}
                            #print(t)
                            time.sleep(3)
                            with wait_for_page_load(driver):
                                driver.find_element_by_xpath('//*[@id="example_regYearWise_caseDetails_length"]/label/select')


                            select = Select(driver.find_element_by_xpath('//*[@id="example_regYearWise_caseDetails_length"]/label/select'))
                            select.select_by_value('50')
                            with wait_for_page_load(driver):
                                driver.find_element_by_xpath(
                                    '//*[@id="regYearWise_caseDetails_report_body"]/tr[' + str(t) + ']/td[1]')
                            key5 = driver.find_element_by_xpath('//*[@id="regYearWise_caseDetails_report_body"]/tr[' + str(t) + ']/td[1]').text
                            value5 = driver.find_element_by_xpath('//*[@id="regYearWise_caseDetails_report_body"]/tr[' + str(t) + ']/td[2]/a').text
                            Key5 = Key4 + ' - ' + key5
                            dict5[Key5] = value5
                            dict.update(dict5)
                            print(dict)
                            time.sleep(5)
                            z = driver.find_element_by_xpath('//*[@id="regYearWise_caseDetails_report_body"]/tr[' + str(t) + ']/td[2]/a').text
                            driver.find_element_by_xpath('//*[@id="regYearWise_caseDetails_report_body"]/tr[' + str(t) +
                                                         ']/td[2]/a').click()
                            z = str(z)
                            z = int(z)
                            y = int(z / 100)

                            if z > 0:
                                for o in range(1, y + 2):
                                        for p in range(1, 101):
                                            try:
                                                dict6 = {}
                                                time.sleep(3)
                                                select = Select(driver.find_element_by_xpath('//*[@id="example_regnoWise_caseDetails_length"]/label/select'))
                                                select.select_by_value('100')
                                                driver.find_element_by_xpath('// *[ @ id = "example_regnoWise_caseDetails_next"]').click()
                                                key6 = driver.find_element_by_xpath('//*[@id="regnoWise_caseDetails_report_body"]/tr[' + str(p) + ']/td/a').text
                                                value6 = driver.find_element_by_xpath('//*[@id="regnoWise_caseDetails_report_body"]/tr[' + str(p) + ']/td/a').text
                                                Key6 = Key5 + ' - ' + key6
                                                dict6[Key6] = value6
                                                dict.update(dict6)
                                                print(dict)
                                                # time.sleep(10)
                                            except Exception as e:
                                                driver.execute_script("window.scrollTo(0, 0)")
                                                with wait_for_page_load(driver):
                                                    # time.sleep(10)
                                                    driver.find_element_by_link_text("Back")
                                                driver.find_element_by_link_text("Back").click()
                                                break
                                        with wait_for_page_load(driver):
                                            driver.find_element_by_xpath('//*[@id="example_regnoWise_caseDetails_next"]').click()

                            else:
                                for p in range(1, 101):
                                    try:
                                        dict6 = {}
                                        time.sleep(3)
                                        select = Select(driver.find_element_by_xpath('//*[@id="example_regnoWise_caseDetails_length"]/label/select'))
                                        select.select_by_value('100')
                                        driver.find_element_by_xpath('// *[ @ id = "example_regnoWise_caseDetails_next"]').click()
                                        key6 = driver.find_element_by_xpath('//*[@id="regnoWise_caseDetails_report_body"]/tr[' + str(p) + ']/td/a').text
                                        value6 = driver.find_element_by_xpath('//*[@id="regnoWise_caseDetails_report_body"]/tr[' + str(p) + ']/td/a').text
                                        Key6 = Key5 + ' - ' + key6
                                        dict6[Key6] = value6
                                        dict.update(dict6)
                                        print(dict)
                                        # time.sleep(10)
                                    except Exception as e:
                                        #time.sleep(10)
                                        driver.execute_script("window.scrollTo(0, 0)")
                                        with wait_for_page_load(driver):
                                            #time.sleep(10)
                                            driver.find_element_by_xpath('//*[@id="regno_Wise_caseDetails_tab"]/a')
                                        driver.find_element_by_xpath('//*[@id="regno_Wise_caseDetails_tab"]/a').click()
                                        break
                        except Exception as e:
                            driver.execute_script("window.scrollTo(0, 0)")
                            with wait_for_page_load(driver):
                                driver.find_element_by_link_text("Back")
                            driver.find_element_by_link_text("Back").click()
                            break

pickle.dump(dict, pickle_out)
pickle_out.close()






