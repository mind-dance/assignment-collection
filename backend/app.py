import os
import json
from flask import Flask, jsonify, request
from flask_cors import CORS
from tools import Tools

app = Flask(__name__)
CORS(app)  # 这行代码启用了CORS，允许来自任何源的请求
# 初始化
t = Tools()
os.chdir(t.same_path)

# 如果有预设就读取
if os.path.exists("config.json"):
    t.get_config()

# 欢迎
@app.route('/api/welcome/', methods = ['GET'])
def welcome():
    return jsonify({"message": "道爷我成啦！"})

# 添加目标路径
@app.route("/api/target/", methods = ['GET', "POST"])
def load_target():
    if request.method == 'POST':
        t.target_path = request.args.get("path")
        t.set_config()
        return "ok", 200
    else:
        out = t.target_path
        return out, 200

# 列出目标文件夹下的所有文件名
@app.route("/api/read-filenames/", methods = ["get"])
def read_filenames():
    out = t.read_filenames(t.target_path)
    return jsonify(out)

# 添加模板
@app.route("/api/template", methods = ["PUT"])
def load_template(template):
    '''输入模板'''
    t.template = template
    return "ok"

# 查看作业完成情况，返回done，miss，error列表
@app.route("/api/check", methods = ["GET"])
def check():
    error_list = t.check_hw()
    etc = t.read_error_list(error_list)
    out = {"done":t.get_done, "miss":t.get_miss, "etc":etc}
    return jsonify(out)

# 打开文件
@app.route("/api/open", methods = ["GET"])
def open_file(sid):
    hw = t.db.get_s_hw(sid)
    path = t.get_path(hw)
    os.system(f'start {path}')  # 对于Windows系统
    return "ok"

# 导出名单
@app.route("/api/export", methods = ["GET"])
def export():
    return "ok"