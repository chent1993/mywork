# _*_ coding: utf-8 _*_
# @Time : 2024/8/25 18:14 
# @Author : tian
# @File : jsonschema_util.py
# @desc :
import json

from genson import SchemaBuilder
from jsonschema import validate

class JSONSchemaUtils:
    @classmethod
    def validate_schema_by_file(cls, data_obj, schema_file):
        with open(schema_file) as f:
            schema_data = json.load(f)
        return cls.validate_schema(data_obj, schema_data)

    @classmethod
    def validate_schema(cls, data_obj, schema):
        """
        通过schema验证数据
        """
        # 问题，在实际使用的过程中，不想直接抛出错误，而是返回是否成功的标志（T 或 F）
        try:
            validate(data_obj, schema=schema)
            return True
        except Exception as e:
            # log()
            print(f"结构体验证失败，失败原因是{e}")
            return False



    @classmethod
    def generate_jsonschema_by_file(cls, obj, file_path):
        json_schema_data = cls.generate_jsonschema(obj)
        with open(file_path, "w") as f:
            json.dump(json_schema_data, f)

    @classmethod
    def generate_jsonschema(cls, obj):
        """
        生成jsonschema 数据
        """
        # 实例化 SchemaBuilder 类
        builder = SchemaBuilder()
        # 调用 add_object 方法，将要转换成jsonschema的数据传入进去
        builder.add_object(obj)
        # 转成schema结构
        return builder.to_schema()


# 定义一个 JSON 对象
obj = {
    "greeting": "Welcome to quicktype!",
    "instructions": [
        "Type or paste JSON here",
        "Or choose a sample above",
        "quicktype will generate code in your",
        "chosen language to parse the sample data"
    ]
}

# 生成 JSON schema
schema = JSONSchemaUtils.generate_schema(obj)

# 打印生成的 JSON schema
print(schema)

# 准备要验证的对象
obj_to_validate = {
    "greeting": "Hello, World!",
    "instructions": [
        "Type or paste JSON here",
        "Or choose a sample above"
    ]
}

# 验证对象与生成的 JSON schema 结构一致性
is_valid = JSONSchemaUtils.schema_validate(obj_to_validate, schema)

if is_valid:
    print("Object is valid according to JSON schema.")
else:
    print("Object is not valid according to JSON schema.")