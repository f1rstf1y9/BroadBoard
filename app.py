from pymongo import MongoClient
from flask import Flask, render_template, jsonify, request
app = Flask(__name__)
client = MongoClient('mongodb://dice:dice4@15.164.214.224/', 27017)
db = client.list_number_2
## HTML 화면 보여주기
@app.route('/')
def homework():
    return render_template('index.html')
# 목록보기(Read) API
# @app.route('/search', methods=['GET'])
# def show():
#     games = list(db.getCollection('gamelist').find({},{'_id':False}))
#     return jsonify({'all_games':games})
@app.route('/search', methods=['GET'])
def view_games():
    games = list(db.newgamelist.find({}, {'_id': False}))
    return jsonify({'all_games': games})


## 회원 관리용
@app.route('/member', methods=['POST'])
def input_member():
    id_receive = request.form['id_give']
    pwd_receive = request.form['pwd_give']

    doc = {
        'id': id_receive,
        'pwd': pwd_receive
    }
    db.imsi_member.insert_one(doc)

    return jsonify({'msg': '가입을 축하합니다! 로그인 창으로 이동합니다.'})

@app.route('/member', methods=['GET'])
def read_members():
    members = list(db.imsi_member.find({}, {'_id':False}))
    return jsonify({'all_members':members})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)