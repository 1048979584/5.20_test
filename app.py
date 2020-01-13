from appium import webdriver
import time
class AppiumTest:
    def appTest(self):
        #配置连接appium的连接参数的
        disred_caps={}                                               #定义webdriver的兼容性设置字典对象
        disred_caps['platformName']='Android'                        #指定测试平台
        disred_caps['platformVersion']='5.1.1'                       #指定移动端的版本号
        disred_caps['deviceName']='Appium'                           #/指定设备名称-手机类型或模拟器
        disred_caps['appPackage']='com.tencent.mm'                   #指定要启动的包
        disred_caps['appActivity']='.ui.LauncherUI'                  #指定的主类程序
        disred_caps['udid']='127.0.0.1:62001'                        #指定模拟器编号（adb devices输出结果）
        app_path="C:\\Users\\A\\Desktop\\weixin.apk"
        #app_path=os.path.abspath('.')+\\xxx.apk                     #指定apk文件路径安装程序
        disred_caps['app']=app_path                                  #指定待测应用程序
        disred_caps['unicodeKeyboard']='True'                        #指定可输入中文
        disred_caps['noReset']='True'                                  #设置是否清空应用程序数据（执行完后卸载apk）


        #实例化webdriver，并指定appium服务器访问地址，一定要加上，wd/hub
        driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub',disred_caps)
        time.sleep(3)
        #使用C:\Program Files (x86)\android-sdk-windows\tools\uiautomatorviewer.bat工具获取页面元素
        #模拟手工操作
        driver.find_element_by_id("com.tencent.mm:id/drq").click()
        driver.find_element_by_id("com.tencent.mm:id/ji").send_keys(13628165081)
        driver.find_element_by_id("com.tencent.mm:id/ast").click()
        driver.find_element_by_id("com.tencent.mm:id/ji").send_keys("QwdQQ8863200")
        driver.find_element_by_id("com.tencent.mm:id/ast").click()
    #测试系统自带浏览器
    def chrome_test(self):
        disred_caps={}
        disred_caps['platformName']='Android'
        disred_caps['platformVersion']='5.1.1'
        disred_caps['deviceName']='Appium'
        disred_caps['browserName']='chrome'
        disred_caps['appPackage']='com.tencent.mm'
        disred_caps['appActivity']='.ui.LauncherUI'
        disred_caps['udid']='127.0.0.1:62001'
        disred_caps['unicodeKeyboard']='True'
        driver=webdriver.Remote("http://127.0.0.1:4327/wd/hub",disred_caps)


if __name__ == '__main__':
    AppiumTest().appTest()