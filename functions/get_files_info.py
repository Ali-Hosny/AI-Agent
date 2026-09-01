import os

def get_files_info(working_directory: str, directory: str = ".") -> str:
    working_directory_absolute = os.path.abspath(working_directory)

    target_directory = os.path.normpath(os.path.join(working_directory_absolute, directory))

    is_valid_target = os.path.commonpath([working_directory_absolute, target_directory]) == working_directory_absolute

    if not is_valid_target:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

    if not os.path.isdir(target_directory):
        return f'Error: "{directory}" is not a directory'

    return f'Success: "{directory}" is within the working directory'