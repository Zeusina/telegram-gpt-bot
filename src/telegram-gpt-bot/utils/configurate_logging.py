import logging
from colorama import init, Fore


def configurate_logging():
    init()
    logging.basicConfig(level=logging.DEBUG,
                        format=Fore.BLACK + "%(asctime)s" + Fore.CYAN + " %(levelname)s      "
                        + Fore.RED + "%(funcName)s" + " %(message)s")