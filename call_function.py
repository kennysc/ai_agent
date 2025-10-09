from google.genai import types

from functions.get_files_info import schema_get_files_info, get_files_info
from functions.get_file_content import schema_get_file_content, get_file_content
from functions.run_python_file import schema_run_python_file, run_python_file
from functions.write_file import schema_write_file, write_file
from config import WORKING_DIRECTORY

available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,
        schema_get_file_content,
        schema_run_python_file,
        schema_write_file,
    ]
)

def call_function(function_call_part, verbose=False):
    function_name = function_call_part.name
    function_args = function_call_part.args

# Was used instead of functions_mapping before
#    possible_functions = [
#        "get_files_info",
#        "get_file_content",
#        "run_python_file",
#        "write_file"
#    ]

    functions_mapping = {
        "get_files_info": get_files_info,
        "get_file_content": get_file_content,
        "run_python_file": run_python_file,
        "write_file": write_file
    }

    if verbose:
        print(f"Calling function: {function_name}({function_args})")
    else:
        print(f" - Calling function: {function_name}")

    if function_name not in functions_mapping:
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_name,
                    response={"error": f"Unknown function: {function_name}"}
                )
            ]
        )

    function_args["working_directory"] = WORKING_DIRECTORY
    function_output = functions_mapping[function_name](**function_args)

# Ok, so this was my original way of executing the functions, but above is wayyy more elegant
#    function_output = ""
#    if function_name == "get_files_info":
#        function_output = get_files_info(WORKING_DIRECTORY, **function_args)
#    if function_name == "get_file_content":
#        function_output = get_file_content(WORKING_DIRECTORY, **function_args)
#    if function_name == "run_python_file":
#        function_output = run_python_file(WORKING_DIRECTORY, **function_args)
#    if function_name == "write_file":
#        function_output = write_file(WORKING_DIRECTORY, **function_args)
#
    return types.Content(
        role="tool",
        parts=[
            types.Part.from_function_response(
                name=function_name,
                response={"result": function_output}
            )
        ]
    )

