from fastapi import APIRouter, Request, Response


class ClientRouter:
    def __init__(self, controller, cfg):
        self.controller = controller
        self.cfg = cfg
        self.router = APIRouter()

        @self.router.post('/register')
        async def register(request: Request, response: Response):
            body = await request.json()
            if not "data" in body:
                response.status_code = 400
                return {'ok': False, 'message': 'bad request'}
            data = body["data"]
            if not ("login" in data and "password" in data):
                response.status_code = 400
                return {'ok': False, 'message': 'bad request'}
            status_code, data = self.controller.register(login=data["login"], password=data["password"])
            response.status_code = status_code
            return data

        @self.router.post('/authenticate')
        async def authenticate(request: Request, response: Response):
            body = await request.json()
            if not "data" in body:
                response.status_code = 400
                return {'ok': False, 'message': 'bad request'}
            data = body["data"]
            if not ("login" in data and "password" in data):
                response.status_code = 400
                return {'ok': False, 'message': 'bad request'}
            status_code, data = self.controller.authenticate(login=data["login"], password=data["password"])
            response.status_code = status_code
            return data
