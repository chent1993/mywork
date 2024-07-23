
pytest -vs web_auto/test01_wework.py  --alluredir=./result --clean-alluredir

allure serve ./result
