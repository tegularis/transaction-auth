import uvicorn
from fastapi import FastAPI
from src.pkg.jwt_manager.main import JwtManager
from src.pkg.logger.main import Logger
from src.api.components.client.controller import ClientController
from src.api.components.client.router import ClientRouter


class App:
    def __init__(self, cfg, logger: Logger):
        self.cfg = cfg
        jwt_manager = JwtManager(cfg)
        client_controller = ClientController(jwt_manager=jwt_manager, logger=logger)

        self.app = FastAPI()
        self.app.include_router(
            ClientRouter(controller=client_controller, cfg=cfg).router, prefix="/client")

    def run(self):
        uvicorn.run(self.app, host=self.cfg["app"]["host"], port=self.cfg["app"]["port"])