#!flask-sample/app.py

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hey, we have Flask in a Docker container! \n Hello World!'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
    #app.run()