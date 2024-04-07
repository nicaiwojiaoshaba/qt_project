import random


def generate_unique_random_numbers(minNum, maxNum, count):
    # 初始化一个集合存储随机数
    unique_numbers = set()

    while len(unique_numbers) < count:
        # 生成一个随机数
        random_number = random.randint(minNum, maxNum)
        # 讲随机数添加到集合中
        unique_numbers.add(random_number)

    # 讲集合转换成列表返回
    return list(unique_numbers)
