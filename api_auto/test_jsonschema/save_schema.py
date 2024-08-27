# _*_ coding: utf-8 _*_
# @Time : 2024/8/25 18:03 
# @Author : tian
# @File : save_schema.py
# @desc :

from genson import SchemaBuilder
obj = {"errcode":0,"errmsg":"ok","department_id":[{"id":220,"parentid":1,"order":1}]}
obj = {
	"errcode": 0,
	"errmsg": "ok",
	"next_cursor": "aaaaaaaaa",
	"dept_user": [
		{
			"open_userid": "woAAAAAAAA",
			"department": 1
		},
		{
			"open_userid": "woAAAAAAAA",
			"department": 2
		},
		{
			"open_userid": "woBBBBBBBB",
			"department": 2
		}
	]
}
obj2 ={"errcode":0,"errmsg":"ok","dept_user":[{"userid":"ChenTian","department":1},{"userid":"sanzhang","department":1},{"usrid":"HeXiuHua","department":1},{"userid":"LuKun","department":1},{"userid":"BaiHui2","department":1},{"userid":"WangJun","department":1},{"userid":"ChengXin","department":1},{"userid":"f9130386-1080-430a-b9d8-b32f0e7c1160","department":1},{"userid":"6762c400-a44a-456a-bc56-542ffb377ec8","department":1},{"userid":"2634363b-fd3d-4217-b8f7-f94f47a02c9f","department":1},{"userid":"b5855d64-4cac-4b3d-a991-30112daf441d","department":1},{"userid":"fe698a42-f089-42dd-92e5-36e20f4f7610","department":1},{"userid":"93ac09b7-c54e-40fe-b2b0-c8f5e8635f35","department":1},{"userid":"test","department":1},{"userid":"YanXiuRong","department":1},{"userid":"HePeng","department":1},{"userid":"ChenGuiXiang","department":1},{"userid":"ZhouXiuYun","department":1},{"userid":"XingJian","department":1},{"userid":"YeXiuLan","department":1},{"userid":"HuMing","department":1},{"userid":"GaoXiuMei","department":1},{"userid":"ChenJun","department":1},{"userid":"HuGuiFang","department":1},{"userid":"YangJuan","department":1},{"userid":"aa80773a-398f-480b-83e5-ecba68925574","department":1},{"userid":"371b3a53-5a71-4928-ac34-59c231417f17","department":1},{"userid":"35e42ba8-9b0d-4ac5-abc5-779db2f0aefb","department":1},{"userid":"tian","department":9},{"userid":"ShaYaTou","department":14},{"userid":"08931023fe2eaf1fa22a680c9af17a06","department":14},{"userid":"YangMeiMei","department":14},{"userid":"XuZong","department":14},{"userid":"ambition","department":14},{"userid":"PanYan","department":14},{"userid":"LiLi","department":14},{"userid":"GaoSaiFen","department":14},{"userid":"NiFengDeQiangWei","department":14},{"userid":"dde850a4-e123-4dec-98a5-7f298b4ef891","department":14}]}

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
schema2 = generate_jsonschema(obj2)

# 打印生成的 JSON schema
print(schema2)