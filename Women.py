from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
import pickle
from selenium.webdriver.chrome.options import Options

driver = webdriver.Chrome("/Users/adhyadagar/PycharmProjects/WebCrawler1/Drivers/chromedriver")

site = driver.get("https://njdg.ecourts.gov.in/njdgnew/index.php")

title = driver.title

print(title)

my_url = "https://njdg.ecourts.gov.in/njdgnew/index.php"

dict = {}

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


pickle_out = open("WomanCases.pickle","wb")

chrome_options = Options()
# maximized window
chrome_options.add_argument("--start-maximized")

#WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="report_body"]/tr[' + str(i) + ']/td[1]')))
element = driver.find_element_by_xpath('//*[@id="report_body"]/tr[27]/td[1]')
driver.execute_script("arguments[0].scrollIntoView(true);", element)
key = driver.find_element_by_xpath('//*[@id="report_body"]/tr[27]/td[1]').text
value = driver.find_element_by_xpath('//*[@id="report_body"]/tr[27]/td[3]/a').text
time.sleep(10)
dict[key]=value
print(dict)
driver.find_element_by_xpath('//*[@id="report_body"]/tr[27]/td[3]/a').click()
for i in range(1, 51):
    try:
        dict1 = {}
        time.sleep(10)
        with wait_for_page_load(driver):
            driver.find_element_by_xpath('//*[@id="example_WomenState_length"]/label/select')
        time.sleep(10)
        select = Select(driver.find_element_by_xpath('//*[@id="example_WomenState_length"]/label/select'))
        select.select_by_value('50')
        key1 = driver.find_element_by_xpath('//*[@id="WomenState_body"]/tr['+ str(i) +']/td[1]').text
        value1 = driver.find_element_by_xpath('//*[@id="WomenState_body"]/tr['+ str(i) +']/td[2]/a').text
        Key1 = key + ' - ' + key1
        dict1[Key1] = value1
        dict.update(dict1)
        print(dict)
        driver.find_element_by_xpath('//*[@id="WomenState_body"]/tr['+ str(i) +']/td[2]/a').click()
    except Exception as e:
        driver.execute_script("window.scrollTo(0, 0)")
        with wait_for_page_load(driver):
            # time.sleep(10)
            driver.find_element_by_link_text("Back")
        driver.find_element_by_link_text("Back").click()
        break
    for j in range(1,101):
        try:
            dict2 = {}
            time.sleep(10)
            select = Select(driver.find_element_by_xpath('//*[@id="example_Womendist_length"]/label/select'))
            select.select_by_value('100')
            key2 = driver.find_element_by_xpath('//*[@id="Womendist_body"]/tr['+ str(j) +']/td[1]').text
            value2 = driver.find_element_by_xpath('//*[@id="Womendist_body"]/tr['+ str(j) +']/td[2]/a').text
            Key2 = Key1 + ' - ' + key2
            dict2[Key2] = value2
            dict.update(dict2)
            print(dict)
            # time.sleep(10)
            #driver.find_element_by_xpath('//*[@id="Womendist_body"]/tr['+ str(j) +']/td[2]/a').click()
        except Exception as e:
            driver.execute_script("window.scrollTo(0, 0)")
            with wait_for_page_load(driver):
                # time.sleep(10)
                driver.find_element_by_link_text("Back")
            driver.find_element_by_link_text("Back").click()
            break
        for k in range(1,51):
            try:
                dict3 = {}
                time.sleep(10)
                select = Select(driver.find_element_by_xpath('//*[@id="example_Womenest_length"]/label/select'))
                select.select_by_value('50')
                key3 = driver.find_element_by_xpath('//*[@id="Womenest_body"]/tr['+ str(k) +']/td[1]').text
                value3 = driver.find_element_by_xpath('//*[@id="Womenest_body"]/tr['+ str(k) +']/td[2]/a').text
                Key3 = Key2 + ' - ' + key3
                dict3[Key3] = value3
                dict.update(dict3)
                print(dict)
                driver.find_element_by_xpath('//*[@id="Womenest_body"]/tr['+ str(k) +']/td[2]/a').click()
                time.sleep(10)
                element = driver.find_element_by_xpath('//*[@id="example_Womencase_info"]')
                driver.execute_script("arguments[0].scrollIntoView(true);", element)
                with wait_for_page_load(driver):
                    driver.find_element_by_xpath('//*[@id="example_Womencase_info"]')
                y = driver.find_element_by_xpath('//*[@id="example_Womencase_info"]')
                temp = y.text
                temps2 = temp.split(" ")
                x = int(temps2[-2])
                z = int(x / 100)
                print(z)
            except Exception as e:
                driver.execute_script("window.scrollTo(0, 0)")
                with wait_for_page_load(driver):
                    # time.sleep(10)
                    driver.find_element_by_link_text("Back")
                driver.find_element_by_link_text("Back").click()
                break
            if z > 0:
                for n in range(1,z+2):
                    try:
                        for m in range(1,101):
                            try:
                                dict4 = {}
                                time.sleep(3)
                                select = Select(driver.find_element_by_xpath('//*[@id="example_Womencase_length"]/label/select'))
                                select.select_by_value('100')
                                key4 = driver.find_element_by_xpath('//*[@id="Womenest_body"]/tr['+ str(m) +']/td/a').text
                                value4 = driver.find_element_by_xpath('//*[@id="Womenest_body"]/tr['+ str(m) +']/td/a').text
                                Key4 = Key3 + ' - ' + key4
                                dict4[Key4] = value4
                                dict.update(dict4)
                                print(dict)
                                # time.sleep(10)
                            except Exception as e:
                                #print(e)
                                driver.execute_script("window.scrollTo(0, 0)")
                                with wait_for_page_load(driver):
                                    # time.sleep(10)
                                    driver.find_element_by_link_text("Back")
                                driver.find_element_by_link_text("Back").click()
                                break
                        with wait_for_page_load(driver):
                            driver.find_element_by_xpath('//*[@id="example_Womencase_next"]').click()
                    except Exception as e:
                        break
            else:
                for m in range(1, 101):
                    try:
                        dict4 = {}
                        time.sleep(10)
                        select = Select(
                            driver.find_element_by_xpath('//*[@id="example_Womencase_length"]/label/select'))
                        select.select_by_value('100')
                        #WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="Womenest_body"]/tr[' + str(m) + ']/td/a')))
                        key4 = driver.find_element_by_xpath('//*[@id="Womenest_body"]/tr[' + str(m) + ']/td/a').text
                        value4 = driver.find_element_by_xpath('//*[@id="Womenest_body"]/tr[' + str(m) + ']/td/a').text
                        Key4 = Key3 + ' - ' + key4
                        dict4[Key4] = value4
                        dict.update(dict4)
                        print(dict)
                        # time.sleep(10)
                    except Exception as e:
                        print(e)
                        driver.execute_script("window.scrollTo(0, 0)")
                        with wait_for_page_load(driver):
                            # time.sleep(10)
                            driver.find_element_by_link_text("Back")
                        driver.find_element_by_link_text("Back").click()
                        break





pickle.dump(dict,pickle_out)
pickle_out.close()




