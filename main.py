from config.main import Config
from src.pkg.logger.main import Logger
from src.main import App


if __name__ == '__main__':
    cfg = Config("config/config.yml").load()
    logger = Logger(filename='auth.log', name='AUTH', cfg=cfg)
    app = App(cfg, logger)
    app.run()
