import os

def write_file(working_directory: str, file_path: str, content: str) -> str:
    working_directory_absolute = os.path.abspath(working_directory)
    target_file = os.path.normpath(os.path.join(working_directory_absolute, file_path))
    is_valid_target = os.path.commonpath([working_directory_absolute, target_file]) == working_directory_absolute
    
    if not is_valid_target:
        return f'Error: Cannot write "{file_path}" as it is outside the permitted working directory'
        
    if os.path.isdir(file_path):
        return f'Error: Cannot write to "{file_path}" as it is a directory'

    os.makedirs(os.path.dirname(target_file), exist_ok=True)

    try:
        with open(target_file, "w") as file:
            file.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f"Error: {str(e)}"



schema_write_file = {
    "type": "function",
    "function": {
        "name": "write_file",
        "description": "Writes content to a file in the working directory",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "Directory path to list files from, relative to the working directory (default is the working directory itself)",
                },
                "content": {
                    "type": "string",
                    "description": "Content to write to the file",
                },
            },
        },
    },
}    