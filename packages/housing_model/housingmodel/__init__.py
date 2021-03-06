import logging

from housingmodel.config import config
from housingmodel.config import logging_config


VERSION_PATH = config.PACKAGE_ROOT / "VERSION"

# Configure logger for use in package
logger = logging.getLogger(__name__)

# set the level to DEBUG so all messages will be printed in the console
# the default level is usually WARNING
logger.setLevel(logging.DEBUG)
logger.addHandler(logging_config.get_console_handler())
logger.propagate = False


with open(VERSION_PATH, "r") as version_file:
    # assign the version of the package to __version__ from the VERSION file
    __version__ = version_file.read().strip()
