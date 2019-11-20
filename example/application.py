import logging

LOGGER_FORMAT = '%(asctime)s %(name)s %(levelname)-8s %(message)s'


def initialize():
    _setup_logger()


def _setup_logger():
    logger = logging.getLogger(__name__)
    handler = logging.StreamHandler()

    formatter = logging.Formatter(LOGGER_FORMAT)
    handler.setFormatter(formatter)

    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)
