import os

def get_files_info(working_directory, directory="."):
    directory_relative_path = os.path.join(working_directory, directory)
    lst_working_directory = os.listdir(working_directory)
    is_directory = os.path.isdir(directory_relative_path)

    if directory not in lst_working_directory and directory != ".":
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if not is_directory:
        return f'Error: "{directory}" is not a directory'

    try:
        lst_directory = os.listdir(directory_relative_path)
        files_info = []
        for file in lst_directory:
            file_path = os.path.join(directory_relative_path, file)
            file_size = os.path.getsize(file_path)
            is_dir = os.path.isdir(file_path)
            files_info.append(f"- {file}: file_size={file_size} bytes, is_dir={is_dir}")
        return "\n".join(files_info)
    except Exception as e:
        print(f"Error: {e}")
