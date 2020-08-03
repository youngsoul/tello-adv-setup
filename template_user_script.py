from template_user_config import SAMPLE_CONFIG_ITEM
import logging

LOGGER = logging.getLogger()


def init(tello, fly_flag=False):
    LOGGER.debug(f"Inside init method.  fly_flag: {fly_flag}, sample config item: {SAMPLE_CONFIG_ITEM}")
    pass

def handler(tello, frame, fly_flag=False):
    LOGGER.debug(f"Inside handler method.  fly_flag: {fly_flag}, sample config item: {SAMPLE_CONFIG_ITEM}")
    pass