import sqlite3
import os
import re
import csv

def not_exist():
        # 删除demo.db文件
    if os.path.exists('demo.db'):
        os.remove('demo.db')

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


class Database():

    def __init__(self, db = "demo.db"):
        self.con = sqlite3.connect(db)
        self.cur = self.con.cursor()

    

    def update_status_by_filename(self, filename):
        '''按文件名，更新数据库中的状态'''
        self.cur.execute("UPDATE submits SET status = 1 WHERE hw = ?", (filename,))
        self.con.commit()

    def read_sname_by_sid(self,sid):
        '''按学号读取姓名'''
        self.cur.execute("SELECT sname FROM students WHERE sid = ?", (sid,))
        sname = self.cur.fetchone()
        if sname:
            return sname[0]
        else:
            return None

    def read_hw_by_sid(self, sid):
        '''按学号读取文件名'''
        
        hw =  self.cur.execute("SELECT hw FROM submits WHERE sid = ?", (sid,))
        hw = self.cur.fetchone()
        if hw:
            return hw[0]
        else:
            return None

    def read_status_by_sid(self, sid):
        '''按学号读取状态'''
        status = self.cur.execute("SELECT status FROM submits WHERE sid = ?", (sid,))
        status = self.cur.fetchone()
        if status:
            return status[0]
        else:
            return None
    
    def create_hw(self, sid, template):
        '''给定模板和学生id，生成文件名并插入数据库'''
        sdict = {"sid": sid, "sname": self.read_sname_by_sid(sid)}
        hw = generate_target_filename(sdict, template)
        print(hw)
        self.cur.execute("INSERT INTO submits (sid, hw) VALUES (?, ?)", (sid, hw))
        self.con.commit()


        # 构建查询语句
    def import_csv(self, csvfile, table):
        '''导入表格，需要负责异常捕捉'''
        # 清空表格
        self.cur.execute("DELETE FROM " + table)
        try:
            # 打开csv文件
            with open(csvfile, 'r', encoding='utf-8-sig') as f:
                reader = csv.reader(f)
                # 读取字段
                fields = next(reader)
                print(fields)
                query = self.make_insert(table, fields)
                for row in reader:
                    # 构建查询语句并执行
                    self.cur.execute(query,row)
                # 提交事务
                self.con.commit()
        # 捕捉异常，例如找不到字段无法插入等。
        except Exception as e:
            print(f"出错了: {e}")

        # 参考了cs50包含从句的query语句构建教程
    # https://cs50.readthedocs.io/libraries/cs50/python/#how-can-i-add-optional-clauses-to-a-query
    def make_insert(self, table: str, fields: list):
        '''构建插入语句，需要输入目标表，字段名，会检验字段名、表名是否合法，但是不会检测字段名是否应该出现在表中,由执行函数捕捉错误进行异常处理'''
        # 检查表是否合法
        if table not in ["students", "submits"]:
            raise ValueError("表名有误")
        query = "INSERT INTO " + table
        clauses = []
        for i in fields:
            if i in ["sid", "sname", "hw", "status", "path"]:
                clauses.append("?")
            else:
                raise ValueError("字段名有误")
        if clauses:
            query = query + " (" + ", ".join(fields) + ") VALUES (" + ", ".join(clauses) + ")"
        return query