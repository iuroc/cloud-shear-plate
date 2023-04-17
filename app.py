from flask import Flask, render_template, request, redirect
import sqlite3
from datetime import datetime
import random

app = Flask(__name__)


def init_db():
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    cursor.execute(
        '''CREATE TABLE IF NOT EXISTS "data" (
        "text" TEXT,
        "update_at" DATETIME,
        "id" INT PRIMARY KEY
    )'''
    )
    return conn, cursor


def get_new_id():
    conn, cursor = init_db()
    id_len = 6
    _id = random.randint(10 ** (id_len - 1), 10**id_len - 1)
    cursor.execute('SELECT * FROM "data" WHERE "id" = ?', (_id,))
    if cursor.fetchone():
        return get_new_id()
    return _id


@app.route('/')
def index():
    _id = request.args.get('id')
    if not _id:
        _id = get_new_id()
        return redirect(f'/?id={_id}')
    return render_template('index.html', id=_id)


@app.route('/save', methods=['POST'])
def save():
    text = request.form.get('text')
    _id = request.form.get('id')
    if not _id:
        return {'success': False, 'msg': '参数 id 缺失'}
    conn, cursor = init_db()
    cursor.execute('SELECT * FROM "data" WHERE "id" = ?', (_id,))
    time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    if not cursor.fetchone():
        sql = 'INSERT INTO "data" VALUES (?, ?, ?)'
    else:
        sql = 'UPDATE "data" SET "text" = ?, "update_at" = ? WHERE "id" = ?'
    cursor.execute(sql, (text, time, _id))
    conn.commit()
    cursor.close()
    conn.close()
    return 'ok'


@app.route('/get')
def get():
    _id = request.args.get('id')
    if not _id:
        return {'success': False, 'msg': '参数 id 缺失'}
    conn, cursor = init_db()
    sql = 'SELECT * FROM "data" WHERE "id" = ?'
    cursor.execute(sql, (_id,))
    result = cursor.fetchone()
    if not result:
        return {'success': False, 'msg': '数据库没有该记录'}
    return {'text': result[0], 'update_at': result[1], 'id': result[2], 'success': True}


if __name__ == "__main__":
    app.run('0.0.0.0')
