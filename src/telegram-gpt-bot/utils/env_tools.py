import sys
import pathlib
import dotenv
import logging


def get_env_from_file():
    dotenv_path=pathlib.Path(sys.path[0]).absolute().parent.parent.joinpath(".env")
    logging.debug("Path for .env file: " + str(dotenv_path))
    dotenv.load_dotenv(dotenv_path=dotenv_path)

