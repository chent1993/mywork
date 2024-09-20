from datetime import datetime
import subprocess

# 获取当前日期并格式化
today = datetime.now().strftime('%Y%m%d')
# 设置 Allure 结果目录
alluredir = f'./allure-results/{today}'

# 构建 pytest 命令
pytest_command = f'pytest --env test --alluredir={alluredir}'
# 构建 allure generate 命令
allure_generate_command = f'allure generate {alluredir} -o ./allure-report/{today} --clean'

'''
subprocess.run() 是 Python 3.5 及以上版本中引入的 subprocess 模块的一个函数，用于执行外部命令和程序
'''


try:
    # 执行 pytest 命令
    subprocess.run(pytest_command, shell=True, check=True)
    # 执行 allure generate 命令以生成静态 HTML 报告
    subprocess.run(allure_generate_command, shell=True, check=True)

except subprocess.CalledProcessError as e:
    print(f" 执行失败: {e}")


# 现在静态 HTML 报告应该已经生成在 ./allure-report 目录下
print("静态 HTML 报告生成成功。")