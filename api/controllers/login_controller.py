import connexion

from templates.api.services.login_service import LoginService

def login_controller():

    if connexion.request.method == "POST":
        ls = LoginService()
        print("connexion is working")

    return "working"