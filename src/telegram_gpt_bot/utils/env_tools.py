import sys
import os
import pathlib
import dotenv
from .logging_tools import get_logger


def get_env_from_file():
    logger = get_logger("env_tools")
    dotenv_path = pathlib.Path(sys.path[0]).absolute().parent.parent.joinpath(".env")
    if os.path.exists(dotenv_path):
        logger.debug("Loading dotenv file: " + str(dotenv_path))
        dotenv.load_dotenv(dotenv_path=dotenv_path)
    else:
        logger.warning("Dotenv file not found in: " + str(dotenv_path))