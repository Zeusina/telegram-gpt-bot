from . import logging_tools
import os
import pathlib

import yaml


class Config:
    def __init__(self):
        self.logger = logging_tools.get_logger("config")
        config_path = pathlib.Path(os.curdir).absolute().parent.joinpath("config.yaml")
        self.logger.info("Search config file in: " + str(config_path))
        if os.path.exists(config_path):
            self.logger.info("Start parsing config file...")
            with open(config_path) as f:
                self.config: dict = yaml.load(f, Loader=yaml.FullLoader)
                self.logger.debug(self.config)
        else:
            self.logger.warning("Config file not found")
            self.logger.info("Using default config...")

    def get_log_level(self) -> int:
        log_level = self.config.get("logging").get("level", "CRITICAL")
        match log_level:
            case "DEBUG":
                return 10
            case "INFO":
                return 20
            case "WARN":
                return 30
            case "ERROR":
                return 40
            case "CRITICAL":
                return 50
            case _:
                self.logger.warning("Config level not right. Using CRITICAL level.")
                return 50