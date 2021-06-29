from flask import Flask, json, render_template, session
from flaskwebgui import FlaskUI


app = Flask(__name__)
ui = FlaskUI(app, width=600, height=500)
app.config["DEBUG"] = os.environ.get("FLASK_DEBUG", True)
app.config["JSON_AS_ASCII"] = False
app.config['SECRET_KEY'] = 'dev'
app.config.from_mapping(
    BASE_URL="http://localhost:5000",
)

@app.route('/')
def index():
    return render_template('index.html')


if __name__ == "__main__":
    # app.run() for debug
    ui.run()
