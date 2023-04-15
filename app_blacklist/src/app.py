from flask import Flask, jsonify
from .session import Session, engine
from .models.model import Base
from .blueprints.blacklist import blacklist_blueprint


app = Flask(__name__)
app.register_blueprint(blacklist_blueprint)

Base.metadata.create_all(engine)

#@app.errorhandler(ApiError)
# def handle_exception(err):
#     response = {
#       "msg": err.description 
#     }
#     return jsonify(response), err.code