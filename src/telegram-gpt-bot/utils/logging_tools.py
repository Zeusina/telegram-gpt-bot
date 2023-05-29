import logging
from colorama import init, Fore


def configurate_logging():
    init()
    logging.basicConfig(level=logging.DEBUG,
                        format=Fore.BLACK + "%(asctime)s" + Fore.CYAN + " %(levelname)s      "
                               + Fore.RED + "%(funcName)s" + " %(message)s")


def get_logger(name: str = __name__, level: int = logging.DEBUG) -> logging.Logger:
    logger = logging.getLogger(name)
    logger_stream_handler = logging.StreamHandler()
    logger_formatter = logging.Formatter(Fore.BLACK + "%(asctime)s" + Fore.CYAN + " %(levelname)s      "
                                         + Fore.RED + "%(funcName)s" + " %(message)s")
    logger_stream_handler.setFormatter(logger_formatter)
    logger.addHandler(logger_stream_handler)
    logger.setLevel(level)
    return logger

