#utils.py
import os
import datetime

def read_file(file_path):
    """
    Reads the contents of a file and returns it as a string.
    Args:
        file_path (str): The path to the file.
    Returns:
        str: The contents of the file.
    """
    with open(file_path, 'r') as file:
        return file.read()

def write_file(file_path, content):
    """
    Writes the given content to a file.
    Args:
        file_path (str): The path to the file.
        content (str): The content to write.
    """
    with open(file_path, 'w') as file:
        file.write(content)

def get_current_date():
    """
    Returns the current date.
    Returns:
        str: The current date in YYYY-MM-DD format.
    """
    return datetime.date.today().strftime('%Y-%m-%d')

class Logger:
    """
    Helper class for logging application events.
    """
    def __init__(self, filename):
        self.filename = filename
    
    def log(self, message):
        """
        Logs the given message to a log file.
        Args:
            message (str): The message to log.
        """
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        log_message = f"{timestamp} - {message}"
        with open(self.filename, 'a') as file:
            file.write(log_message + '\n')

# Additional utility functions and helper classes can be defined as needed

# END UTILS.PY
