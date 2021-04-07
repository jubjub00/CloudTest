from flask import Flask
app = Flask(__name__)

@app.route('/')
def Home():
    return render_template("home.html")

# @app.route('/aboutUs')
# def aboutUs():
#     return render_template("about.html")

# @app.route('/john')
# def john():
#     return "<h1>Hello john.</h1>"

# @app.route('/welcome/<name>')
# def welcome(name):
#     return "<h1>welcome "+name+"</h1>"

if __name__ == '__main__':
    app.run(host='0.0.0.0',port = 80)