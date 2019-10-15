import time
from io import BytesIO
from PIL import Image
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

EMAIL = 'cqc@cuiqingcai.com'
PASSWORD = '123456'
BORDER=6
BORDER_1=7
BORDER_2=12
class CrackGeetest():
    def __init__(self):
        self.url='https://account.geetest.com/login'
        self.browser=webdriver.Chrome()
        self.wait=WebDriverWait(self.browser,20)
        self.browser.maximize_window()
        self.email=EMAIL
        self.password=PASSWORD
        self.success=False
        self.try_num=2
        self.now_num=2
        self.flesh_num=1

    def __del__(self):
        self.browser.close()

    def open(self):
        '''
        打开网页输入用户名和密码
        :return: None
        '''
        self.browser.get(self.url)
        email = self.wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='email']")))
        password = self.wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='password']")))
        email.send_keys(self.email)
        password.send_keys(self.password)

    def get_geetest_button(self):
        '''
        获取初始化按钮
        :return:
        '''
        button = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'geetest_radar_tip')))
        return button

    def get_geetest_image(self,name='captcha.png'):
        '''
        获取验证码图片
        :return: 图片对象
        '''
        top,bottom,left,right=self.get_position()
        print('验证码位置：',top,bottom,left,right)
        screenshot=self.get_screenshot()
        #截取验证码图片
        captcha=screenshot.crop((left,top,right,bottom))
        captcha.save(name)
        return captcha

    def get_slider(self):
        '''
        获取滑块
        :return: 滑块对象
        '''
        try:
            slider=self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME,'geetest_slider_button')))
        except Exception:
            self.crack()
            return
        return slider

    def get_position(self):
        '''
        获取验证码上下左右位置
        :return: 验证码位置-元组形式
        '''
        img=self.wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME,'geetest_canvas_img')))
        time.sleep(2)
        location=img.location
        size=img.size
        top,bottom,left,right=location['y'],location['y']+size['height'],location['x'],location['x']+size['width']
        return(top,bottom,left,right)

    def get_screenshot(self):
        '''
        获取网页截图
        :return: 截图对象
        '''
        screenshot=self.browser.get_screenshot_as_png()
        #将image转换为字节流
        screenshot=Image.open(BytesIO(screenshot))
        return screenshot

    @staticmethod  #声明静态变量
    def get_track(distance):
        '''
        根据偏移量获取移动轨迹
        :param distance:偏移量
        :return:移动轨迹
        '''
        #移动轨迹
        track=[]
        #当前位移
        current=0
        #减速阈值
        mid=distance*4/5
        #计算间隔
        t=0.2
        #初速度
        v=0
        while current < distance:
            if current < mid:
        #加速度
                a=2
            else:
                a=-3
        #初速度
            v0=v
        #当前速度
            v=v0+a*t
        #移动距离
            move=v0*t+1/2*a*t*t
        #当前位移
            current+=move
        #加入轨迹
            track.append(round(move))
        return track

    def move_to_gap(self,slider,track):
        '''
        拖动滑块到缺口处
        :param slider:滑块
        :param track:轨迹
        :return:
        '''
        ActionChains(self.browser).click_and_hold(slider).perform()
        for x in track():
            ActionChains(self.browser).move_by_offset(xoffset=x,yoffset=0).perform()
        time.sleep(1)
        ActionChains(self.browser).release().perform()
    @staticmethod
    def is_pixel_equal(img1,img2,x,y):
        '''
        判断两个像素是否相同
        :param img1: 图片1
        :param img2: 图片2
        :param x: 位置X
        :param y: 位置Y
        :return: 像素是否相同
        '''
        #获取两个图片的像素点
        pix1=img1.load()[x,y]
        pix2=img2.load()[x,y]
        threshold = 60
        if (abs(pix1[0]-pix2[0]<threshold)) and abs(pix1[1]-pix2[1] < threshold and abs(pix1[2]-pix2[2]<threshold)):
            return True
        else:
            return False

    def get_gap(self,image1,image2):
        '''
        获取缺口偏移量
        :param image1: 没有缺口的图片
        :param image2: 有缺口的图片
        :return:
        '''
        left_list = []
        #image1.size[长，宽]
        left = 45
        for i in range(left, image1.size[0]):
            for j in range(image1.size[1]):
                if not self.is_pixel_equal(image1, image2, i, j):
                    left = i
                    return left
        return left

    def login(self):
        """
        登录
        :return: None
        """
        submit = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'login-btn')))
        submit.click()
        time.sleep(10)
        print('登录成功')
        
        
    #补充方法    
    def FindPic(target, template):

    """

    找出图像中最佳匹配位置即缺口位置

    :param target: 目标即背景图

    :param template: 滑块图

    :return: 返回最佳匹配及其最差匹配和对应的坐标

    """

    target_rgb = cv2.imread(target)

    target_gray = cv2.cvtColor(target_rgb, cv2.COLOR_BGR2GRAY)

    template_rgb = cv2.imread(template, 0)

    res = cv2.matchTemplate(target_gray, template_rgb, cv2.TM_CCOEFF_NORMED)

    value = cv2.minMaxLoc(res)    
        
        

    def crack(self):
        #点击验证按钮
        self.open()
        time.sleep(1)
        button=self.get_geetest_button()
        button.click()
        #获取验证码图片
        image1=self.get_geetest_image('captcha1.png')
        #点按呼出缺口
        slider=self.get_slider()
        slider.click()
        #获取带缺口的验证码图片
        image2=self.get_geetest_image('captcha2.png')
        #获取缺口位置
        gap=self.get_gap(image1,image2)
        print('缺口位置',gap)
        # 减去缺口位移
        gap -= BORDER
        #获取移动轨迹
        track=self.get_track(gap)
        print('滑动轨迹', track)
        #拖动滑块
        self.move_to_gap(slider,track)
        success=self.wait.until(
           EC.text_to_be_present_in_element((By.CLASS_NAME,'geetest_success_radar_tip_content'),'验证成功'))
        print(success)
        #失败后重试
        if not success:
            self.crack()
        else:
            self.login()

if __name__ == '__main__':
    crack=CrackGeetest()
    crack.crack()




