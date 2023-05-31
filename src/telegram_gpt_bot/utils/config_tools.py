from logging import getLogger
import sys
import os
import pathlib

import yaml


class Config:

    @staticmethod
    def get_instance():
        if '_instance' not in Config.__dict__:
            Config._instance = Config()
        return Config._instance

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Config, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        self.logger = getLogger("utils/config")
        config_path = pathlib.Path(sys.path[0]).absolute().parent.parent.joinpath("config.yaml")
        self.logger.info("Search config file in: " + str(config_path))
        if os.path.exists(config_path):
            self.logger.info("Start parsing config file...")
            with open(config_path) as f:
                config: dict = yaml.load(f, Loader=yaml.FullLoader)
                self.config = config
                self.logger.debug(self.config)
        else:
            self.logger.warning("Config file not found\nFind in: " + str(config_path))
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
