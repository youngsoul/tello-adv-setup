import logging

LOGGER = logging.getLogger()

# User Configuration
SAMPLE_CONFIG_ITEM = 42


def init(tello, fly_flag=False):
    LOGGER.debug(f"Inside init method.  fly_flag: {fly_flag}, sample config item: {SAMPLE_CONFIG_ITEM}")
    pass


def handler(tello, frame, fly_flag=False):
    LOGGER.debug(f"Inside handler method.  fly_flag: {fly_flag}, sample config item: {SAMPLE_CONFIG_ITEM}")
    pass
