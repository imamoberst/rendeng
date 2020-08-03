from flask import Flask
from models import home_view

app = Flask(__name__)
app.register_blueprint(home_view)
if __name__ == '__main__':
    app.run(port=8080, debug=True)
