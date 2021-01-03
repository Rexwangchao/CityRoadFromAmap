import itertools
import random


# 数据加载器
def loader(file):
    try:
        data_file = open(file, 'r', encoding='utf8')
    except UnicodeDecodeError:
        data_file = open(file, 'r', encoding='gbk')
    except FileExistsError:
        print("文件不存在！")
        return
    data = []
    for line in data_file.readlines():
        data.append(line.strip())
    data_file.close()
    return data


# 数据保存
def saver(data, file_path, encoding='utf8'):
    with open(file_path, 'w+', encoding=encoding) as file:
        for d in data:
            file.write(str(d).strip() + '\n')
    print("Total %s row(s) data has been saved." % len(data))
