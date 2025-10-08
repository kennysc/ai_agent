import os
from google.genai import types

def get_files_info(working_directory, directory="."):
    try:
        working_abs_path = os.path.abspath(working_directory)
        target_abs_path = os.path.abspath(os.path.join(working_directory, directory))

        # if the absolute target path does not start with the absolute working
        # directory path: output an error
        if not target_abs_path.startswith(working_abs_path):
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        if not os.path.isdir(target_abs_path):
            return f'Error: "{directory}" is not a directory'

        lst_directory = os.listdir(target_abs_path)
        files_info = []
        for file in lst_directory:
            # needs the whole relative filepath. Using only the file variable
            # would cause to look into the directory where the script is executed
            file_path = os.path.join(target_abs_path, file)
            file_size = os.path.getsize(file_path)
            is_dir = os.path.isdir(file_path)
            files_info.append(f"- {file}: file_size={file_size} bytes, is_dir={is_dir}")
        return "\n".join(files_info)
    except Exception as e:
        return f"Error: {e}"

schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)
