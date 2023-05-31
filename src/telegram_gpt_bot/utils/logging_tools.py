import logging
from colorama import init, Fore
from src.telegram_gpt_bot.utils.config_tools import Config


def configurate_logging(level: int = 50):
    init()
    logging.basicConfig(level=level,
                        format=Fore.BLACK + "%(asctime)s" + Fore.CYAN + " %(levelname)s      "
                               + Fore.RED + "%(name)s - %(funcName)s" + " %(message)s")


def get_logger(name: str = __name__, level: int = logging.CRITICAL) -> logging.Logger:
    config = Config.get_instance()
    logger = logging.getLogger(name)
    logger.setLevel(config.get_log_level())
    return logger

