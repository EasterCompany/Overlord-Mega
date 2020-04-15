# PROJECT IMPORTS
from modules.services.api_manager import service as api_service

# SUPPORTED THIRD-PARTY IMPORTS
from flask import Blueprint

# ELANG IMPORTS
from modules.elang.edocs import EDOC

# PROJECT APPLICTION
overlord = Blueprint(
    "Overlord",
    "index",
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
    return EDOC("home").compiler()


""" ELANG PAGE (www.easter.company/elang)

    
"""
@overlord.route('/elang')
def _elang_page_():
    return EDOC("elang").compiler()


""" OVERLORD PAGE (www.easter.company/overlord)

    
"""
@overlord.route('/overlord')
def _overlord_page_():
    return EDOC("overlord").compiler()


""" GENESIS PAGE (www.easter.company/gensis)

    
"""
@overlord.route('/genesis')
def _genesis_page_():
    return EDOC("genesis").compiler()


""" LOGIN PAGE (www.easter.company/login)

    
"""
@overlord.route('/login')
def _login_page_():
    return EDOC("login").compiler()


""" API DISTRIBUTION (.../api)

	capable of distributing api
	services from this domain
"""
@overlord.route('/api', methods=["GET", "POST"])
def _api_distribution_():
    return api_service()
