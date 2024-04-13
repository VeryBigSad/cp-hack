import logging
import os
import sys

from dotenv import load_dotenv
from pydantic import ValidationError

from config import ConfigsValidator

logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
root_logger = logging.getLogger()
root_logger.removeHandler(*root_logger.handlers)
consoleHandler = logging.StreamHandler()
consoleHandler.setFormatter(logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s"))
root_logger.addHandler(consoleHandler)

_logger = logging.getLogger(__name__)

# This flag available only in production enviroment
is_prod = os.environ.get("IS_PROD", False) in [1, True, "true", "True"]

if is_prod:
    root_logger.setLevel(logging.INFO)
else:
    root_logger.setLevel(logging.DEBUG)
    load_dotenv()

try:
    config_parameters = ConfigsValidator(**os.environ)
except ValidationError as e:
    _logger.critical(exc_info=e, msg="Env parameters validation")
    sys.exit(-1)
config_parameters.IS_PROD = is_prod
