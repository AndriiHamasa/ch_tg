from loguru import logger
import sys


logger.remove()


logger.add(
    sys.stdout,
    format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan> - <level>{message}</level>",
    level="INFO"
)

logger.add(
    "logs/app_{time: YYYY-MM-DD HH:mm:ss}.log",
    rotation="00:00",
    retention="30 days",
    compression="zip",
    format="{time: YYYY-MM-DD HH:mm:ss} | {level} | {name}:{function} | {message}",
    level="DEBUG"
)

logger.add(
    "logs/json_ {time: YYYY-MM-DD HH:mm:ss}.json",
    rotation="00:00",
    retention="30 days",
    serialize=True,
    level="INFO"
)


# add error logs