# _*_ coding: utf-8 _*_
# @Time : 2024/8/25 21:36 
# @Author : tian
# @File : utils.py
# @desc :
import os

import yaml

from api_auto.api_po.utils.log_util import logger



class Utils:

    @classmethod
    def get_root_path(cls):
        root_path = os.path.dirname(os.path.abspath(__file__))
        return root_path


    # @classmethod
    # def get_file_path(cls, path_name):
    #     '''
    #     获取文件的绝对路径
    #     :param path_name: 文件在项目中的相对路径
    #     :return:
    #     '''
    #     path = os.sep.join([project_path, path_name])
    #     logger.info(f"文件的绝对路径为 {path}")
    #     return path

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
