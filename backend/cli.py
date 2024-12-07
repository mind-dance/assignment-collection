import utils
import os

def f_init():
    '''
    sql文件初始化数据库
    导入学生表
    '''
    with open('backend/data/init.sql', 'r', encoding='utf-8') as file:
        sql = file.read()
    db.cur.executescript(sql)
    db.import_csv('backend/data/students.csv', 'students')

def f_create():
    '''
    创建目标文件名
    '''
    template = "${sid}-${sname}-清华拳.mp4"
    sids = db.read_all_sid()
    for sid in sids:
        db.create_hw(sid, template)

def f_check():
    '''
    检查文件并更新状态
    '''
    warn = []
    actual = utils.list_actual_filename("tests/actual")
    # 对于列表中的每一文件名
    for filename in actual:
        # 检查是否已在数据库中登记
        flag = db.check_file(filename)
        # 如果已登记，更新状态
        if flag:
            db.update_status_by_filename(filename)
        # 如果未登记，检查是否包含学号
        else:
            # 如果包含学号，重命名文件并更新状态
            try:
                sid = utils.search_sid_in_filename(filename, 8)
                # 查找文件名
                target = db.read_hw_by_sid(sid)
                # 重命名
                os.rename("tests/actual/" + filename, "tests/actual/" + target)
                # 更新状态
                db.update_status_by_filename(target)
            # 如果不包含学号，记录警告
            except ValueError:
                warn.append(filename)
    return warn


# 删除demo.db文件
if os.path.exists('backend/data/demo.db'):
    os.remove('backend/data/demo.db')

db = utils.Database()
f_init()
f_create()
warn = f_check()
if not warn:
    print("\nall is well.\n")
else:
    print(warn)
# while True:
#     menu = '''
# 生成文件名：create
# 列出所有文件名：list
# 查找文件名是否包含在生成文件名中：search
#     '''
#     command = input(menu)
