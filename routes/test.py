from flask import Blueprint, jsonify 
from flask import request

#blueprint 생성
test_bp = Blueprint(
    "test",
    __name__,
    url_prefix="/test"
)

#1. path parameter - URL 경로 자체에 포함되는 값
@test_bp.route("/lionkoreaofficial/<shopid>" )
def find_user(shopid):
    print(f"User ID: {shopid}")
    return f"User ID: {shopid}"

#2. query parameter - URL 뒤에 ?key=value 형태로 붙는 값
# 종류로는 GET, POST, PUT, DELETE, PATCH, HEAD, OPTIONS 등이 있다
@test_bp.route("/find_item", methods=['GET'])
def find_item():
    name = request.args.get("name")
    price = request.args.get("price")
    seller = request.args.get("seller")
    print(f"Item Name: {name}")
    print(f"Item Price: {price}")
    print(f"Item Seller: {seller}")
    return f"Item Name: {name}, Item Price: {price}, Item Seller: {seller}"
#http://127.0.0.1:5000/find_item?name=노트북&price=1000000 이렇게 &로 계속 늘려가면 된다

#3. request body - 주로 POST 방식으로 요청을 받을 때 사용
@test_bp.route("/save_item", methods=['POST'])
def save_item():
    
    name = request.json.get("name")
    price = request.json.get("price")
    seller = request.json.get("seller")
    print(f"Item Name: {name}")
    print(f"Item Price: {price}")
    print(f"Item Seller: {seller}")
    return f"Item Name: {name}, Item Price: {price}, Item Seller: {seller}"
