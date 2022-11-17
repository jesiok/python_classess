from selenium import webdriver

import config
import pandas as pd


class Browser():
    def __init__(self,driver = None):
        
        option = webdriver.ChromeOptions()
        option.add_argument(r"--user-data-dir=/home/jesiok/.config/BraveSoftware/Brave-Browser/Profile 1")
        option.add_argument("--window-size=1920,1200")
        option.add_argument("--disable-gpu")
        option.add_argument("--ignore-certyficate-errors")
        option.add_argument("--disable-extensions")
        option.add_argument("--no-sandbox")
        option.add_argument("--disable-dev-shm-usage")
        
        #option.add_argument("--headless") # ale trzeba wtedy podmienic useragenta
        option.binary_location = config.BINARY_PATH
        self.driver = webdriver.Chrome(executable_path = config.DRIVER_PATH, chrome_options=option)

    def open_page(self,url):
        self.driver.implicitly_wait(10) # moe to czas da na inpucie. Bez tego potem nie bedzie wylapywac np linkow a href
        self.driver.get(url)
    
    def get_all_links_from_page(self):
        # ??? monzna zrobic cos bardziej uniwersalnego

        xpath = "//*[@href]"
        elems = self.driver.find_elements("xpath",xpath)
        links = []
        for elem in elems:
            url_from_page = elem.get_attribute("href")
            links.append(url_from_page)

        return links
        
    def check_mainpage_wallet_earning(self):
        # info o zebranej sumie w tym miesiacu
        xpath = "//div[contains(@class,'earning')]//span[@class = 'amount']"
        elems = self.driver.find_elements("xpath",xpath)
        out = elems[0].text
        return out
    
    def check_mainpage_wallet_pending(self):
        # na poczatku miesiaca pojawia sie info ile BAT-ow jest w pendingu
        # do zweryfikowania
        xpath = "//div[@class='rewards-payment-pending']"
        elems = self.driver.find_elements("xpath",xpath)
        i_elems = elems.length
        if i_elems > 0:
            out = elems[0].textContent
        else:
            out = ''
        
        ##xpath = "//div[@class='rewards-payment-pending'][0].textContent"
        return out
    
    def check_mainpage_stats(self):
        xpath = "//span[contains(@class,'StyledStatsItemCounter')]"
        elems = self.driver.find_elements("xpath",xpath)
        v_trackers = elems[0].text
        v_bandwidth = elems[1].text
        v_time = elems[2].text
        return v_trackers, v_bandwidth, v_time

    def check_mainpage_total_balance(self):
        pass
        
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
    