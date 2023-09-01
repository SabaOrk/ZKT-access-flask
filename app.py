from flask import Flask, request, jsonify
from main import add_user, delete_user, get_users

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "success": True
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
    res = add_user(card=card, pin=pin, ip=ip, port=port)
    return jsonify({
        "success": res,
    })

    
@app.route('/controller/user/remove/', methods = ['POST'])
def remove_user():
    body = request.json
    card = body.get('card')
    pin = body.get('pin')
    ip = body.get('ip')
    port = body.get('port')
    res = delete_user(card, pin, ip, port)
    return jsonify({
        "success": res,
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
