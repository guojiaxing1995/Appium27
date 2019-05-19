#coding=utf-8
"""
@Time    : 2019/5/19 17:35
@Author  : 郭家兴
@Email   : 302802003@qq.com
@File    : switch_context_back.py
@Desc    : 装饰器作用为从h5切换到原生后切换回来，主要场景为在h5页面调用原生组件
"""
def switch_context_back(func):

    def wrapper(*args,**kwargs):
        if args[0].driver.view == "WEB":
            context = args[0].driver.current_context
            args[0].driver.switch_to.context('NATIVE_APP')
            args[0].driver.view = 'NATIVE'

            func(*args, **kwargs)

            args[0].driver.switch_to.context(context)
            args[0].driver.view = 'WEB'


    return wrapper