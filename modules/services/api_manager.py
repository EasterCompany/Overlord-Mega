# -*- coding: utf-8 -*-

# Standard Library Imports
import time
from flask import redirect, request, jsonify

# eLang Module Imports
from modules.elang.basic import git


# API MANAGER SERVICE
def service():

	# fetch requested parameter from url
	req = request.args.get("req")

	# test if service is responding
	if req == "__test__":
		return jsonify(
			{"error": 0}
		)

	# API SERVICES AVAILABLE TO CALL =============

	# server time api
	elif req == "time":
		return str(time.time())

	# documents api
	elif req == "doc":
		return git(request.args.get("doc")).read()

	# ===== END OF CALLABLE SERVICES =============

	# if not service was found
	elif req is not None:
		return jsonify(
			{"error": 1}
		)
	else:
		return redirect("/")
