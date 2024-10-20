from flask import Flask
from flask import render_template

apphola = Flask(__name__)

@apphola.route('/')
def index ():
    return render_template('index.html')

if __name__ == "__main__":
    apphola.run(debug=True, port=5505)