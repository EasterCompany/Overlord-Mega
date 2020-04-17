# PROJECT IMPORTS
from modules.services.api_manager import service as api_service

# SUPPORTED THIRD-PARTY IMPORTS
from flask import Blueprint

# ELANG IMPORTS
from modules.elang.edocs import eDoc

# PROJECT APPLICTION
overlord = Blueprint(
    "overlord",
    "overlord",
    template_folder="templates"
)
app = {
    "home": eDoc("home").local(),
    "elang": eDoc("elang").local(),
    "overlord": eDoc("overlord").local(),
    "genesis": eDoc("genesis").local(),
    "login": eDoc("login").local(),
}

# ======================== WEB APP ROUTE INDEX ========================


@overlord.route('/')
def _home_page_():
    return app["home"]


@overlord.route('/e/elang')
def _elang_page_():
    return app["elang"]


@overlord.route('/e/overlord')
def _overlord_page_():
    return app["overlord"]


@overlord.route('/e/genesis')
def _genesis_page_():
    return app["genesis"]


@overlord.route('/e/login')
def _login_page_():
    return app["login"]


@overlord.route('/api', methods=["GET", "POST"])
def _api_distribution_():
    return api_service()
