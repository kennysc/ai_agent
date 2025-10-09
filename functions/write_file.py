import os
from google.genai import types

def write_file(working_directory, file_path, content):
    try:
        working_dir_abs_path = os.path.abspath(working_directory)
        file_abs_path = os.path.abspath(os.path.join(working_directory, file_path))

        if not file_abs_path.startswith(working_dir_abs_path):
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
        if not os.path.exists(os.path.dirname(file_abs_path)):
            os.makedirs(os.path.dirname(file_abs_path))

        with open(file_abs_path, "w") as f:
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

    except Exception as e:
        return f'Error: {e}'

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Will write the specified content to a file, within the working directory",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path of the file where the content will be written. Careful, if there is already content in the file it will be overwritten.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="Content provided as a string to be written in the file.",
            ),
        },
    ),
)
