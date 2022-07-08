import sys
from loguru import logger

logger.add(sys.stderr, format='[{time:YYYY-MM-DD HH:mm:ss}] {level: <8}: {message}')
