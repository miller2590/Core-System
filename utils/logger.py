import logging


class Logger:
    def __init__(self, name=__name__, log_file=None, level=logging.DEBUG):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)

        # Create console handler with a higher log level
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)

        # Create formatter and add it to the handlers
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - [%(levelname)s] -> %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S')
        ch.setFormatter(formatter)

        # Add the console handler to the logger
        self.logger.addHandler(ch)

        # Create file handler if log_file is provided
        if log_file:
            fh = logging.FileHandler(log_file)
            fh.setLevel(logging.DEBUG)
            fh.setFormatter(formatter)
            self.logger.addHandler(fh)

    @staticmethod
    def get_logger(name=None, log_file=None, level=logging.DEBUG):
        logger_instance = Logger(name, log_file, level)
        return logger_instance.logger

