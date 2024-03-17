from flask import Flask, request, jsonify
from main import add_user, delete_user, get_users, ping_host_endpoint
from queue_manager import add_request

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "success": True
    })

@app.route('/ping/', methods = ['POST'])
def ping_host():
    body = request.json
    ip = body.get('ip')
    res = ping_host_endpoint(ip)
    return jsonify({
        "success": res,
    })

@app.route('/controller/disable/')
def disable():
    body = request.json
    ip = body.get('ip')
    port = body.get('port')
    #TODO
    return jsonify({
        "success": res,
    })

@app.route('/controller/enable/')
def enable():
    body = request.json
    ip = body.get('ip')
    port = body.get('port')
    #TODO
    return jsonify({
        "success": res,
    })
    
    
@app.route('/controller/restart/')
def restart():
    body = request.json
    ip = body.get('ip')
    #TODO
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
    print("app", port)

    add_request(card=card, pin=pin, ip=ip, port=port, operation='add')
    
    return jsonify({
        "success": True,
        "message": "User creation request has been queued",
    })

    
@app.route('/controller/user/remove/', methods = ['POST'])
def remove_user():
    body = request.json
    card = body.get('card')
    pin = body.get('pin')
    ip = body.get('ip')
    port = body.get('port')
    print("app", port)

    add_request(card=card, pin=pin, ip=ip, port=port, operation='delete')
    
    return jsonify({
        "success": True,
        "message": "User deletion request has been queued",
    })
    
    
@app.route('/controller/users/', methods = ['POST'])
def users():
    body = request.json
    ip = body.get('ip')
    port = body.get('port')
    res = get_users(ip, port)
    return jsonify({
        "users": res,
    })

if __name__ == '__main__':
    app.run(debug=True)
