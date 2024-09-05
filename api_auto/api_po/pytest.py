import subprocess
from datetime import datetime

today = datetime.now().strftime('%Y-%m-%d')
alluredir = f'./allure-results/{today}'

command = f'pytest --alluredir={alluredir}'
subprocess.run(command, shell=True, check=True)