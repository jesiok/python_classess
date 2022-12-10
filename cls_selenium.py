########### config ############
########### BROWSER ############
# 'BRAVE'
# 'DECENTR'
BROWSER = "BRAVE"

############ BINARY PATH ############
# linux brave app = '/usr/bin/brave-browser'
# linux decentr app = '/usr/bin/decentr-browser-stable'  
# windows chrome app "C:\Program Files\Google\Chrome\Application\chrome.exe"
BINARY_PATH = '/usr/bin/brave-browser'


############ DRIVER PATH ############
# skad sciagnac
# driver = webdriver.Chrome('./chromedriver')
# linux chromedriver  = '/usr/bin/chromedriver'
# linux sciagniety webdriver DRIVER_PATH_DECENTR = '/home/jesiok/Downloads/chromedriver_linux64_100/chromedriver'
DRIVER_PATH = '/usr/bin/chromedriver'
#chromedriver108.exe

############ PROFILE PATH ############
# windows profile Brave: "C:\Users\grzeg\AppData\Local\BraveSoftware\Brave-Browser\User Data\Profile 2"
# windows profile Chrome: "C:\Users\grzeg\AppData\Local\Google\Chrome\User Data\Profile 2"
# linux profile Brave:  "--user-data-dir=/home/jesiok/.config/BraveSoftware/Brave-Browser/Profile 2"
# linux prifle Decentr "--user-data-dir=/home/jesiok/.config/decentr/Profile 1"

PROFILE_PATH = "--user-data-dir=/home/jesiok/.config/BraveSoftware/Brave-Browser/Profile 2"

############ ENVIROMWNT
ENV = "PRD"

#########################################################
#########################################################

from selenium import webdriver

import config
import pandas as pd


class Browser():

    def __init__(self, driver = None, webdriver_name = '', BINARY_PATH = '', DRIVER_PATH = '', PROFILE_PATH = ''):
        # przydkladowe wywolanie:
        # br = cls_selenium.Browser(webdriver_name = 'chrome', BINARY_PATH=config.BINARY_PATH, DRIVER_PATH=config.DRIVER_PATH, PROFILE_PATH = config.PROFILE_PATH) 
        if webdriver_name == 'chrome':
            option = webdriver.ChromeOptions()
            option.add_argument(PROFILE_PATH)
            #option.add_argument("--user-data-dir=/home/jesiok/.config/BraveSoftware/Brave-Browser/Profile 2")
            option.add_argument("--window-size=1920,1200")
            option.add_argument("--disable-gpu")
            option.add_argument("--ignore-certyficate-errors")
            option.add_argument("--disable-extensions")
            option.add_argument("--no-sandbox")
            option.add_argument("--disable-dev-shm-usage")
            # option.add_argument("--disable-infobars")
            # option.add_argument("--enable-file-cookies")
        
            # Usuniecie infobara - np Brave is controlled by automated system softwere
            option.add_experimental_option("excludeSwitches", ["enable-automation"])
            option.add_experimental_option('useAutomationExtension', False)
            
            #option.add_argument("--headless") # ale trzeba wtedy podmienic useragenta
            #option.binary_location = config.BINARY_PATH
            #self.driver = webdriver.Chrome(executable_path = config.DRIVER_PATH, chrome_options=option)
            option.binary_location = BINARY_PATH
            self.driver = webdriver.Chrome(executable_path = DRIVER_PATH, chrome_options=option)
            
        if webdriver_name == 'firefox':
            print('firefox jeszcze nie zrobiony')
            
    def open_page(self,url):
        self.driver.implicitly_wait(30) # moe to czas da na inpucie. Bez tego potem nie bedzie wylapywac np linkow a href
        self.driver.get(url)
    
    def check_xpath_exists(self, xpath):
        # from selenium.common.exceptions import NoSuchElementException
        try:
            self.driver.find_element('xpath',xpath)
        except NoSuchElementException:
            return False
        return True
    
    def get_all_links_from_page(self):
        # ??? monzna zrobic cos bardziej uniwersalnego

        xpath = "//body//*[@href]"
        elems = self.driver.find_elements("xpath",xpath)
        links = []
        for elem in elems:
            url_from_page = elem.get_attribute("href")
            links.append(url_from_page)            
        return links
     
    


    def save_elem_to_excel(self):
        # ??? dorobic
        # with pd.ExcelWriter('links.xlsx', engine='openpyxl', mode='a') as writer:  
        #     df.to_excel(writer, sheet_name='sts')
        pass
    
    def close_all_tabs(self):

        # get number of opened tabs
        i_tabs = len(self.driver.window_handles)
        for i in range (i_tabs):
            
            print(i)
            print(self.driver.current_url)
            self.driver.switch_to.window(self.driver.window_handles[i-1])
            self.driver.close()
    
    def execute_js_script(self):
        # do poprawki i przetestowania
        xpath = "//a[@href]"
        elems = self.driver.find_elements("xpath",xpath)
        attrs = self.driver.execute_script('var items = {}; for (index = 0; index < arguments[0].attributes.length; ++index) { items[arguments[0].attributes[index].name] = arguments[0].attributes[index].value }; return items;', elems)        
        print(attrs)
    
    def get_all_attributes_from_element(self):
        # do poprawki i przetestowania
        xpath = "//a[@href]"
        elems = self.driver.find_elements("xpath",xpath)
        attrs=[]
        for attr in elems[0].get_property('attributes'):
            attrs.append([attr['name'], attr['value']])
            print(attrs)

        
    # def openBrowser(self,driver=''):
    #     pass
        
    
    # def closeAllTabsInBrowser(self,driver):
    #     pass
    
