
pytest -vs web_auto/test01_wework.py  --alluredir=./result --clean-alluredir

allure serve ./result


20240721-用户端Web自动化测试-课后作业    web_auto/test01_wework.py 
20240728 用户端 Web 自动化测试实战 一 作业  web_po


安装了 pytest-allure-adaptor 后，执行测试用例报错：AttributeError: module 'allure' has no attribute 'severity_level'
原因：
因为之前已经安装了 allure-pytest

解决：
卸载 pytest-allure-adaptor

pip uninstall pytest-allure-adaptor
pip install allure-pytes