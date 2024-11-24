import logging
from collections.abc import Callable
from datetime import datetime

logger = logging.getLogger(__name__)

if not logger.hasHandlers():
    logging.basicConfig(
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        level=logging.INFO,
    )
    logger.setLevel(logging.INFO)


def time_cap(fn: Callable):
    """
    time_cap decorator will print the function execution time in milliseconds
    :param fn: Callable
    :return:
    """

    def wrapper(*args, **kwargs):
        start_time = datetime.now()
        result = fn(*args, **kwargs)
        end_time = datetime.now()
        execution_seconds = end_time - start_time
        logging.info(
            f"{fn.__name__} function took "
            f"{execution_seconds.total_seconds() * 1000} milliseconds"
        )
        return result

    return wrapper


@time_cap
def dummy_func():
    import time
    time.sleep(2)


if __name__ == "__main__":
    logging.basicConfig(level="INFO")
    dummy_func()
