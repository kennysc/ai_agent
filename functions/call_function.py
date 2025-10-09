from google.genai import types
from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.run_python_file import run_python_file
from functions.write_file import write_file

def call_function(function_call_part, verbose=False):
    function_name = function_call_part.name
    function_args = function_call_part.args

    working_directory = "./calculator"
    possible_functions = [
        "get_files_info",
        "get_file_content",
        "run_python_file",
        "write_file"
    ]
    function_output = ""

    if verbose:
        print(f"Calling function: {function_name}({function_args})")
    else:
        print(f" - Calling function: {function_name}")

    if function_name not in possible_functions:
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_name,
                    response={"error": f"Unknown function: {function_name}"}
                )
            ]
        )

    if function_name == "get_files_info":
        function_output = get_files_info(working_directory, **function_args)
    if function_name == "get_file_content":
        function_output = get_file_content(working_directory, **function_args)
    if function_name == "run_python_file":
        function_output = run_python_file(working_directory, **function_args)
    if function_name == "write_file":
        function_output = write_file(working_directory, **function_args)

    return types.Content(
        role="tool",
        parts=[
            types.Part.from_function_response(
                name=function_name,
                response={"result": function_output}
            )
        ]
    )

