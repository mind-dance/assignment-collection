import os
import re
# import db

def generate_target_filename(sdict, template):
    '''生成单一一个文件名
    输入学生字典和模板
    '''
    # 替换模板中的占位符
    filename = template
    for ph, val in sdict.items():
        filename = filename.replace("${" + ph + "}", val)
    return filename


def list_actual_filename(path):
    file_list = []
    # 列出所有文件与子文件夹
    items = os.listdir(path)
    # 过滤出文件
    for item in items:
        if os.path.isfile(os.path.join(path, item)):
            file_list.append(item)
    # 返回所有文件名
    return file_list


def search_actual_filename_list(target_filename, actual_filename_list):
    flag = False
    if target_filename in actual_filename_list:
        flag = True
    return flag


def search_sid_in_filename(filename, len=12):
    pat = re.compile(f"\\d{{{len}}}")
    match = re.search(pat, filename)
    # 如果找到学号
    if match:
        return match.group(0)
    else:
        raise ValueError("未找到学号")


def rename_file(path, newname):
    os.chdir(path)
    os.rename(path, newname)

while True:
    menu = '''
生成文件名：create
列出所有文件名：list
查找文件名是否包含在生成文件名中：search
    '''
    command = input(menu)
