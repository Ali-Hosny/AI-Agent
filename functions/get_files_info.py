import os

def get_files_info(working_directory: str, directory: str = ".") -> str:
    working_directory_absolute = os.path.abspath(working_directory)

    target_directory = os.path.normpath(os.path.join(working_directory_absolute, directory))

    is_valid_target = os.path.commonpath([working_directory_absolute, target_directory]) == working_directory_absolute

    if not is_valid_target:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

    if not os.path.isdir(target_directory):
        return f'Error: "{directory}" is not a directory'

    # return f'Success: "{directory}" is within the working directory'

    content: list[str] = []
    try:
        for file in os.listdir(target_directory):
            name: str = file
            size: int = os.path.getsize(os.path.join(target_directory, file))
            is_dir:bool = os.path.isdir(os.path.join(target_directory, file))
            content.append(f"- {file}: file_size={size} bytes, is_dir={is_dir}")
    except Exception as e:
        return f"Error: {str(e)}"

    result: str = "\n".join(content)

    if directory != ".":
        return f"Result for '{directory}' directory:\n" + result
    
    return "Result for current directory:\n" + result


