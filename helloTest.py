from flask import Flask
app = Flask(__name__)

@app.route('/')
def Home():
    return "<h1>Hello World</h1>"

@app.route('/test')
def test():
    return "<h1>Hello test 123</h1>"

if __name__ == '__main__':
    app.debug = True
    app.run(host='127.0.0.1', port=80)