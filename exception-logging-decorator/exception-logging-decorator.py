import logging
from functools import wraps

# Configure logging
logging.basicConfig(
    filename="exceptions.log",   # where exceptions will be saved
    level=logging.ERROR,         # log only ERROR and above
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def exception_logger(func):
    """Decorator that logs exceptions raised by the wrapped function."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            # log the exception with traceback
            logging.exception(f"Exception in {func.__name__} with args={args}, kwargs={kwargs}")
            print(f"❌ An error occurred in {func.__name__}. Check exceptions.log for details.")
            # re-raise if you want program to crash, or return None to keep running
            return None
    return wrapper


# Example usage
@exception_logger
def divide(a, b):
    return a / b

if __name__ == "__main__":
    print(divide(10, 2))   # works fine
    print(divide(5, 0))    # will trigger ZeroDivisionError and log it

