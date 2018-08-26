from flask import Flask
from flask import jsonify

import westcoast
import tasman
import kawarau

app = Flask(__name__)


@app.route("/tasman")
def getTasman():
    return jsonify(tasman.riverArray)


@app.route("/westcoast")
def getWestCoast():
    return jsonify(westcoast.riverArray)


@app.route("/kawarau")
def getKawarau():
    return jsonify(kawarau.riverArray)


if __name__ == "__main__":
    app.run()
