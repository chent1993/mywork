# _*_ coding: utf-8 _*_
# @Time : 2024/8/25 18:03 
# @Author : tian
# @File : save_schema.py
# @desc :

from genson import SchemaBuilder
obj = {"errcode":0,"errmsg":"ok","department_id":[{"id":220,"parentid":1,"order":1}]}
def generate_jsonschema(obj):
    # 实例化jsonschem
    builder = SchemaBuilder()
    # 传入被转换的对象
    builder.add_object(obj)
    # 转换成 schema 数据
    return builder.to_schema()
schema = generate_jsonschema(obj)

# 打印生成的 JSON schema
print(schema)
