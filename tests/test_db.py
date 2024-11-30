import unittest
import csv
import os
from backend.db import *


class TestDb(unittest.TestCase):
    def import_csv(self, csvfile, table):
        '''导入表格，需要负责异常捕捉'''
        # 清空表格
        self.cur.execute("DELETE FROM " + table)
        try:
            # 打开csv文件
            with open(csvfile, 'r', encoding='utf-8') as f:
                reader = csv.reader(f)
                # 读取字段
                fields = next(reader)
                query = self.make_insert(table, fields)
                for row in reader:
                    # 构建查询语句并执行
                    self.cur.execute(query,row)
                # 提交事务
                self.con.commit()
        # 捕捉异常，例如找不到字段无法插入等。
        except:
            print("出错了")
    
    def setUp(self):
        self.db = Database('backend/demo.db')
        self.import_csv("backend/data/students.csv", "students")
        self.import_csv("backend/data/submits.csv", "submits")


    def tearDown(self):
        pass

    def test_create_hw(self):
        # 20241112,20241112-薛维旭-清华拳.mp4,0
        self.db.create_hw(20241112, "20241112-薛维旭-清华拳.mp4")
        out = self.db.cur.execute("SELECT * FROM submits WHERE sid = ?", (20241112,))
        expected = [(20241112, "20241112-薛维旭-清华拳.mp4", 0)]
        self.assertEqual(expected, out)
    def test_update_status_by_filename(self):
        self.db.update_status_by_filename("20241112-薛维旭-清华拳.mp4")
        out = self.db.cur.execute("SELECT hw FROM submits WHERE sid = ?", (20241112,))
        expected = 1
        self.assertEqual(expected, out)