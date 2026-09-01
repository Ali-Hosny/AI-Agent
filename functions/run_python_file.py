import os
import subprocess

def run_python_file(
    working_directory: str, file_path: str, args: list[str] | None = None
) -> str:
    working_directory_absolute = os.path.abspath(working_directory)
    target_file = os.path.normpath(os.path.join(working_directory_absolute, file_path))
    is_valid_target = os.path.commonpath([working_directory_absolute, target_file]) == working_directory_absolute
    
    if not is_valid_target:
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

    if not os.path.isfile(target_file):
        return f'Error: "{file_path}" does not exist or is not a regular file'

    if not file_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file'

    command = ["python", target_file]
    if args:
        command.extend(args)

    output: str

    try:
        Completed = subprocess.run(command, capture_output=True, cwd=working_directory_absolute, timeout=30, text=True, check=True)
        if Completed.returncode != 0:
            output = f"Process exited with code {Completed.returncode}"
        if not Completed.stdout and not Completed.stderr:
            output = "No output produced"
        else:
            output = f"STDOUT: {Completed.stdout} STDERR: {Completed.stderr}"
        return output

    except Exception as e:
        return f"Error: executing Python file: {e}"




