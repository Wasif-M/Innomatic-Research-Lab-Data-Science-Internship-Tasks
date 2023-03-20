from flask import Flask, request

app = Flask(__name__)

@app.route('/task')
def index():
    name = request.args.get('name', '')
    uppercase_name = name.upper()
    return f'Hello, {uppercase_name}!'

if __name__ == '__main__':
    app.run(debug=True)