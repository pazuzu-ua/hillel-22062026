def calculate(x, y):
    result = x + y
    return result


def process(data):
    if data is None:
        return
    for i in data:
        print(i)


class myClass:
    def __init__(self):
        self.value = 1
