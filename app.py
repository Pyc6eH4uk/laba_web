from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

users = []


@app.errorhandler(404)
def error_handler(error):
    return '<h1>Hello, World</h1>!', 200


@app.route('/')
def index():
    name = request.args.get('name', 'Default name')
    return render_template('name.html', name=name), 200


@app.route('/user', methods=['GET', 'POST'])
def users_name():
    global users
    if request.method == 'GET':
        return render_template('users.html', users=users)
    if request.method == 'POST':
        name = request.form['name']
        users.append(str(name))
        return jsonify({'Success': 200}), 200


if __name__ == '__main__':
    app.run(debug=True)
