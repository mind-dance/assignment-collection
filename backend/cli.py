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
    warning = []
    actual = utils.list_actual_filename("tests/actual")
    # 对于列表中的每一文件名
    for filename in actual:
        # 检查是否已在数据库中登记
        flag = db.check_file(filename)
        # 如果已登记，更新状态
        if flag:
            db.update_status_by_filename(filename)
        else:
            warning.append(filename)
    return warning

def f_fix(warning):
    '''
    修正文件名
    '''
    change = []
    error = []
    for filename in warning:
        # 如果包含学号，重命名文件并更新状态
        try:
            sid = utils.search_sid_in_filename(filename, 8)
            # 查找文件名
            target = db.read_hw_by_sid(sid)
            change.append((filename, target))
            # 重命名
            os.rename("tests/actual/" + filename, "tests/actual/" + target)
            # 更新状态
            db.update_status_by_filename(target)
        # 如果不包含学号，记录警告
        except ValueError:
            error.append(filename)
    return error, change

# 删除demo.db文件
if os.path.exists('backend/data/demo.db'):
    os.remove('backend/data/demo.db')

if __name__ == '__main__':
    db = utils.Database()
    while True:
        menu = '''
    初始化：init
    生成hw：create
    列出所有文件名：list
    检查文件名：check
    搜索正确文件名：search
    修正文件名：fix
    统计作业提交情况：dash
    退出：exit
        '''
        command = input(menu)
        if command == 'init':
            f_init()
        elif command == 'create':
            f_create()
        elif command == 'list':
            print(utils.list_actual_filename("tests/actual"))
        # elif command == 'search':
        #     target = input("输入目标文件名：")
        #     print(utils.search_actual_filename_list(target, utils.list_actual_filename("tests/actual")))
        elif command == 'check':
            print(f_check())
        elif command == 'fix':
            warning = f_check()
            error, change = f_fix(warning)
            if error:
                print(f"未知文件：{error}")
            if change:
                for item in change:
                    print(f"修改：{item[0]} -> {item[1]}")
        elif command == 'dash':
            submit_list, empty_list = db.dash()
            if submit_list:
                print("\n已提交：\n")
                for item in submit_list:
                    print(item[1])
            if empty_list:
                print("\n未提交：\n")
                for item in empty_list:
                    print(item[1])
        elif command == 'exit':
            break