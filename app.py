from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return jsonify({"message": "Hello, World!"})

@app.route('/api/hello')
def hello_api():
    return jsonify({"message": "Hello from Azure API!"})

@app.route('/api/hello/<name>')
def hello_name(name):
    return jsonify({"message": f"Hello, {name}!"})

if __name__ == '__main__':
    app.run(debug=True)