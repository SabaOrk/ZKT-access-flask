from flask import Flask, request, jsonify
from main import add_user, delete_user

app = Flask(__name__)


@app.route('/controller/disable/')
def disable():
    card = request.args.get('card')
    res = delete_user(card=card)
    return jsonify({
        "success": res,
    })

@app.route('/controller/enable/')
def enable():
    card = request.args.get('card')
    res = add_user(card=card)
    return jsonify({
        "success": res,
    })


if __name__ == '__main__':
    app.run()
