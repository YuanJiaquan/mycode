'''
    三类等待：
        1. 强制等待:
            不考虑整体代码的连贯性和逻辑性，运行到强制等待时，就直接停止指定的时间
            时间结束后，再继续运行后面的代码
            sleep表示强制等待，以秒为时间单位，是在time包下的类
            优势：容易上手，有需要的时候直接调用即可。对于新手特别友好
            劣势：迟钝。在自动化执行时会造成大量的时间浪费
            一般而言都是新手在使用sleep，或者是临时性的调试应用。或者特定情况
        2. 隐式等待
            悄悄的等待。本质意义上而言是driver的一个设置项
            只需要设置一次，即可在整个driver生命周期中生效
            隐式等待的时间也是基于秒来进行等待的。但是隐式等待会在找到元素之后，等待直接结束。
            如果没有找到元素，就会一直等待到最大时间。等待的过程中会一直去寻找这个元素。
            如果最终没有找到元素，就继续运行代码。
            隐式等待必须要等待页面加载完成之后再生效。所以效率的提升不是太明显。
            没有办法指定到元素来进行等待。
            一般而言隐式等待都会添加。添加的时间一般是5或者10秒
            优势：在整个webdriver生命周期中，只需要设置一次即可。
            劣势：如果找不到元素就不管了。
        3. 显式等待：
            专门针对元素来进行等待的。
            和强制等待一样，在需要调用的时候就要定义。
            显式等待分为until和until_not两种函数来实现等待，作用是完全相反
            如果元素未查找到，会抛出timeout的异常。
            显示等待在执行的时候会有一个return，返回等待的元素
            优势： 可以直接对单个元素进行等待，效率最高。
            劣势： 代码太长了，用起来比较麻烦。
            显示等待还可以作为断言的形式来使用。
    在实际的自动化测试中，等待是综合运用的。
    当显式与隐式同时存在的时候：
        1. 如果显示等待的元素找不到，则抛出超时异常。
        2. 基于两者等待机制的时间设定，默认遵循时间更长的等待。
'''
from time import sleep

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()

# 隐式等待
driver.implicitly_wait(5)

driver.get('http://www.baidu.com')
driver.find_element('id', 'kw').send_keys('xuzhu')
driver.find_element('id', 'su').click()

# 强制等待
# sleep(2)

# 显式等待
el = WebDriverWait(driver, 10, 0.5).until(
    lambda el1: driver.find_element('xpath', '//*[@id="1"]/h3/a1'), message='查找失败')
# WebDriverWait(driver, 5, 0.5).until_not(
#     lambda el1: driver.find_element('xpath', '//*[@id="1"]/h3/a'), message='查找失败')
driver.find_element('xpath', '//*[@id="1"]/h3/a1').click()
print('这是a1元素后的一行代码')

'''
    弹窗机制：
        很久没用过了。现在的系统很少有了。因为所有的弹窗交互都是基于div层直接实现。
        所有形式的弹窗不是页面弹出，而是浏览器弹出。
        在浏览器中有三类弹窗：
            1. alert：确认
            2. prompt：支持输入并确认
            3. confirm：确认与取消
        
    如果弹窗的样式与操作系统或者浏览器一个风格，则一定是alert
    如果弹窗的样式与软件系统一个风格，一般都是div层，只需要考虑是否存在iframe即可
'''
# 切换到弹窗
alert = driver.switch_to.alert
# alert弹窗处理
alert.accept()
# confirm弹窗处理
alert.accept()
alert.dismiss()
# prompt
alert.send_keys()
alert.accept()
alert.dismiss()
# 获取alert弹窗的文本
text = alert.text

