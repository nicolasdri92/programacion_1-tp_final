def isValid(list: list, value: str) -> bool:
    for item in list:
        if (item['id'] == value):
            return True
    return False