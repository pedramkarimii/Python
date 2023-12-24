import functools
import datetime

class FileLoggerDecorator:
    def __init__(self, input_file_address, output_file_address):
        """Initialize the decorator with file addresses."""
        self.input_file_address = input_file_address
        self.output_file_address = output_file_address

    def __call__(self, func):
        """Decorator entry point - logs the function call and file inputs, and delegates to the original function."""
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            """Logs the function call and file inputs in a new file."""
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            log_filename = f"log_{timestamp}.txt"

            # Log the function call along with the file inputs
            log_message = f"{timestamp} - Function '{func.__name__}' called. Read File: {self.input_file_address}, Save File: {self.output_file_address}\n"

            with open(log_filename, 'a') as log_file:
                log_file.write(log_message)

            # Call the original function with the file inputs
            func(self.input_file_address, self.output_file_address, *args, **kwargs)

        return wrapper

# Example usage:

def process_file(input_file, output_file):
    """An example function that reads from one file and saves to another."""
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        content = infile.read()
        outfile.write(content)
    print(f"File processed and saved successfully.")

# Get the addresses of the files from user input
input_file_address = input("Enter the address of the file to read: ")
output_file_address = input("Enter the address of the file to save: ")

# Apply the decorator to the function with the provided file addresses
@FileLoggerDecorator(input_file_address, output_file_address)
def decorated_process_file(input_file, output_file):
    """Decorated version of the process_file function."""
    process_file(input_file, output_file)

# Call the decorated function
decorated_process_file()
