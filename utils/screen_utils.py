# _*_ coding: utf-8 _*_
'''
封装截图方法，并结合allure报告
'''
import time
import allure
class ScreenUtil:
    def get_screen(self,driver):
        #todo:手动创建images目录
        timestamp = int(time.time())
        image_path = f"./images/image_{timestamp}.PNG"
        #截图
        driver.save_screenshot(image_path)
        #结合allure报告
        allure.attach.file(image_path,name="picture",attachment_type=allure.attachment_type.PNG)