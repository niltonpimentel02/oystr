from flask import Flask
from .execution_process import routes

app = Flask(__name__)
routes(app)
if __name__ == '__main__':
    app.run()
