from flask import Blueprint, jsonify,request
from db import get_conn

user_bp = Blueprint(
    "user",
    __name__,
    url_prefix="/user"
)

#회원 전체 조회
@user_bp.route("/all",methods=['GET'])
def all_users():
   #회원 전체 조회
   try:
      conn = get_conn()
      cursor = conn.cursor()
      cursor.execute("SELECT * FROM `user`")
      users = cursor.fetchall()
      conn.close()
      return jsonify({
         "success": True,
         "message": "모든 사용자 조회 완료",
         "users": users
      })
   except Exception as e:
      return jsonify({
         "success": False,
         "message": "모든 사용자 조회 실패",
         "error": str(e)
      }), 500

# 회원 생성
@user_bp.route("/create",methods=['POST'])
def create_user():
   try:
      id = request.json.get('id')
      pw = request.json.get('pw')
      nick = request.json.get('nick')
      conn = get_conn()
      cursor = conn.cursor()
      cursor.execute(
     "INSERT INTO `user` (id, pw, nick) VALUES (%s, %s, %s)",
      (id, pw, nick))
      conn.commit()
      conn.close()
      return jsonify({
         "success": True,
         "message": "회원 생성 완료"
      })
   except Exception as e:
      return jsonify({
         "success": False,
         "message": "회원 생성 실패",
         "error": str(e)
      }), 500

#닉네임 수정
@user_bp.route("/update-nick",methods=['POST'])
def update_nick():
   try:
      idx = request.json.get('idx')
      nick = request.json.get('nick')
      conn = get_conn()
      cursor = conn.cursor()
      cursor.execute("UPDATE `user` SET nick = %s WHERE idx = %s", (nick, idx))
      conn.commit()
      conn.close()
      return jsonify({
         "success": True,
         "message": "닉네임 수정 완료"
      })
   except Exception as e:
      return jsonify({
         "success": False,
         "message": "닉네임 수정 실패",
         "error": str(e)
      }), 500

# 회원 삭제
@user_bp.route("/delete",methods=['POST'])
def delete_user():
   idx = request.json.get('idx')
   conn = get_conn()
   cursor = conn.cursor()
   cursor.execute("DELETE FROM `user` WHERE idx = %s", (idx))
   conn.commit()
   conn.close()
   return jsonify({
      "success": True,
      "message": "회원 삭제 완료"
   })