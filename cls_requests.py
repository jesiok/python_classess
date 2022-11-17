import random
from fake_useragent.fake import UserAgent
import requests
from fake_useragent import User

class Request():
    url = ''
    
    user_agent = ''
    cookies = ''
    payload = ''
    header = ''
    
def cookies():
    pass
    
def request_validate(response):
    r = response.status_code
    if r == 200:
        pass
    else: 
        raise Exception (f'resp: = {r}')
        
        

 
def random_user_agent_by_my_dict():
    dict_user_agent = {"chrome" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36",
                    "firefox" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:95.0) Gecko/20100101 Firefox/95.0",
                    "edge" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18363",
                    "ie" : "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko",
                    "opera": "Opera/9.80 (Windows NT 6.0) Presto/2.12.388 Version/12.14",
                    "mac": "Mozilla/5.0 (Macintosh; Intel Mac OS X 12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 OPR/82.0.4227.43",
                    "linux": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 OPR/82.0.4227.43"
                    }
    user_agent = list(dict_user_agent.values())
    user_agent = random.choice(user_agent)
    return user_agent

def random_user_agent_by_package_dict():
    ua = UserAgent()
    a = ua.random
    
    # if response.status_code != 200:
    #     print(f'request error resp: {response.status_code}')
    
    # print (response.headers)