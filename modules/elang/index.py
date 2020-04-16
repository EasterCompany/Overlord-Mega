# PROJECT IMPORTS
from modules.services.api_manager import service as api_service

# SUPPORTED THIRD-PARTY IMPORTS
from flask import Blueprint

# ELANG IMPORTS
from modules.elang.edocs import EDOC

# PROJECT APPLICTION
overlord = Blueprint(
	"overlord",
	"overlord",
	template_folder="templates"
)

# ======================== WEB APP ROUTE INDEX ========================

""" HOME PAGE (www.easter.company/)

	home page app and page index for
	hosted domain (easter.company)
	and (eastercompany.co.uk)
"""
@overlord.route('/')
def _home_page_():
	return EDOC("home").test()


""" ELANG PAGE (www.easter.company/e/elang)


"""
@overlord.route('/e/elang')
def _elang_page_():
	return EDOC("elang").test()


""" OVERLORD PAGE (www.easter.company/e/overlord)


"""
@overlord.route('/e/overlord')
def _overlord_page_():
	return EDOC("overlord").test()


""" GENESIS PAGE (www.easter.company/e/gensis)


"""
@overlord.route('/e/genesis')
def _genesis_page_():
	return EDOC("genesis").test()


""" LOGIN PAGE (www.easter.company/e/login)


"""
@overlord.route('/e/login')
def _login_page_():
	return EDOC("login").test()


""" API DISTRIBUTION (.../api)

	capable of distributing api
	services from this domain
"""
@overlord.route('/api', methods=["GET", "POST"])
def _api_distribution_():
	return api_service()
