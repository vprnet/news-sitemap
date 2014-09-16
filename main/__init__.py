from flask import Flask

app = Flask(__name__)

from main import views

if __name__ == '__main__':
    app.debug = True
    app.run()
