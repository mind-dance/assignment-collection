import sqlite3

def execute_sql_file(database_name, sql_file_path):
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()
    try:
        with open(sql_file_path, 'r', encoding="utf-8") as sql_file:
            sql_commands = sql_file.read().split(';')
            for command in sql_commands:
                if command.strip():  # 跳过空语句
                    cursor.execute(command)
        conn.commit()
    except Exception as e:
        print(f"执行SQL文件出错: {e}")
        conn.rollback()
    finally:
        cursor.close()
        conn.close()


# 使用with语句创建一个名为new_file.txt的文件
with open("new_file.txt", "w") as file:
    # 这里可以对文件进行写入操作，不过在这个例子中没有写入内容，所以创建的是一个空文件
    pass
execute_sql_file("backend/demo.db", "backend/data/init.sql")

