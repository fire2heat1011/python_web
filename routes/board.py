# 외래 키를 받아서 게시판 글을 작성하고 전체 글을 조회하는 기능을 구현한다.

from flask import Blueprint, jsonify,request
from db import get_conn

board_bp = Blueprint(
    "board",
    __name__,
    url_prefix="/board"
)


# 게시판 글 쓰기
@board_bp.route("/write",methods=['POST'])
def write_board():
   try:
      user_idx = request.json.get('user_idx')
      title = request.json.get('title')
      content = request.json.get('content')
      conn = get_conn()
      cursor = conn.cursor()
      cursor.execute("INSERT INTO `board` (user_idx, title, content, created_at) VALUES (%s, %s, %s, NOW())", (user_idx, title, content))
      conn.commit()
      conn.close()
      return jsonify({
        "success": True,
        "message": "게시판 글 쓰기 완료"
      })
   except Exception as e:
      return jsonify({
        "success": False,
        "message": "게시판 글 쓰기 실패",
        "error": str(e)
      }), 500

# 게시판 전체 글 조회
@board_bp.route("/list",methods=['GET'])
def list_boards():
   try:
      conn = get_conn()
      cursor = conn.cursor()
      cursor.execute("SELECT * FROM `board`")
      boards = cursor.fetchall()
      conn.close()
      return jsonify({
        "success": True,
        "message": "게시판 전체 글 조회 완료",
        "boards": boards 
        })
   except Exception as e:
      return jsonify({
        "success": False,
        "message": "게시판 전체 글 조회 실패",
        "error": str(e)
      }), 500