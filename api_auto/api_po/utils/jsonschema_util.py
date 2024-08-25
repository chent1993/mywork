# _*_ coding: utf-8 _*_
# @Time : 2024/8/25 18:14 
# @Author : tian
# @File : jsonschema_util.py
# @desc :
from genson import SchemaBuilder
from jsonschema import validate

class JSONSchemaUtils:
    @classmethod
    def generate_schema(cls, obj):
        builder = SchemaBuilder()
        builder.add_object(obj)
        return builder.to_schema()

    @classmethod
    def schema_validate(cls, obj, schema):
        try:
            validate(instance=obj, schema=schema)
            return True
        except Exception as e:
            return False

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