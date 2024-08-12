import os
import sys

from app_po.utils.log_util import logger

# 获取当前项目的绝对路径
project_path = os.path.dirname(os.path.abspath(__file__))
logger.info(f"当前项目绝对路径为 {project_path}")
# 把项目路径添加到环境变量
sys.path.append(project_path)
