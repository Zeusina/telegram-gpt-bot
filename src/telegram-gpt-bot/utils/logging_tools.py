import logging
from colorama import init, Fore


def configurate_logging():
    init()
    logging.basicConfig(level=logging.DEBUG,
                        format=Fore.BLACK + "%(asctime)s" + Fore.CYAN + " %(levelname)s      "
                               + Fore.RED + "%(name)s-%(funcName)s" + " %(message)s")


def get_logger(name: str = __name__, level: int = logging.DEBUG) -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(level)
    return logger

