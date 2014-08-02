# Dommert Flask-Rum Loader
from flask import Flask, render_template
from flask_rum.main import rum
import flask_rum.rum_config


app = Flask(__name__)
app.register_blueprint(rum)
app.config.from_object(flask_rum.rum_config)
app.config.THEME_FOLDER='rum/banana/'

@app.route('/fuckyou')
def fuckyou(title='fuck'):
    return 'Fuck you Cunt'

@app.route('/suckit')
def suckit(title='Home '):
    return render_template('site/frontpage2.html', title=title)


if __name__ == '__main__':
    app.run(host='localhost', port=app.config['PORT'])