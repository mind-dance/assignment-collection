import utils
import os

def init():
    '''
    sql文件初始化数据库
    导入学生表
    '''
    with open('backend/data/init.sql', 'r', encoding='utf-8') as file:
        sql = file.read()
    db.cur.executescript(sql)
    db.import_csv('backend/data/students.csv', 'students')

def create():
    '''
    
    '''
    template = "${sid}-${sname}-清华拳.mp4"
    db.create_hw("20241111", template)
    db.create_hw("20241113", template)

def check():
    '''
    
    '''
    warn = []
    actual = utils.list_actual_filename("tests/actual")
    target = db.read_hw_by_sid("20241111")
    flag = utils.search_actual_filename_list(target, actual)
    if flag:
        db.update_status_by_filename(actual)
    else:
        warn.append(actual)
    return warn

def f_rename():
    sid = utils.search_sid_in_filename("20241113-沙袋-清华拳.mp4", 8)
    target = db.read_hw_by_sid(sid)
    utils.os.rename("tests/actual/20241113-沙袋-清华拳.mp4", "tests/actual/" + target)
    


# 删除demo.db文件
utils.not_exist()
db = utils.Database()
init()
create()
check()
f_rename()
# while True:
#     menu = '''
# 生成文件名：create
# 列出所有文件名：list
# 查找文件名是否包含在生成文件名中：search
#     '''
#     command = input(menu)
