from src.pkg.database.models import Client, Transaction
from src.pkg.jwt_manager.main import JwtManager
from src.pkg.clock.main import get_seconds_since_epoch
from src.pkg.logger.main import Logger


class ClientController:
    def __init__(self, jwt_manager: JwtManager, logger: Logger):
        self.jwt_manager = jwt_manager
        self.logger = logger

    # ROUTE TO REGISTER
    def register(self, login: str, password: str):
        if Client.get(login=login):
            return 404, {
                'ok': False,
                'message': "login exists"
            }
        client = Client(login=login, password=password).save()
        Transaction(amount=100, receiver_id=client.id).save() # initial transaction
        self.logger.success(f"CLIENT REGISTERED | uuid: {client.uuid}")
        return self._generate_jwt(client)


    # ROUTE TO GET NEW JWT TOKEN
    def authenticate(self, login: str, password: str):
        client = Client.get(login=login, password=password)
        if not client:
            return 404, {
                'ok': False,
                'message': "invalid credentials"
            }
        return self._generate_jwt(client)

    def _generate_jwt(self, client):
        expiration_time = get_seconds_since_epoch() + 600  # 5 minutes expiration time
        jwt_token = self.jwt_manager.encode(
            {
                "client": {
                    "id": client.id,
                    "uuid": str(client.uuid),
                    "login": client.login,
                    "password": client.password
                },
                "expiration_time": expiration_time
            }
        )
        self.logger.info(f"JWT TOKEN GENERATED FOR CLIENT | uuid: {client.uuid}")
        return 200, {
            'ok': True,
            'message': "success",
            'content': {
                "data": {
                    "jwt_token": jwt_token,
                    "expiration_time": expiration_time
                }
            }
        }
