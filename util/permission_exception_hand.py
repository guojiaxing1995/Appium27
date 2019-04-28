#coding=utf-8
"""
@Time    : 2019/4/24 20:50
@Author  : 郭家兴
@Email   : 302802003@qq.com
@File    : permission_exception_hand.py
@Desc    : 主要功能是对未授权的情况做容错处理
"""
import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from util.get_by_local import GetByLocal

def authorize(num=1):
    """
    装饰器的作用是对在需要授权的地方做容错处理，进行授权。被装饰方法的当前实例对象必须要有driver属性
    args[0]  这里是self
    :param num:需要授予的权限个数
    :return:
     """
    def middle(func):
        def wrapper(*args,**kwargs):
            try:
                func(*args,**kwargs)
            except Exception:
                getByLocal = GetByLocal(args[0].driver)
                #判断授权按钮是否可见，如果存在则点击授权按钮
                for n in range(num):
                    try:
                        allow_button_a = WebDriverWait(args[0], 2, 0.1).until(EC.visibility_of(getByLocal.get_element('login_element','allowButtonA')))
                        allow_button_a.click() if allow_button_a else ''
                    except Exception:
                        pass
                for n in range(num):
                    try:
                        allow_button_b = WebDriverWait(args[0], 2, 0.1).until(EC.visibility_of(getByLocal.get_element('login_element', 'allowButtonB')))
                        allow_button_b.click() if allow_button_a else ''
                    except Exception:
                        pass

                time.sleep(2)
                func(*args, **kwargs)

        return wrapper

    return middle