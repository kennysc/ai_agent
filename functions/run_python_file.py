import os
import subprocess

def run_python_file(working_directory, file_path, args=[]):
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
            process = subprocess.run([
                "python3",
                file_abs_path] + args, # contatenate additional args
                cwd=working_dir_abs_path,
                timeout=30, # 30 seconds timeout
                capture_output=True # capture stdout and stderr
            )

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
