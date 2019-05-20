#coding=utf-8
"""
@Time    : 2019/5/19 21:35
@Author  : 郭家兴
@Email   : 302802003@qq.com
@File    : slide_find_element.py
@Desc    : 容错类装饰器，如果定位不到元素则通过滑动页面，再次定位元素
"""


def slide_up(num=1):
    """
    当前未定位到元素，则通过上划屏幕来定位元素.每滑动一次则定位一次，如果定位到则继续执行，达到滑动上限任未定位到则抛出异常
    :param num: 上划的次数
    :return:
    """
    def middle(fun):
        def wrapper(*args,**kwargs):
            try:
                fun(*args,**kwargs)
            except Exception:
                switch_flag = 0
                # 如果当前的context是h5则切换到原生
                if args[0].driver.view == "WEB":
                    context = args[0].driver.current_context
                    args[0].driver.switch_to.context('NATIVE_APP')
                    args[0].driver.view = 'NATIVE'
                    switch_flag = 1

                width, height = get_size(args[0].driver)
                for i in range(1,num+1):
                    # 如果当前的context是h5则切换到原生
                    if args[0].driver.view == "WEB":
                        context = args[0].driver.current_context
                        args[0].driver.switch_to.context('NATIVE_APP')
                        args[0].driver.view = 'NATIVE'
                        switch_flag = 1

                    args[0].driver.swipe(width / 2, height / 10 * 9, width / 2, height / 10 * 1, 2000)

                    # 如果之前进行过切换则切换回h5
                    if switch_flag == 1:
                        args[0].driver.switch_to.context(context)
                        args[0].driver.view = 'WEB'
                    #如果定位执行成功则跳出循环，未定位到则判断是不是最后一次滑动，如果是则手动抛出异常
                    try:
                        fun(*args, **kwargs)
                        break
                    except Exception:
                        if i == num:
                            raise RuntimeError(u'元素定位失败')

        return wrapper

    return middle


def slide_down(num=1):
    """
    当前未定位到元素，则通过下划屏幕来定位元素。每滑动一次则定位一次，如果定位到则继续执行，达到滑动上限任未定位到则抛出异常
    :param num: 上划的次数
    :return:
    """
    def middle(fun):
        def wrapper(*args,**kwargs):
            try:
                fun(*args,**kwargs)
            except Exception:
                switch_flag = 0
                # 如果当前的context是h5则切换到原生
                if args[0].driver.view == "WEB":
                    context = args[0].driver.current_context
                    args[0].driver.switch_to.context('NATIVE_APP')
                    args[0].driver.view = 'NATIVE'
                    switch_flag = 1

                width, height = get_size(args[0].driver)
                for i in range(1,num+1):
                    # 如果当前的context是h5则切换到原生
                    if args[0].driver.view == "WEB":
                        context = args[0].driver.current_context
                        args[0].driver.switch_to.context('NATIVE_APP')
                        args[0].driver.view = 'NATIVE'
                        switch_flag = 1

                    args[0].driver.swipe(width / 2, height / 10 * 1, width / 2, height / 10 * 9, 2000)

                    # 如果之前进行过切换则切换回h5
                    if switch_flag == 1:
                        args[0].driver.switch_to.context(context)
                        args[0].driver.view = 'WEB'
                    #如果定位执行成功则跳出循环，未定位到则判断是不是最后一次滑动，如果是则手动抛出异常
                    try:
                        fun(*args, **kwargs)
                        break
                    except Exception:
                        if i == num:
                            raise RuntimeError(u'元素定位失败')

        return wrapper

    return middle

def get_size(driver):
    '''获取屏幕尺寸'''
    width = driver.get_window_size()['width']
    height = driver.get_window_size()['height']

    return width, height
