'''
    Document对象，是前端中的顶梁柱。UI自动化的过程中操作的就是前端对象，对于一些特殊
    场景，可以通过document对象来进行处理
    作用:
        1. 定位元素。
        2. 通过Document修改元素属性，添加或者移除属性
        3. 滚动条操作：目前要么可以忽略，要么只能通过js来实现。
            滚动的比例记三个数值：
                1. 0 表示最上方
                2. 500 表示中间
                3. 1000 表示末尾
        4. 滚动到指定元素:
            操作滚动条的目的就是为了将指定的元素显示出来，能够通过selenium进行定位与操作。
    arguments是占位符，相对document更为灵活操作
'''
# 导入selenium模块
from time import sleep

from selenium import webdriver

# 启动浏览器:浏览器首字母要大写，还要添加()
driver = webdriver.Chrome()
# 访问url:一定要在url中添加http://这样的内容,如果不加会报错，必须加//
driver.get('http://www.baidu.com')
# 输入‘秋水好蠢’：通过find element函数查找元素，一定是查找有对应属性的元素
# driver.find_element_by_name('wd').send_keys('虚竹')
# # 点击‘百度一下’按钮实现搜索
# driver.find_element_by_id('su').click()
# 添加等待
sleep(3)

# 滚动条操作js语句
# js = 'window.scrollTo(0,500)'
# # 通过js执行器来实现js语句的调用。
# driver.execute_script(js)
# el = driver.find_element('xpath', '//*[@id="10"]/h3/a')
# js精准定位到指定元素，并显示
# js = "arguments[0].scrollIntoView()"
# 调用js执行器
# driver.execute_script(js, el)

# el = driver.find_element('xpath', '//*[@id="kw"]')
# # js修改元素属性
# js = 'arguments[0].removeAttribute("name")'
# driver.execute_script(js, el)

el = driver.find_element('xpath', '//*[@id="s-top-left"]/a[1]')
# 通过js获取对象或者内容时，需要在原有的js语句上添加return
js = 'return arguments[0].innerHTML'
text = driver.execute_script(js, el)
print(text)
print(driver.find_element('xpath', '//*[@id="s-top-left"]/a[1]').text)
