import sqlite3

class Database():

    def __init__(self, db = "demo.db"):
        self.con = sqlite3.connect(db)
        self.cur = self.conn.cursor()

    def update_status_by_filename(self, filename):
        # 接受文件名，更新数据库中的状态
        self.cur.execute("UPDATE submits SET status = 1 WHERE hw = ?", (filename,))
        self.con.commit()


    def read_hw_by_sid(self, sid):
        hw =  self.cur.execute("SELECT hw FROM submits WHERE sid = ?", (sid,))
        return hw

    def read_status_by_sid(self, sid):
        status = self.cur.execute("SELECT status FROM submits WHERE sid = ?", (sid,))
        return status
    
    def create_hw(self, sid, hw):
        self.cur.execute("INSERT INTO submits (sid, hw) VALUES (?, ?)", (sid, hw))
        self.con.commit()