# Appium27
python + appium 移动端自动化

python版本采用python2.7，appium版本为1.8.1。项目框架支持多台安卓手机同时进行自动化测试，一键自动化，无需手动启动服务。一次测试执行会生成报告并附带错误截图，同时保存
appium的log方便快速定位问题。


![测试报告](https://github.com/guojiaxing1995/Appium27/blob/master/img/readme报告.png)


项目采用分层自动化的设计思想，分为元素层、操作层、业务层和用例层。用例层可以看作一条用例的入口，用例层调用业务层方法，业务层调用操作层，操作层调用元素层，
元素层获取页面元素，定位信息写在配置文件中。


![项目目录结构](https://github.com/guojiaxing1995/Appium27/blob/master/img/项目目录结构1.png)






_项目删除了apk安装包和部分代码_

