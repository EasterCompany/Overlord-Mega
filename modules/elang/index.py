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


<<<<<<< HEAD
=======
	home page app and page index for
	hosted domain (easter.company)
	and (eastercompany.co.uk)
"""
>>>>>>> 4b3f04acdf8fffacda491b93138850e0bd60adcf
@overlord.route('/')
def _home_page_():
	return EDOC("home").test()


<<<<<<< HEAD
=======
""" ELANG PAGE (www.easter.company/e/elang)


"""
>>>>>>> 4b3f04acdf8fffacda491b93138850e0bd60adcf
@overlord.route('/e/elang')
def _elang_page_():
	return EDOC("elang").test()


<<<<<<< HEAD
=======
""" OVERLORD PAGE (www.easter.company/e/overlord)


"""
>>>>>>> 4b3f04acdf8fffacda491b93138850e0bd60adcf
@overlord.route('/e/overlord')
def _overlord_page_():
	return EDOC("overlord").test()


<<<<<<< HEAD
=======
""" GENESIS PAGE (www.easter.company/e/gensis)


"""
>>>>>>> 4b3f04acdf8fffacda491b93138850e0bd60adcf
@overlord.route('/e/genesis')
def _genesis_page_():
	return EDOC("genesis").test()


<<<<<<< HEAD
=======
""" LOGIN PAGE (www.easter.company/e/login)


"""
>>>>>>> 4b3f04acdf8fffacda491b93138850e0bd60adcf
@overlord.route('/e/login')
def _login_page_():
	return EDOC("login").test()


@overlord.route('/api', methods=["GET", "POST"])
def _api_distribution_():
<<<<<<< HEAD
    return api_service()


# =====================================================================
=======
	return api_service()
>>>>>>> 4b3f04acdf8fffacda491b93138850e0bd60adcf
