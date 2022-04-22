import logging
from framework.utils.singleton import Singleton


class Logger(metaclass=Singleton):
    def __init__(self):
        pass

    def log_step(self, n_step, description):
        self.info('({n_step}) {dsc}'.format(n_step=n_step, dsc=description))

    def debug(self, message):
        logging.debug('{}'.format(message))

    def info(self, message):
        logging.info('{}'.format(message))

    def warning(self, message):
        logging.warning('{}'.format(message))

    def add_handler(self, handler):
        if handler not in logging.getLogger().handlers:
            logging.getLogger().addHandler(handler)

    def get_logger(self, name=None):
        logging.getLogger(name)

    @staticmethod
    def get_instance():
        return Logger()
