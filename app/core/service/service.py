import logging
from fastapi import HTTPException, status

from tortoise.exceptions import BaseORMException

logger = logging.getLogger(__name__)


