import logging
from logging.handlers import TimedRotatingFileHandler  # , RotatingFileHandler


class LogsDefault:
    """definicoes da aplicacao"""

    def __init__(self) -> None:
        self.logger: logging.Logger = self.get()

    def get(self) -> logging.Logger:
        handlertime = TimedRotatingFileHandler(
            "logs/testes.log", when="d", interval=1, backupCount=5
        )
        # handlersize = RotatingFileHandler("server.log", maxBytes=2048, backupCount=5)
        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s - %(levelname)s - %(message)s",
            handlers=[handlertime],  # , handlersize]
        )
        return logging.getLogger("testes")


logger = LogsDefault().get()
