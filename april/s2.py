from ddt import ddt,file_data
from selenium import webdriver
import unittest
from time import sleep

@ddt
class case_demo(unittest.TestCase):
    @file_data('../yaml1/data.yaml')
    def test_01(self,**kwargs):
        driver=webdriver.Chrome()
        driver.get(kwargs['url'])
        driver.find_element_by_id('kw').send_keys(kwargs['txt'])
        driver.find_element_by_id('su').click()
        sleep(2)
        quit()





if __name__=='__main__':
    unittest.main()
