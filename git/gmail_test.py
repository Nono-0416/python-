from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import bs4
import os,requests
import configparser
config = configparser.ConfigParser()


class gmail_test(object):
    '''
    classdocs
    '''
    def __init__(self):
        '''
        Constructor
        '''
        pass
    
    def set(self,browser,value_dict):
        folder = value_dict['folder']
        configfile = value_dict['configfile']
        config.read(os.path.join(os.getcwd() , folder , configfile),encoding="utf-8")
        session = value_dict['session']
        xpath = value_dict['xpath_id']
        # elem = browser.find_element_by_xpath(config.get(session, xpath))
        elem = browser.find_element(By.XPATH, config.get(session, xpath))
        elem.send_keys(value_dict['value'])
    
    def click(self,browser,value_dict):
        folder = value_dict['folder']
        configfile = value_dict['configfile']
        config.read(os.path.join(os.getcwd() , folder , configfile),encoding="utf-8")
        session = value_dict['session']
        xpath = value_dict['xpath_id']
        elem = browser.find_element(By.XPATH, config.get(session, xpath))
        elem.click()

    def email_search_enter(self,browser,value_dict):
        folder = value_dict['folder']
        configfile = value_dict['configfile']
        config.read(os.path.join(os.getcwd() , folder , configfile),encoding="utf-8")
        session = value_dict['session']
        xpath = value_dict['xpath_id']
        elem = browser.find_element(By.XPATH, config.get(session, xpath))
        elem.send_keys(Keys.ENTER)

    def email_exist_verify(self,browser,value_dict):
        folder = value_dict['folder']
        configfile = value_dict['configfile']
        config.read(os.path.join(os.getcwd() , folder , configfile),encoding="utf-8")
        xpath = '/html[1]/body[1]/div[7]/div[3]/div[1]/div[2]/div[4]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/span[1]/div[1]/span[1]/span[2]'
        
        
        try :
            result = browser.find_element(By.XPATH, xpath)
            if result != '0':
                pass
        except NoSuchElementException:
            raise error.notfind()
