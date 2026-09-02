import os

MAX_CHARS = 10000

def get_file_content(working_directory: str, file_path: str) -> str:
    working_directory_absolute = os.path.abspath(working_directory)
    target_file = os.path.normpath(os.path.join(working_directory_absolute, file_path))
    is_valid_target = os.path.commonpath([working_directory_absolute, target_file]) == working_directory_absolute

    if not is_valid_target:
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.isfile(target_file):
        return f'Error: file is not found or is not a regular file: "{file_path}"'

    try:
        with open(target_file, "r") as file:
            content_string = file.read(MAX_CHARS)

            if file.read(1):
                content_string += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'

            return content_string
    except Exception as e:
        return f"Error: {str(e)}"


schema_get_file_content = {
    "type": "function",
    "function": {
        "name": "get_file_content",
        "description": "Reads the content of a file in the working directory",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "Directory path to list files from, relative to the working directory (default is the working directory itself)",
                },
            },
        },
    },
}