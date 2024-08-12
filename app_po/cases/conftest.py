
# 解决用例描述中中文乱码的问题
def pytest_collection_modifyitems(
        session, config, items
) -> None:
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')
