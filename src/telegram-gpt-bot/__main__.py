from utils import get_env_from_file, configurate_logging


def main():
    configurate_logging.configurate_logging()
    get_env_from_file.get_env_from_file()


if __name__ == "__main__":
    main()
