import os
import subprocess
from google.genai import types

def run_python_file(working_directory, file_path, args=None):
    try:
        working_dir_abs_path = os.path.abspath(working_directory)
        file_abs_path = os.path.abspath(os.path.join(working_directory, file_path))

        if not file_abs_path.startswith(working_dir_abs_path):
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        if not os.path.exists(file_abs_path):
            return f'Error: File "{file_path}" not found.'
        if not file_path.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file.'

        try:
            commands = ["python3", file_abs_path]
            if args:
                commands.extend(args)
            process = subprocess.run(
                commands, # contatenate additional args
                cwd=working_dir_abs_path,
                timeout=30, # 30 seconds timeout
                capture_output=True # capture stdout and stderr
                )

            # convert stdout and stderr to utf-8 to be able to check if there is an outpur
            # without it it returns the result in bytes and an empty result equals b''
            if process.stdout.decode("utf-8") == "" and process.stderr.decode("utf-8") == "":
                return "No output produced."
            process_output = ""
            process_output += f'STDOUT:\n{process.stdout.decode("utf-8")}\n\nSTDERR:\n{process.stderr.decode("utf-8")}'
            if process.returncode != 0:
                process_output += f"\nProcess exited with code {process.returncode}"
            return process_output

        except Exception as e:
            return f"Error: executing Python file: {e}"

    except Exception as e:
        return f'Error: {e}'

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Run a python script with the provide (optionnal) arguments, within the working directory. It will return stdout and stderror. If no output is produced it will also say so.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The python file to run, relative to the working directory.",
            ),
            "args": types.Schema(
                type=types.Type.STRING,
                description="Optional/depending on the script ran. List of arguments provided to the script.",
            ),
        },
    ),
)
