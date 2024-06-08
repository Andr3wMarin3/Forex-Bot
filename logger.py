import os
import datetime

class Logger:
    LOG_LEVELS = {
        "DEBUG": 1,
        "INFO": 2,
        "WARNING": 3,
        "ERROR": 4,
        "CRITICAL": 5,
    }

    def __init__(self, log_file="log.txt", log_level="INFO"):
        self.log_file = log_file
        self.log_level = log_level

        # Create the log file if it doesn't exist
        if not os.path.exists(log_file):
            with open(log_file, "w") as file:
                pass

    def log(self, message, level="INFO"):
        if self.LOG_LEVELS[level] >= self.LOG_LEVELS[self.log_level]:
            current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            try:
                with open(self.log_file, "a") as file:
                    file.write(f"{current_time} - {level} - {message}\n")
            except Exception as e:
                print(f"Error writing to log file: {e}")

# Example usage
logger = Logger(log_file="my_app.log", log_level="DEBUG")  # Customize log file and level

logger.log("Starting application", level="INFO")
logger.log("Debug message", level="DEBUG")
logger.log("Warning message", level="WARNING")
