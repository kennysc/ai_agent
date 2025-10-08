import os
from functions.config import *

def get_file_content(working_directory, file_path):
    try:
        working_abs_path = os.path.abspath(working_directory)
        target_abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))

        # if the absolute target file path does not start with the absolute working
        # directory path: output an error
        if not target_abs_file_path.startswith(working_abs_path):
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(target_abs_file_path):
            return f'Error: File not found or is not a regular file: "{file_path}"'

        with open(target_abs_file_path, "r") as f:
            content = f.read(MAX_CHARS)
            # get_size return the number of bytes, which is equivalent to the
            # number of characters
            if not os.path.getsize(target_abs_file_path) >= MAX_CHARS:
                return content
            return f'{content}\n[...File "{file_path}" truncated] at {MAX_CHARS} characters'
    except Exception as e:
        return f"Error: {e}"
