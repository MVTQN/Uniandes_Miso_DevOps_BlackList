from flask import Flask, jsonify, request, Blueprint
from commands.add_email import AddEmail
from commands.get_email import GetEmail
blacklist_blueprint = Blueprint('blacklist', __name__)

@blacklist_blueprint.route('/blacklist', methods = ['POST'])
def add() :
    if auth_token() == True:
        ip = request.remote_addr
        email_added = AddEmail(request.get_json(),ip).execute()
        return email_added
    else:
        return jsonify("Acceso no autorizado ")
    


@blacklist_blueprint.route('/', methods = ['GET'])
def root() :
    return jsonify("hola ")

@blacklist_blueprint.route('/blacklist/<string:email>', methods = ['GET'])
def getEmail(email) :
    if auth_token() == True:
        query = GetEmail(email).execute()
        return jsonify(query)
    else:
        return jsonify("Acceso no autorizado ")
def auth_token():
    if 'Authorization' in request.headers:
        authorization = request.headers['Authorization']
        print (authorization)
        if authorization == "Bearer maxima_seguridad":
            return True
    else:
        authorization = None
        return False




