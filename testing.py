from src.logger import get_logger
from src.custom_exception import CustomException
import sys

logger = get_logger(__name__)

def divide_number(a, b):
    try:
        result =  a / b
        logger.info(f"Division of {a} by {b} is {result}")
    except Exception as e:
        logger.error("Error occured")
        raise CustomException("Division by zero", sys)

if __name__ == "__main__":
    try:
        logger.info("Starting the program")
        divide_number(10, 0)
        divide_number(10, 2)
    except CustomException as ce:
        logger.error(str(ce))