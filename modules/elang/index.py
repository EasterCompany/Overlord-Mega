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


@overlord.route('/')
def _home_page_():
    return EDOC("home").compiler()


@overlord.route('/e/elang')
def _elang_page_():
    return EDOC("elang").compiler()


@overlord.route('/e/overlord')
def _overlord_page_():
    return EDOC("overlord").compiler()


@overlord.route('/e/genesis')
def _genesis_page_():
    return EDOC("genesis").compiler()


@overlord.route('/e/login')
def _login_page_():
    return EDOC("login").compiler()


@overlord.route('/api', methods=["GET", "POST"])
def _api_distribution_():
    return api_service()


# =====================================================================
