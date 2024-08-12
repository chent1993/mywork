import os
import time

import yaml

from app_po.conftest import project_path
from app_po.utils.log_util import logger


class Utils:

    @classmethod
    def get_file_path(cls, path_name):
        '''
        获取文件的绝对路径
        :param path_name: 文件在项目中的相对路径
        :return:
        '''
        path = os.sep.join([project_path, path_name])
        logger.info(f"文件的绝对路径为 {path}")
        return path

    @classmethod
    def get_yaml_data(cls, yaml_path):
        '''
        读取 yaml 文件数据
        :param yaml_path: yaml 文件的路径
        :return:
        '''
        with open(yaml_path, encoding="utf-8") as f:
            datas = yaml.safe_load(f)
        logger.info(f"yaml 文件内容为 {datas}")
        return datas

    @classmethod
    def get_current_time(cls):
        """
        获取当前的日期与时间
        :return:
        """
        return time.strftime("%Y-%m-%d-%H-%M-%S")

    @classmethod
    def save_source_datas(cls, source_type):
        '''
        保存文件
        :param source_type: 文件类型，images 为图片，pagesource 为页面源码
        :return:
        '''
        if source_type == "images":
            end = ".png"
            _path = "images"
        elif source_type == "pagesource":
            end = "_page_source.xml"
            _path = "page_source"
        else:
            return None
        # 以当前时间命名
        source_name = Utils.get_current_time() + end
        # 拼接当前要输出的路径
        source_dir_path = os.sep.join([project_path, _path])
        # 资源目录如果不存在则新创建一个
        if not os.path.isdir(source_dir_path):
            os.mkdir(source_dir_path)
        # 拼接资源保存目录
        source_file_path = os.sep.join([source_dir_path, source_name])
        # 返回保存的路径
        return source_file_path
