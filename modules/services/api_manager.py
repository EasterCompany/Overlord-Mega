import time
from flask import redirect, request, jsonify
from modules.elang.basic import git

'''
API SERVICE MANAGER

lists the requestable API's
that are available through this backend 
application and will return errors or
redirects on incorrect input.
'''


def service():

    req = request.args.get("req")

    if req == "__test__":
        return jsonify(
            {"error": 0}
        )

    elif req == "time":
        return str(time.time())

    elif req == "doc":
        return git(request.args.get("doc")).read()

    # If request is not fulfillable
    elif req is not None:
        return jsonify(
            {"error": 1}
        )

    # If paremeters are unmet
    else:
        return redirect("/")
