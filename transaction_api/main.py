from config.main import Config
from src.main import App
from src.pkg.database.main import Database
from src.pkg.logger.main import Logger


if __name__ == '__main__':
    cfg = Config("config/config.yml").load()
    logger = Logger(filename='api.log', logger_name='api', cfg=cfg)
    db = Database(cfg, logger=logger)
    app = App(cfg, db, logger=logger)
    app.run()
