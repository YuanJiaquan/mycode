from time import sleep

from selenium import webdriver

driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(3)
driver.get('http://www.baidu.com')
driver.find_element('id','kw').send_keys('xuzhu')
driver.find_element('id','su').click()

# js='window.scrollTo(0,500)'
js='arguments[0].scrollIntoView()'
el=driver.find_element('xpath','//*[@id="10"]/h3/a')
driver.execute_script(js,el)
print(el.text)
js1='return arguments[0].innerHTML'
x=driver.execute_script(js1,el)
print(x)
js2='arguments[0].setAttribute("name","xiaoming")'
driver.execute_script(js2,el)

sleep(20)

driver.close()