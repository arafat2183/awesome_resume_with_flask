from templates.api.services import BaseArwfService


class LoginService(BaseArwfService):
    def __init__(self) -> None:
        """
        Constructor of the BaseArwfService
        """
        super().__init__()
        