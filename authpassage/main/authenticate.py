from flask import Blueprint,jsonify, request, g
import os
from passageidentity import Passage,PassageError

auth = Blueprint("auth", __name__)

PASSAGE_API_KEY = os.environ.get("PASSAGE_API_KEY")
PASSAGE_ID = os.environ.get("PASSAGE_APP_ID")

try:
    psg = Passage(app_id=PASSAGE_ID,api_key=PASSAGE_API_KEY)
except PassageError as e:
    print(e)
    exit()

@auth.before_request
def before_request():
    try:
        g.user = psg.authenticateRequest(request)
    except PassageError as e:
        return jsonify({"error": e})

@auth.route("/user-info", methods=["GET"])
def get_user_info():
    psg_user = psg.getUser(g.user)

    identifier = ""
    if psg_user.email:
        identifier = psg_user.email
    elif psg_user.phone:
        identifier = psg_user.phone

    return jsonify({"identifier": identifier})