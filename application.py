from flask import Flask, jsonify
from session import Session, engine
from models.model import Base
from blueprints.blacklist import blacklist_blueprint

application  = app = Flask(__name__)
application.register_blueprint(blacklist_blueprint)

Base.metadata.create_all(engine)

if __name__ == "__main__":
    application.run(port = 5000, debug = True)


#@app.errorhandler(ApiError)
# def handle_exception(err):
#     response = {
#       "msg": err.description 
#     }
#     return jsonify(response), err.code
