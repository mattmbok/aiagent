import os
import subprocess
from google.genai import types


def run_python_file(working_directory, file_path, args=[]):
    file_dir_path = os.path.join(working_directory, file_path)
    try:
        if not os.path.abspath(file_dir_path).startswith(os.path.abspath(working_directory)):
            raise PermissionError
        if not os.path.isfile(file_dir_path):
            raise FileNotFoundError
        if not file_dir_path.endswith(".py"):
            raise TypeError
        completed_process = subprocess.run(["python", f"{file_path}", *args], capture_output=True, timeout=30, cwd=f"{working_directory}")
        result = f"STDOUT: {completed_process.stdout}\nSTDERR: {completed_process.stderr}\n"
        if completed_process.returncode != 0: 
            result += f"Process exited with code {completed_process.returncode}\n"
        if not completed_process.stdout:
            result += "No output produced."
        return result
        
    except PermissionError:
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    except FileNotFoundError:
        return f'Error: File "{file_path}" not found.'
    except TypeError:
        return f'Error: "{file_path}" is not a Python file.'
    except Exception as e:
        return f"Error: executing Python file: {e}"
    

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Run a Python file with the specified arguments, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The Python file to be executed, relative to the working directory.",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                items=types.Schema(
                    type=types.Type.STRING,
                    description="Single command-line argument to the Python file.",
                ),
                description="The arguments to be provided to the python program from the file.",
            )
        },
    ),
)