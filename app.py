from flask import Flask, request, jsonify
from main import add_user, delete_user, get_users, ping_host_endpoint
from queue_manager import add_request
import sys
from datetime import datetime
import pytz

app = Flask(__name__)

def get_local_time():
    tz = pytz.timezone('Asia/Tbilisi')
    return datetime.now(tz).strftime('%Y-%m-%d %H:%M:%S')

@app.route('/')
def home():
    print(f"[{get_local_time()}] Server received an empty request")
    with open('output.txt', 'a') as output:
        output.write(f"[{get_local_time()}] Server received an empty request" + "\n")
    return jsonify({
        "success": True
    })

@app.route('/ping/', methods = ['POST'])
def ping_host():
    body = request.json
    ip = body.get('ip')
    res = ping_host_endpoint(ip)
    print(f"[{get_local_time()}] Ping successful on host: {ip}")
    with open('output.txt', 'a') as output:
        output.write(f"[{get_local_time()}] Ping successful on host: {ip}" + "\n")
    return jsonify({
        "success": res,
    })

@app.route('/controller/user/set/', methods = ['POST'])
def set_user():
    body = request.json
    card = body.get('card')
    pin = body.get('pin')
    ip = body.get('ip')
    port = body.get('port')
    doors = body.get('doors')
    print(f"[{get_local_time()}] Recieved request to add user with card: {card} and pin: {pin}")
    with open('output.txt', 'a') as output:
        output.write(f"[{get_local_time()}] Recieved request to add user with card: {card} and pin: {pin}" + "\n")
    res = add_user(card=card, pin=pin, ip=ip, port=port, doors=doors)
    
    return jsonify({
        "success": True,
        "message": "Added user successfully" if res else "Failed to add user",
    })

    
@app.route('/controller/user/remove/', methods = ['POST'])
def remove_user():
    body = request.json
    card = body.get('card')
    pin = body.get('pin')
    ip = body.get('ip')
    port = body.get('port')
    print(f"[{get_local_time()}] Recieved request to remove user with card: {card} and pin: {pin}")
    with open('output.txt', 'a') as output:
        output.write(f"[{get_local_time()}] Recieved request to remove user with card: {card} and pin: {pin}" + "\n")
    res = delete_user(card=card, pin=pin, ip=ip, port=port)
    
    return jsonify({
        "success": True,
        "message": "Removed user successfully" if res else "Failed to remove user",
    })
    
@app.route('/controller/users/', methods = ['POST'])
def users():
    body = request.json
    ip = body.get('ip')
    port = body.get('port')
    res = get_users(ip, port)
    print(f"[{get_local_time()}] Returned {len(res)} users from host: {ip}")
    with open('output.txt', 'a') as output:
        output.write(f"[{get_local_time()}] returned {len(res)} users from host: {ip}" + "\n")
    return jsonify({
        "users": res,
    })

if __name__ == '__main__':
    app.run(debug=True)


# @app.route('/controller/disable/')
# def disable():
#     body = request.json
#     ip = body.get('ip')
#     port = body.get('port')
#     #TODO
#     return jsonify({
#         "success": res,
#     })

# @app.route('/controller/enable/')
# def enable():
#     body = request.json
#     ip = body.get('ip')
#     port = body.get('port')
#     #TODO
#     return jsonify({
#         "success": res,
#     })
    
    
# @app.route('/controller/restart/')
# def restart():
#     body = request.json
#     ip = body.get('ip')
#     #TODO
#     return jsonify({
#         "success": res,
#     })
