

'''
自定义封装显示等待方法
多次点击元素，默认5次
'''
def click_exception(by,element,max_attempts=5):
    def _inner(driver):
        #实际点击次数
        actul_attempts = 0
        #当实际点击次数小于最大点击次数时
        while actul_attempts < max_attempts:
            actul_attempts += 1
            try:
                #如果点击报错，执行except逻辑，并且继续循环
                #如果点击没有报错，跳出循环，返回True
                driver.find_element(by,element).click()
                return True
            except Exception:
                print("点击时报错")

        #超出了最大点击次数
        raise Exception("超出了最大点击次数")

    return _inner