import os
import pathlib
import dotenv
import logging


def get_env_from_file():
    dotenv_path=pathlib.Path(os.curdir).absolute().parent.joinpath(".env")
    print("Path for .env file: " + str(dotenv_path))
    dotenv.load_dotenv(dotenv_path=dotenv_path)

