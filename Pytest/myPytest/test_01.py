from time import sleep

import pytest
from selenium import webdriver

def setup():
    print('前置')
def teardown():
    print('后置')


@pytest.mark.interface
def test_01(jiaquan):
    if jiaquan==1:
        driver = webdriver.Chrome()
        driver.get('http://www.baidu.com')
        sleep(2)
        driver.quit()


def test_02():
    driver = webdriver.Chrome()
    driver.get('http://www.bilibili.com')
    sleep(2)
    driver.quit()


def test_03():
    driver = webdriver.Chrome()
    driver.get('http://www.douyu.com')
    sleep(2)
    driver.quit()


if __name__ == '__main__':
    pytest.main(['test_01.py::test_01'])